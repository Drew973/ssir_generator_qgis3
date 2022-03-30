if __name__=='__console__':
    import sys
    p = r'C:\Users\drew.bennett\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\manytoonemapper\widgets'
    sys.path.append(p)
    import searchableComboBox
    
else:
    from . import searchableComboBox



from qgis.core import QgsFeatureRequest
from qgis.utils import iface
#from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import QSortFilterProxyModel
'''
'''

from PyQt5.QtGui import QStandardItemModel



class featureWidget(searchableComboBox.searchableComboBox):
#
  #  featuresChanged = pyqtSignal()
    
    def __init__(self,parent=None):
        super().__init__(parent)
     
        self.layer = None
        self.field = None
    
    
    #string,QgsVectorLayer
       
    def setField(self,field,layer):
        self.layer = layer
    
        if layer is None:
            self.clear()
        
        else:
            filt = layer.subsetString()
            layer.setSubsetString('')#remove filter.

            self.layerModel = QStandardItemModel(layer.featureCount(),1,self)#row = fid
            
            if layer.fields().indexOf(field)!=-1:           #currentField='' when QGSFIeldComboBox layer not set?
                for f in layer.getFeatures():
                    self.layerModel.setData(self.layerModel.index(f.id(),0),f[field])
            
            else:
                for f in layer.getFeatures():
                    self.layerModel.setData(self.layerModel.index(f.id(),0),f.id())
                  
           # self.setModel(model)
            m = QSortFilterProxyModel(self)
            m.setSourceModel(self.layerModel)
            m.sort(0)
            self.setModel(m)
            layer.setSubsetString(filt)#add filter.

    
    def next(self):
        #count starts from 1. index starts from 0
        if self.currentIndex()<self.count()-1:
            self.setCurrentIndex(self.currentIndex()+1)
        
        
    def last(self):
        if self.currentIndex()>0:
            self.setCurrentIndex(self.currentIndex()-1)
       

    def fromLayer(self):
        ids = [f.id() for f in self.layer.selectedFeatures()]
        if len(ids)>0:
            self.setCurrentIndex(self.fidToRow(min(ids)))
            return True,'no error'
        else:
            return False,'No features selected'


    #fid to row of combobox
    def fidToRow(self,fid):
        if not self.layer is None:
            i = self.layerModel.index(fid,0)
            return self.model().mapFromSource(i).row()      

            
    #row of combobox to fid
    def rowToFid(self,row):
        if not self.layer is None:
            i = self.model().index(row,0)
            return self.model().mapToSource(i).row()           
    
    
    def currentFid(self):
        return self.rowToFid(self.currentIndex())


def singleQuote(s):
    return "'%s'"%(s)


def doubleQuote(s):
    return '"%s"'%(s)

    
def zoomToSelected(layer):
    a = iface.activeLayer()
    iface.setActiveLayer(layer)
    iface.actionZoomToSelected().trigger()
    iface.setActiveLayer(a)
    

def filterString(field,value):
    return '%s=%s '%(doubleQuote(field),singleQuote(value))
    
    

if __name__ =='__console__':
    layer = QgsProject.instance().mapLayersByName('stats19')[0]
    field = 'gid'
    w = featureWidget()
    w.setField(field,layer)
    w.show()
