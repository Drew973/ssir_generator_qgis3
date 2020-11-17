# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal,QDate,QUrl

from PyQt5.QtWidgets import QComboBox,QLineEdit,QCompleter
from qgis.PyQt.QtWidgets import QFileDialog

from . import widget_value,layer_functions,file_dialogs

from qgis.utils import iface

import csv
import collections
from qgis.core import QgsFeatureRequest,QgsProject,QgsMapLayerProxyModel,QgsRasterLayer



def fixHeaders(path):
    with open(path) as f:
        t=f.read()
    r={'qgsfieldcombobox.h':'qgis.gui','qgsmaplayercombobox.h':'qgis.gui'}
    for i in r:
        t=t.replace(i,r[i])
    with open(path, "w") as f:
        f.write(t)


ui_path=os.path.join(os.path.dirname(__file__), 'ssir_generator_dockwidget_base.ui')
fixHeaders(ui_path)
FORM_CLASS, _ = uic.loadUiType(ui_path)


class ssirGeneratorDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        super(ssirGeneratorDockWidget, self).__init__(parent)

        self.site=None
        self.setupUi(self)
        self.from_selected_button.clicked.connect(self.from_selected)
        self.save_button.clicked.connect(self.save)
        self.clear_button.clicked.connect(self.clear)
        
        self.init_key()
        self.help_button.clicked.connect(self.open_help)

        self.site_box.setInsertPolicy(QComboBox.NoInsert)
        self.site_box.setEditable(True)


#WritableLayer,VectorLayer,PointLayer
        self.layer_box.setFilters(QgsMapLayerProxyModel.VectorLayer|QgsMapLayerProxyModel.PointLayer)
        self.filter_layers()
        QgsProject.instance().layersAdded.connect(self.filter_layers)
        
        
        #special handling for comboboxes
        for k,v in self.key.items():
            if isinstance(v['widget'],QComboBox):
                v['widget'].setLineEdit(QLineEdit())
                if 'items' in v:
                    v['widget'].clear()
                    v['widget'].addItems(v['items'])

                        
        self.rules = (('Surveyed', 'not "csv" is null', 'green', None),('Unsurveyed', '"csv" is null', 'red', None))#rules for symbology
        self.split_button.clicked.connect(lambda:layer_functions.set_rules(self.layer_box.currentLayer(),self.rules))#change symbology
        self.layer_box.layerChanged.connect(self.layer_changed)

        self.layer_changed(self.layer_box.currentLayer())
        self.zoom_button.clicked.connect(self.zoom)

        self.site_box.currentIndexChanged.connect(self.site_box_changed)
        
        self.layer_changed(self.layer_box.currentLayer())
        self.next_site_button.clicked.connect(self.next_site)
        self.last_site_button.clicked.connect(self.last_site)


        

        
    def filter_layers(self):
        #ex=[]
        #iterating through layers already in box results in already exepted layers missing
        #for i in range(0,self.layer_box.count()):
            #layer=self.layer_box.layer(i)
            #if layer:
                
              #  if not layer_valid(layer):
             #       print('invalid:'+layer.name())
            #        ex.append(layer)
           #     else:
          #          print('valid:'+layer.name())
         #   
        #self.layer_box.setExceptedLayerList(ex+self.layer_box.exceptedLayerList())
        self.layer_box.setExceptedLayerList([layer for layer in QgsProject.instance().mapLayers().values() if not layer_valid(layer)])   #QgsMapLayerRegistry.instance().mapLayers().values() for qgis2





  #create ordered dict self.key to link name of attribute to widget and default value
    def init_key(self):
        #site details
        self.key=collections.OrderedDict()
        self.key['site']={'widget':self.site,'default':''}
        self.key['section']={'widget':self.section,'default':''}
        self.key['start_ch']={'widget':self.start_ch,'default':0}
        self.key['end_ch']={'widget':self.end_ch,'default':0}
        self.key['section_length']={'widget':self.section_length,'default':0}
        self.key['assesment_length']={'widget':self.assesment_length,'default':0}

        #survey details
        self.key['surveyor']={'widget':self.surveyor,'default':''}
        self.key['survey_date']={'widget':self.survey_date,'default':QDate.currentDate().toString(widget_value.DATE_FORMAT)}
        self.key['photo_ref']={'widget':self.photo_ref,'default':''}
        self.key['additional_photos']={'widget':self.additional_photos,'default':''}

        #visual assesment
        self.key['surface_type']={'widget':self.surface_type,'default':'TSSC'}
        self.key['aggregate_size']={'widget':self.aggregate_size,'default':''}
        self.key['aggregate_condition']={'widget':self.aggregate_condition,'default':'Good'}
        self.key['inconsistencies']={'widget':self.inconsistencies,'default':'No'}
        self.key['contaminants']={'widget':self.contaminants,'default':'N/A'}
        self.key['local_defects']={'widget':self.local_defects,'default':'N/A'}
        self.key['drainage_adequate']={'widget':self.drainage_adequate,'default':'Yes'}

        #road layout
        self.key['meets_design_specification']={'widget':self.meets_design_specification,'default':'Yes'}
        self.key['appropriate_for_vunerable_users']={'widget':self.appropriate_for_vunerable_users,'default':'Yes'}
        self.key['appropriate_for_turning']={'widget':self.appropriate_for_turning,'default':'Yes'}

        #markings,signs,visibitity
        self.key['markings_clear']={'widget':self.markings_clear,'default':'Yes'}
        self.key['roadside_objects']={'widget':self.roadside_objects,'default':'Yes'}
        self.key['clear_sight_lines']={'widget':self.clear_sight_lines,'default':'Yes'}
        self.key['additional_comments']={'widget':self.additional_comments,'default':'N/A'}

        #recomendation
        self.key['treatment_req']={'widget':self.treatment_req,'default':'Yes'}
        self.key['treatment_type']={'widget':self.treatment_type,'default':'N/A'}
        self.key['change_il']={'widget':self.change_il,'default':'Yes'}
        self.key['other_action_req']={'widget':self.other_action_req,'default':'Road marking survey'}
                


    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
    


    def layer_changed(self,layer):

        if not layer:
            iface.messageBar().pushMessage('ssir generator:no layer')
            return
            
        field='segment_no'
        if layer_valid(layer):
            self.site_box.clear()
            s=[str(int(i)) for i in self.valid_segments()]
            self.site_box.addItems(s)
        #    self.site_box.setCurrentindex(0)
            self.site_box.setCompleter(QCompleter(s))
            self.site_box_changed(self.site_box.currentIndex())#value in site_box might not change. site_box_changed might be called twice

        else:
            iface.messageBar().pushMessage('ssir generator:layer needs fields segment_no and csv')

            
    #change feature to red for unsurveyed,green for surveyed
   # def colour_feats(self) :
    ##    layer=iface.activeLayer()
     #   layer_functions.colour_features(self.surveyed_features(),layer,QtGui.QColor('green'))
     #   layer_functions.colour_features(self.unsurveyed_features(),layer,QtGui.QColor('red'))


    def save(self):
        p=file_dialogs.save_file_dialog(ext='.csv',caption='save as csv',default_name=str(self.segment_no()))
        
        if p:

            self.to_csv(p)
            iface.messageBar().pushMessage('ssir generator:saved to '+p)

            #setting 'csv' field of feature
            f=self.segment_no_to_feat()
            
            #self.colour_feats()
            self.layer_box.currentLayer()
            self.layer_box.currentLayer().startEditing()
            self.layer_box.currentLayer().changeAttributeValue(f.id(), self.layer_box.currentLayer().fields().indexOf('csv'),p)
            self.layer_box.currentLayer().commitChanges()


    def get_site(self):
        return self.site

    def next_site(self):
        i=self.site_box.currentIndex()+1
        if i > self.site_box.count()-1:
            i-=self.site_box.count()
        self.site_box.setCurrentIndex(i)
    

    def last_site(self):
        i=self.site_box.currentIndex()-1
        if i < 0:
            i=self.site_box.count()-1
        self.site_box.setCurrentIndex(i)


#str new_site
    def site_box_changed(self,index):
        if self.site_box.itemText(index):
            new_site=int(self.site_box.itemText(index))
            if new_site in self.valid_segments():
                if new_site!=self.site:
                    f=str(self.segment_no_to_feat(int(new_site))['csv'])
                    self.site=new_site
                    if os.path.exists(f):
                        self.load_csv(f,new_site)
                    else:
                        self.clear()
            else:
                iface.messageBar().pushMessage('ssir generator:segment_no %d not in layer.'%(new_site))
                i=self.site_box.findText(str(self.site))
                if i!=-1:
                    self.site_box.setCurrentIndex(i)



    def valid_segments(self):
        if self.layer_box.currentLayer():
            return layer_functions.distinct_values(self.layer_box.currentLayer(),'segment_no')
        

#attributes to dict
    def to_dict(self):
        return {k:widget_value.get_value(v['widget']) for k,v in self.key.items()}


#opens help/index.html in default browser
    def open_help(self):
        help_path=os.path.join(os.path.dirname(__file__),'help','index.html')
        help_path='file:///'+os.path.abspath(help_path)
        QtGui.QDesktopServices.openUrl(QUrl(help_path))

        

    def from_selected(self):
        sf=self.layer_box.currentLayer().selectedFeatures()

        if len(sf)==0:
            iface.messageBar().pushMessage('ssir generator: no features selected')

        if len(sf)>1:
            iface.messageBar().pushMessage('ssir generator: more than 1 feature selected')

        if len(sf)==1:
            i=self.site_box.findText(str(int(sf[0]['segment_no'])))
            if i!=-1:
                self.site_box.setCurrentIndex(i)



#returns list of features with form in folder.
#needs folder to be set
    def surveyed_features(self):
        field='segment_no'
        return [f for f in self.layer_box.currentLayer().getFeatures() if os.path.exists(self.make_save_path(f[field]))]



#returns list of features without form in folder.
#needs folder to be set
    def unsurveyed_features(self):
        field='segment_no'
        return [f for f in self.layer_box.currentLayer().getFeatures() if not os.path.exists(self.make_save_path(f[field]))]




    def clear(self):
        #self.load_dict({k:self.key[k]['default'] for k in self.key})
        d={k:self.key[k]['default'] for k in self.key}
        f=self.segment_no_to_feat()

        d['site']=int(f['segment_no'])
        d['section']=f['sec_label']
        d['start_ch']=f['st_ch']
        d['end_ch']=f['end_ch']
        d['section_length']=f['sec_len']
        d['assesment_length']=f['assess_len']
        d['survey_date']=QDate.currentDate().toString(widget_value.DATE_FORMAT)
        self.load_dict(d)



    def load_csv_old(self,csv_file,sep=','):
        with open(csv_file,'r') as f:
            reader=csv.DictReader(f,fieldnames=['att','val'],dialect='excel',delimiter=sep)
            d={row['att']:row['val'] for row in reader}
            self.load_dict(d)


            
#load csv. loads last row with site=segment_no
    def load_csv(self,csv_file,segment_no,sep=','):
        with open(csv_file,'r') as f:
            reader=csv.DictReader(f,dialect='excel',delimiter=sep)
            #d={row['att']:row['val'] for row in reader}
            for row in reader:
                if int(row['site'])==int(segment_no):
                    self.load_dict(row)  

                
    #load dict of attribute:val
    def load_dict(self,d):
        for k,v in self.key.items():
            widget_value.set_value(v['widget'],d[k],add=True)
            
            
    
    def to_csv_old(self,csv_file,sep=','):
        lines=['%s%s"%s"'%(k,sep,v) for k,v in self.to_dict().items()]#quote charactor around user given values-may contain ','

        with open(csv_file,'w') as f:
           # f.write('attribute%svalue\n'%(sep))#header
            f.write('\n'.join(lines))


#save to csv
    def to_csv(self,csv_file,sep=','):

        if os.path.exists(csv_file):

        #remove existing row for site.
            with open(csv_file,'r') as f:
                reader=csv.DictReader(f,dialect='excel',delimiter=sep)
                dicts=[row for row in reader if int(row['site'])!=int(self.get_site())]
                            
            with open(csv_file,'w') as f:
                w=csv.DictWriter(f,fieldnames=self.key.keys(),dialect='excel',delimiter=sep,lineterminator='\n')
                w.writeheader()
                [w.writerow(d)for d in dicts]
                w.writerow(self.to_dict())

        else:        
            with open(csv_file,'w') as f:
                w=csv.DictWriter(f,fieldnames=self.key.keys(),dialect='excel',delimiter=sep,lineterminator='\n')
                w.writeheader()
                w.writerow(self.to_dict())


    def segment_no(self):
        return self.site

        
    def segment_no_to_feat(self,segment_no=None):
        if not segment_no:
            segment_no=self.segment_no()
            
        field='segment_no'
        e='"%s"=%d'%(field,int(segment_no))
        request = QgsFeatureRequest().setFilterExpression(e)
        feats=[f for f in self.layer_box.currentLayer().getFeatures(request)]

        if len(feats)>1:
            raise KeyError('more than 1 feature with segment_no of '+str(segment_no))
        if len(feats)==0:
            raise KeyError('no features with segment_no of '+str(segment_no))

        return feats[0]
        

    def zoom(self):  
        self.layer_box.currentLayer().selectByIds([self.segment_no_to_feat().id()])#select segment
        layer_functions.zoom_to_selected(self.layer_box.currentLayer())



req_fields={'segment_no':{'types':['int','float']},'sec_label':{'types':['text']},'st_ch':{'types':['int','float']},
            'end_ch':{'types':['int','float']},'sec_len':{'types':['int','float']},'assess_len':{'types':['int','float']},'csv':{'types':['text']}}

        #d['site']=int(f['segment_no'])
        #d['section']=f['sec_label']
        #d['start_ch']=f['st_ch']
        #d['end_ch']=f['end_ch']
        #d['section_length']=f['sec_len']
        #d['assesment_length']=f['assess_len']


def layer_valid(layer):

    if isinstance(layer,QgsRasterLayer):
        return False

    for f in req_fields:
        if layer.fields().indexOf(f)==-1:
            return False           
    return True
    

def str_to_int(s):
    try:
        return int(s)
    except:
        return
