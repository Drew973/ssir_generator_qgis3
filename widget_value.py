
DATE_FORMAT='dd_MM_yyyy'


from PyQt5.QtWidgets import QTextEdit,QDateEdit,QSpinBox,QDoubleSpinBox,QLineEdit,QComboBox,QLabel
from PyQt5.QtCore import QDate


#w=widget
def get_value(w):
    if isinstance(w,QTextEdit):
        return w.toPlainText()

    if isinstance(w,QLineEdit):
        return w.text()

    if isinstance(w,QSpinBox):
        return w.value()

    if isinstance(w,QDoubleSpinBox):
        return w.value()

    if isinstance(w,QDateEdit):
        return w.date().toString(DATE_FORMAT)


    if isinstance(w,QComboBox):
        return w.currentText()

    if isinstance(w,QLabel):
        return w.text()
    

    

#w=widget
def set_value(w,v,add=False):
    if isinstance(w,QTextEdit):
        w.setPlainText(str(v))
        return True

    if isinstance(w,QLineEdit):
        w.setText(str(v))

    if isinstance(w,QSpinBox):
        w.setValue(int(v))

    if isinstance(w,QDoubleSpinBox):
        w.setValue(float(v))

    if isinstance(w,QDateEdit):
        w.setDate(QDate.fromString(v,DATE_FORMAT))

    if isinstance(w,QComboBox):
        i=w.findText(v)

        if add and not i>=0:
            w.addItem(v)
            i=w.findText(v)
        
        if i>=0:
            w.setCurrentIndex(i)
        
                
        
    if isinstance(w,QLabel):
        return w.setText(str(v))
