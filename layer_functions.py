
from qgis.utils import iface
from qgis.core import QgsRuleBasedRenderer,QgsSymbol

from PyQt5.QtGui import QColor


def colour_features(feats,layer,colour):
    sf=layer.selectedFeatures()
    layer.selectByIds([f.id() for f in feats])
    iface.mapCanvas().setSelectionColor(colour)
    layer.selectByIds([f.id() for f in sf])



#rules = (
  #  ('Surveyed', 'not "csv" is null', 'green', None),
 #   ('Unsureyed', 'not "csv" is null', 'red', None)
#)

def set_rules(layer,rules):

    # create a new rule-based renderer
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    renderer = QgsRuleBasedRenderer(symbol)

    # get the "root" rule
    root_rule = renderer.rootRule()

    for label, expression, color_name, scale in rules:
        # create a clone (i.e. a copy) of the default rule
        rule = root_rule.children()[0].clone()
        # set the label, expression and color
        rule.setLabel(label)
        rule.setFilterExpression(expression)
        rule.symbol().setColor(QColor(color_name))
        # set the scale limits if they have been specified
        if scale is not None:
            rule.setScaleMinDenom(scale[0])
            rule.setScaleMaxDenom(scale[1])
        # append the rule to the list of rules
        root_rule.appendChild(rule)

    # delete the default rule
    root_rule.removeChildAt(0)

    # apply the renderer to the layer
    layer.setRenderer(renderer)


#returns sorted list of distinct values
def distinct_values(layer,field):
    vals=[f[field] for f in layer.getFeatures()]#all values
    vals=list(set(vals))#unique values
    vals.sort()
    return vals


#zoom to selected features of layer. Works with any crs
def zoom_to_selected(layer):
    a=iface.activeLayer()
    iface.setActiveLayer(layer)
    iface.actionZoomToSelected().trigger()
    iface.setActiveLayer(a)
    #iface.mapCanvas().setExtent(layer.boundingBoxOfSelected())
    #iface.mapCanvas().refresh()
