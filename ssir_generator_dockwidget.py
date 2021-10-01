# -*- coding: utf-8 -*-
"""
read and write rows of csv.

1 csv to many features.
different features can have different csv

csv linked to feature through csv attribute of feature
feature linked to segment_number

1 site : 1 feature : row of csv

replace with QDataWidgetMapper and model?
model with only 1 row

ability to save to 1 or to many csvs
"""

import os

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QDate,QUrl,Qt

from PyQt5.QtWidgets import QComboBox,QLineEdit,QCompleter,QMenu
from qgis.PyQt.QtWidgets import QFileDialog

from . import widget_value,layer_functions,file_dialogs

from qgis.utils import iface

import csv
import collections
from qgis.core import QgsFeatureRequest,QgsProject,QgsMapLayerProxyModel,QgsRasterLayer


from . ssir_generator_dockwidget_base import Ui_ssir_generatorDockWidgetBase


class ssirGeneratorDockWidget(QtWidgets.QDockWidget, Ui_ssir_generatorDockWidgetBase):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        super(ssirGeneratorDockWidget, self).__init__(parent)

        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.clear_button.clicked.connect(self.clear)
        
        self.initKey()
        self.help_button.clicked.connect(self.openHelp)


#WritableLayer,VectorLayer,PointLayer
        self.layer_box.setFilters(QgsMapLayerProxyModel.VectorLayer|QgsMapLayerProxyModel.PointLayer)
        self.filterLayers()
        QgsProject.instance().layersAdded.connect(self.filterLayers)
        
        
        #special handling for comboboxes
        for k,v in self.key.items():
            if isinstance(v['widget'],QComboBox):
                v['widget'].setLineEdit(QLineEdit())
                if 'items' in v:
                    v['widget'].clear()
                    v['widget'].addItems(v['items'])

                        
        self.rules = (('Surveyed', 'not "csv" is null', 'green', None),('Unsurveyed', '"csv" is null', 'red', None))#rules for symbology
        self.split_button.clicked.connect(lambda:layer_functions.set_rules(self.layer_box.currentLayer(),self.rules))#change symbology
        self.layer_box.layerChanged.connect(self.layerChanged)

        self.layerChanged(self.layer_box.currentLayer())

        self.siteBox.currentIndexChanged.connect(self.siteBoxChanged)
        
        self.next_site_button.clicked.connect(self.nextSite)
        self.last_site_button.clicked.connect(self.lastSite)


        siteMenu = QMenu(self)
        zoomAct = siteMenu.addAction('Zoom to site')
        zoomAct.triggered.connect(self.zoom)
        
        fromSelectedAct = siteMenu.addAction('Change to selected feature')
        fromSelectedAct.triggered.connect(self.fromSelected)
        
        self.siteBox.setContextMenuPolicy(Qt.CustomContextMenu);
        self.siteBox.customContextMenuRequested.connect(lambda pt:siteMenu.exec_(self.mapToGlobal(pt)))
        

        
    def filterLayers(self):
        self.layer_box.setExceptedLayerList([layer for layer in QgsProject.instance().mapLayers().values() if not layerValid(layer)])   #QgsMapLayerRegistry.instance().mapLayers().values() for qgis2



  #create ordered dict self.key to link name of attribute to widget and default value
    def initKey(self):
        #site details
        self.key=collections.OrderedDict()
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
    


    def layerChanged(self,layer):

        if not layer:
            iface.messageBar().pushMessage('ssir generator:no layer')
            return
            
        field='segment_no'
        if layerValid(layer):
            self.siteBox.clear()
            s = self.segments()
            self.siteBox.addItems(s)
            self.siteBox.setCompleter(QCompleter(s))
            #self.siteBox.setCurrentIndex(self.siteBox.currentIndex())#value in site_box might not change. site_box_changed might be called twice

        else:
            iface.messageBar().pushMessage('ssir generator:layer needs fields segment_no and csv')


    def save(self):
        p = file_dialogs.save_file_dialog(ext='.csv',caption='save as csv',default_name=str(self.site()),options=QFileDialog.DontConfirmOverwrite)
        
        if p:

            self.toCsv(p)
            iface.messageBar().pushMessage('ssir generator:saved to '+p)

            #setting 'csv' field of feature
            self.layer_box.currentLayer()
            self.layer_box.currentLayer().startEditing()
            self.layer_box.currentLayer().changeAttributeValue(self.feature().id(), self.layer_box.currentLayer().fields().indexOf('csv'),p)
            self.layer_box.currentLayer().commitChanges()



    def nextSite(self):
        self.siteBox.setCurrentIndex(min(self.siteBox.count(),self.siteBox.currentIndex()+1))
    

    def lastSite(self):
        self.siteBox.setCurrentIndex(max(0,self.siteBox.currentIndex()-1))


#str new_site
    def siteBoxChanged(self,index):
        if self.siteBox.itemText(index):
            
            f = str(self.feature()['csv'])
                
            if os.path.exists(f):
                self.loadCsv(f)
            else:
                self.clear()
                    

    def segments(self):
        layer = self.layer_box.currentLayer()
        if layer:
            vals = sorted(layer.uniqueValues(layer.fields().indexOf('segment_no')))
            return [str(v) for v in vals]

#attributes to dict
    def toDict(self):
        d = {k:widget_value.get_value(v['widget']) for k,v in self.key.items()}
        d['site'] = self.site()
        return d


#opens help/index.html in default browser
    def openHelp(self):
        help_path=os.path.join(os.path.dirname(__file__),'help','index.html')
        help_path='file:///'+os.path.abspath(help_path)
        QtGui.QDesktopServices.openUrl(QUrl(help_path))

        

    def fromSelected(self):
        sf=self.layer_box.currentLayer().selectedFeatures()

        if len(sf)==0:
            iface.messageBar().pushMessage('ssir generator: no features selected')

        if len(sf)>1:
            iface.messageBar().pushMessage('ssir generator: more than 1 feature selected')

        if len(sf)==1:
            i=self.siteBox.findText(str(int(sf[0]['site'])))
            if i!=-1:
                self.siteBox.setCurrentIndex(i)



#returns list of features with form in folder. unused
#needs folder to be set
    def surveyedFeatures(self):
        field='segment_no'
        return [f for f in self.layer_box.currentLayer().getFeatures() if os.path.exists(self.make_save_path(f[field]))]



#returns list of features without form in folder. unused
#needs folder to be set
    def unsurveyedFeatures(self):
        field='segment_no'
        return [f for f in self.layer_box.currentLayer().getFeatures() if not os.path.exists(self.make_save_path(f[field]))]


    def clear(self):
        d = {k:self.key[k]['default'] for k in self.key}
        self.loadDict(d)

            
#load csv. loads last row with site=segment_no
    def loadCsv(self,csv_file,sep=','):
        s = self.site()
        
        with open(csv_file,'r') as f:
            reader=csv.DictReader(f,dialect='excel',delimiter=sep)
            for row in reader:
                if row['site']==s:
                    self.loadDict(row)

                
    #load dict of attribute:val
    def loadDict(self,d):
        for k,v in self.key.items():
            widget_value.set_value(v['widget'],d[k],add=True)
            
            

#save form to csv, replacing any existing row for site.
    def toCsv(self,csv_file,sep=','):

        if os.path.exists(csv_file):

        #remove existing row for site.
            with open(csv_file,'r') as f:
                reader=csv.DictReader(f,dialect='excel',delimiter=sep)
                dicts = [row for row in reader if row['site']!=self.site()]
                            
            with open(csv_file,'w') as f:
                w=csv.DictWriter(f,fieldnames=list(self.key.keys())+['site'],dialect='excel',delimiter=sep,lineterminator='\n')
                w.writeheader()
                [w.writerow(d) for d in dicts]
                w.writerow(self.toDict())

        else:        
            with open(csv_file,'w') as f:
                w=csv.DictWriter(f,fieldnames=list(self.key.keys())+['site'],dialect='excel',delimiter=sep,lineterminator='\n')
                w.writeheader()
                w.writerow(self.toDict())


    #str
    def site(self):
        return self.siteBox.itemText(self.siteBox.currentIndex())


    def feature(self):
            
        e='"segment_no"=%s'%(self.site())
        request = QgsFeatureRequest().setFilterExpression(e)
        feats = [f for f in self.layer_box.currentLayer().getFeatures(request)]

        if len(feats)>1:
            raise KeyError('more than 1 feature with segment_no of '+self.site())
        if len(feats)==0:
            raise KeyError('no features with segment_no of '+self.site())

        return feats[0]
        

    def zoom(self):  
        self.layer_box.currentLayer().selectByIds([self.feature().id()])#select segment
        layer_functions.zoom_to_selected(self.layer_box.currentLayer())



reqFields = {'site':{'types':['int','float','text']},'csv':{'types':['text']}}

def layerValid(layer):

    if isinstance(layer,QgsRasterLayer):
        return False

    for f in reqFields:
        if layer.fields().indexOf(f)==-1:
            return False           
    return True
    
