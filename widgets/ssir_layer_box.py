
from qgis.gui import QgsMapLayerComboBox
from qgis.core import QgsProject,QgsVectorLayer


class ssirLayerBox(QgsMapLayerComboBox):

    def __init__(self,parent=None):
        super().__init__(parent)
        QgsProject.instance().layersAdded.connect(self.filter)
        QgsProject.instance().writeMapLayer.connect(self.filter)#changes to map layer saved.
        self.filter()


    #happens when cursor over widget box
    def enterEvent(self,event):
        self.filter()
        super().enterEvent(event)
        
        
    def filter(self):
        self.setExceptedLayerList([layer for layer in QgsProject.instance().mapLayers().values() if not layerValid(layer)])
        #QgsMapLayerRegistry.instance().mapLayers().values() for qgis2
        
        
reqFields = {'site':{'types':['int','float','text']},'csv':{'types':['text']}}

def layerValid(layer):

    if isinstance(layer,QgsVectorLayer):
        for f in reqFields:
            if layer.fields().indexOf(f)==-1:
                return False
        return True
    
    return False

def test():
    b = ssirLayerBox()
    b.show()