# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssir_generator_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ssir_generatorDockWidgetBase(object):
    def setupUi(self, ssir_generatorDockWidgetBase):
        ssir_generatorDockWidgetBase.setObjectName("ssir_generatorDockWidgetBase")
        ssir_generatorDockWidgetBase.resize(570, 621)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_28 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_4.addWidget(self.label_28)
        self.layer_box = ssirLayerBox(self.dockWidgetContents)
        self.layer_box.setObjectName("layer_box")
        self.horizontalLayout_4.addWidget(self.layer_box)
        self.split_button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.split_button.setObjectName("split_button")
        self.horizontalLayout_4.addWidget(self.split_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.lastButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.lastButton.setObjectName("lastButton")
        self.horizontalLayout.addWidget(self.lastButton)
        self.siteBox = featureWidget(self.dockWidgetContents)
        self.siteBox.setObjectName("siteBox")
        self.horizontalLayout.addWidget(self.siteBox)
        self.nextButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName("toolBox")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 546, 265))
        self.page_5.setObjectName("page_5")
        self.formLayout_6 = QtWidgets.QFormLayout(self.page_5)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_2 = QtWidgets.QLabel(self.page_5)
        self.label_2.setObjectName("label_2")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.section = QtWidgets.QLineEdit(self.page_5)
        self.section.setObjectName("section")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.section)
        self.label_3 = QtWidgets.QLabel(self.page_5)
        self.label_3.setObjectName("label_3")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.start_ch = QtWidgets.QDoubleSpinBox(self.page_5)
        self.start_ch.setMaximum(99999.0)
        self.start_ch.setObjectName("start_ch")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.start_ch)
        self.label_4 = QtWidgets.QLabel(self.page_5)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.end_ch = QtWidgets.QDoubleSpinBox(self.page_5)
        self.end_ch.setMaximum(99999.0)
        self.end_ch.setObjectName("end_ch")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.end_ch)
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setObjectName("label_5")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.section_length = QtWidgets.QDoubleSpinBox(self.page_5)
        self.section_length.setMaximum(99999.0)
        self.section_length.setObjectName("section_length")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.section_length)
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.assesment_length = QtWidgets.QDoubleSpinBox(self.page_5)
        self.assesment_length.setMaximum(99999.0)
        self.assesment_length.setObjectName("assesment_length")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.assesment_length)
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 219, 139))
        self.page_6.setObjectName("page_6")
        self.formLayout = QtWidgets.QFormLayout(self.page_6)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.page_6)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.surveyor = QtWidgets.QLineEdit(self.page_6)
        self.surveyor.setObjectName("surveyor")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.surveyor)
        self.survey_date_label = QtWidgets.QLabel(self.page_6)
        self.survey_date_label.setObjectName("survey_date_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.survey_date_label)
        self.survey_date = QtWidgets.QDateEdit(self.page_6)
        self.survey_date.setCalendarPopup(True)
        self.survey_date.setObjectName("survey_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.survey_date)
        self.photo_ref_label = QtWidgets.QLabel(self.page_6)
        self.photo_ref_label.setObjectName("photo_ref_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.photo_ref_label)
        self.photo_ref = QtWidgets.QLineEdit(self.page_6)
        self.photo_ref.setObjectName("photo_ref")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.photo_ref)
        self.label_8 = QtWidgets.QLabel(self.page_6)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.additional_photos = QtWidgets.QLineEdit(self.page_6)
        self.additional_photos.setObjectName("additional_photos")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.additional_photos)
        self.toolBox.addItem(self.page_6, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 419, 218))
        self.page.setObjectName("page")
        self.formLayout_2 = QtWidgets.QFormLayout(self.page)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.surface_type = QtWidgets.QComboBox(self.page)
        self.surface_type.setEditable(True)
        self.surface_type.setObjectName("surface_type")
        self.surface_type.addItem("")
        self.surface_type.addItem("")
        self.surface_type.addItem("")
        self.surface_type.addItem("")
        self.surface_type.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.surface_type)
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.aggregate_size = QtWidgets.QComboBox(self.page)
        self.aggregate_size.setEditable(True)
        self.aggregate_size.setObjectName("aggregate_size")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.aggregate_size)
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.aggregate_condition = QtWidgets.QComboBox(self.page)
        self.aggregate_condition.setEditable(True)
        self.aggregate_condition.setObjectName("aggregate_condition")
        self.aggregate_condition.addItem("")
        self.aggregate_condition.addItem("")
        self.aggregate_condition.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.aggregate_condition)
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.inconsistencies = QtWidgets.QComboBox(self.page)
        self.inconsistencies.setEditable(True)
        self.inconsistencies.setObjectName("inconsistencies")
        self.inconsistencies.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inconsistencies)
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.contaminants = QtWidgets.QComboBox(self.page)
        self.contaminants.setEditable(True)
        self.contaminants.setObjectName("contaminants")
        self.contaminants.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.contaminants)
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.local_defects = QtWidgets.QComboBox(self.page)
        self.local_defects.setEditable(True)
        self.local_defects.setObjectName("local_defects")
        self.local_defects.addItem("")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.local_defects)
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.drainage_adequate = QtWidgets.QComboBox(self.page)
        self.drainage_adequate.setEditable(True)
        self.drainage_adequate.setObjectName("drainage_adequate")
        self.drainage_adequate.addItem("")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.drainage_adequate)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 384, 102))
        self.page_2.setObjectName("page_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.page_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.meets_design_specification = QtWidgets.QComboBox(self.page_2)
        self.meets_design_specification.setEditable(True)
        self.meets_design_specification.setObjectName("meets_design_specification")
        self.meets_design_specification.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.meets_design_specification)
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.appropriate_for_vunerable_users = QtWidgets.QComboBox(self.page_2)
        self.appropriate_for_vunerable_users.setEditable(True)
        self.appropriate_for_vunerable_users.setObjectName("appropriate_for_vunerable_users")
        self.appropriate_for_vunerable_users.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.appropriate_for_vunerable_users)
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.appropriate_for_turning = QtWidgets.QComboBox(self.page_2)
        self.appropriate_for_turning.setEditable(True)
        self.appropriate_for_turning.setObjectName("appropriate_for_turning")
        self.appropriate_for_turning.addItem("")
        self.appropriate_for_turning.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.appropriate_for_turning)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 415, 131))
        self.page_3.setObjectName("page_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.page_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_20 = QtWidgets.QLabel(self.page_3)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.markings_clear = QtWidgets.QComboBox(self.page_3)
        self.markings_clear.setEditable(True)
        self.markings_clear.setObjectName("markings_clear")
        self.markings_clear.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.markings_clear)
        self.label_21 = QtWidgets.QLabel(self.page_3)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.roadside_objects = QtWidgets.QComboBox(self.page_3)
        self.roadside_objects.setEditable(True)
        self.roadside_objects.setObjectName("roadside_objects")
        self.roadside_objects.addItem("")
        self.roadside_objects.addItem("")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roadside_objects)
        self.label_22 = QtWidgets.QLabel(self.page_3)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.clear_sight_lines = QtWidgets.QComboBox(self.page_3)
        self.clear_sight_lines.setEditable(True)
        self.clear_sight_lines.setObjectName("clear_sight_lines")
        self.clear_sight_lines.addItem("")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clear_sight_lines)
        self.label_23 = QtWidgets.QLabel(self.page_3)
        self.label_23.setObjectName("label_23")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.additional_comments = QtWidgets.QComboBox(self.page_3)
        self.additional_comments.setEditable(True)
        self.additional_comments.setObjectName("additional_comments")
        self.additional_comments.addItem("")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.additional_comments)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 468, 131))
        self.page_4.setObjectName("page_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.page_4)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_24 = QtWidgets.QLabel(self.page_4)
        self.label_24.setObjectName("label_24")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.treatment_req = QtWidgets.QComboBox(self.page_4)
        self.treatment_req.setEditable(True)
        self.treatment_req.setObjectName("treatment_req")
        self.treatment_req.addItem("")
        self.treatment_req.addItem("")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.treatment_req)
        self.label_25 = QtWidgets.QLabel(self.page_4)
        self.label_25.setObjectName("label_25")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.treatment_type = QtWidgets.QComboBox(self.page_4)
        self.treatment_type.setEditable(True)
        self.treatment_type.setObjectName("treatment_type")
        self.treatment_type.addItem("")
        self.treatment_type.addItem("")
        self.treatment_type.addItem("")
        self.treatment_type.addItem("")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.treatment_type)
        self.label_26 = QtWidgets.QLabel(self.page_4)
        self.label_26.setObjectName("label_26")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.change_il = QtWidgets.QComboBox(self.page_4)
        self.change_il.setEditable(True)
        self.change_il.setObjectName("change_il")
        self.change_il.addItem("")
        self.change_il.addItem("")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.change_il)
        self.label_27 = QtWidgets.QLabel(self.page_4)
        self.label_27.setObjectName("label_27")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.other_action_req = QtWidgets.QComboBox(self.page_4)
        self.other_action_req.setEditable(True)
        self.other_action_req.setObjectName("other_action_req")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.other_action_req.addItem("")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.other_action_req)
        self.toolBox.addItem(self.page_4, "")
        self.horizontalLayout_2.addWidget(self.toolBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.save_button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_3.addWidget(self.save_button)
        self.clear_button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_3.addWidget(self.clear_button)
        self.help_button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.help_button.setObjectName("help_button")
        self.horizontalLayout_3.addWidget(self.help_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        ssir_generatorDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(ssir_generatorDockWidgetBase)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ssir_generatorDockWidgetBase)

    def retranslateUi(self, ssir_generatorDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        ssir_generatorDockWidgetBase.setWindowTitle(_translate("ssir_generatorDockWidgetBase", "ssir_generator"))
        self.label_28.setText(_translate("ssir_generatorDockWidgetBase", "Layer"))
        self.layer_box.setToolTip(_translate("ssir_generatorDockWidgetBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Layer with sites. Only shows layers with the necessary fields. These are site(int/float/text) and csv(text).</p></body></html>"))
        self.split_button.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\'; font-size:16px; color:#000000; background-color:transparent;\">Change the layer style to display surveyed and unsurveyed features differently.</span></p></body></html>"))
        self.split_button.setText(_translate("ssir_generatorDockWidgetBase", "Surveyed/Unsurveyed"))
        self.label_9.setText(_translate("ssir_generatorDockWidgetBase", "Site"))
        self.lastButton.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Go to previous site. WILL LOSE ANY UNSAVED CHANGES TO FORM.</p></body></html>"))
        self.lastButton.setText(_translate("ssir_generatorDockWidgetBase", "<"))
        self.siteBox.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Current site. <span style=\" font-weight:600;\">CHANGING THIS WILL LOSE ANY UNSAVED CHANGES TO FORM</span>. Right click for more options.</p></body></html>"))
        self.nextButton.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Go to next site. WILL LOSE ANY UNSAVED CHANGES TO FORM.</p></body></html>"))
        self.nextButton.setText(_translate("ssir_generatorDockWidgetBase", ">"))
        self.label_2.setText(_translate("ssir_generatorDockWidgetBase", "Section"))
        self.label_3.setText(_translate("ssir_generatorDockWidgetBase", "Start Ch"))
        self.label_4.setText(_translate("ssir_generatorDockWidgetBase", "End Ch"))
        self.label_5.setText(_translate("ssir_generatorDockWidgetBase", "Section Length"))
        self.label_6.setText(_translate("ssir_generatorDockWidgetBase", "Assesment length"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("ssir_generatorDockWidgetBase", "Site Details"))
        self.label_7.setText(_translate("ssir_generatorDockWidgetBase", "Surveyor"))
        self.survey_date_label.setText(_translate("ssir_generatorDockWidgetBase", "Survey_date"))
        self.survey_date.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>dd/mm/yyyy</p></body></html>"))
        self.photo_ref_label.setText(_translate("ssir_generatorDockWidgetBase", "Photo ref"))
        self.label_8.setText(_translate("ssir_generatorDockWidgetBase", "Additional photos"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("ssir_generatorDockWidgetBase", "Survey Details"))
        self.label_10.setText(_translate("ssir_generatorDockWidgetBase", "Surface Type"))
        self.surface_type.setItemText(0, _translate("ssir_generatorDockWidgetBase", "TSSC"))
        self.surface_type.setItemText(1, _translate("ssir_generatorDockWidgetBase", "HRA"))
        self.surface_type.setItemText(2, _translate("ssir_generatorDockWidgetBase", "SURFACE DRESSING"))
        self.surface_type.setItemText(3, _translate("ssir_generatorDockWidgetBase", "SLURRY SEAL"))
        self.surface_type.setItemText(4, _translate("ssir_generatorDockWidgetBase", "MICRO ASPHALT"))
        self.label_11.setText(_translate("ssir_generatorDockWidgetBase", "Aggregate Size"))
        self.label_12.setText(_translate("ssir_generatorDockWidgetBase", "Aggregate Condition"))
        self.aggregate_condition.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Good"))
        self.aggregate_condition.setItemText(1, _translate("ssir_generatorDockWidgetBase", "Average"))
        self.aggregate_condition.setItemText(2, _translate("ssir_generatorDockWidgetBase", "Poor"))
        self.label_13.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Any inconsistencies with data</p></body></html>"))
        self.inconsistencies.setItemText(0, _translate("ssir_generatorDockWidgetBase", "No"))
        self.label_14.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Presence of Debris or other Contamination</p></body></html>"))
        self.contaminants.setItemText(0, _translate("ssir_generatorDockWidgetBase", "No"))
        self.label_15.setText(_translate("ssir_generatorDockWidgetBase", "Local defects (potholes,rutting, etc)"))
        self.local_defects.setItemText(0, _translate("ssir_generatorDockWidgetBase", "N/A"))
        self.label_16.setText(_translate("ssir_generatorDockWidgetBase", "Is drainage adequate"))
        self.drainage_adequate.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("ssir_generatorDockWidgetBase", "Visual Assesment"))
        self.label_17.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Does site appear to meet current design specification</p></body></html>"))
        self.meets_design_specification.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.label_18.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Is layout appropriate for vunerable users</p></body></html>"))
        self.appropriate_for_vunerable_users.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.label_19.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Are junctions appropriate for turning manouvers</p></body></html>"))
        self.appropriate_for_turning.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.appropriate_for_turning.setItemText(1, _translate("ssir_generatorDockWidgetBase", "N/A"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("ssir_generatorDockWidgetBase", "Road Layout"))
        self.label_20.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Are markings and signs clear and effective in all conditions</p></body></html>"))
        self.markings_clear.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.label_21.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Are roadside objects protected from vehicle impact</p></body></html>"))
        self.roadside_objects.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.roadside_objects.setItemText(1, _translate("ssir_generatorDockWidgetBase", "Na"))
        self.label_22.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Clear sight lines/visibility of queues/vegetation</p></body></html>"))
        self.clear_sight_lines.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.label_23.setText(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Additional comments and other observations</p></body></html>"))
        self.additional_comments.setItemText(0, _translate("ssir_generatorDockWidgetBase", "N/A"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("ssir_generatorDockWidgetBase", "Markings Signs and Visibility"))
        self.label_24.setText(_translate("ssir_generatorDockWidgetBase", "Is treatment req"))
        self.treatment_req.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.treatment_req.setItemText(1, _translate("ssir_generatorDockWidgetBase", "No"))
        self.label_25.setText(_translate("ssir_generatorDockWidgetBase", "What type of treatment"))
        self.treatment_type.setItemText(0, _translate("ssir_generatorDockWidgetBase", "N/A"))
        self.treatment_type.setItemText(1, _translate("ssir_generatorDockWidgetBase", "Surface condition poor"))
        self.treatment_type.setItemText(2, _translate("ssir_generatorDockWidgetBase", "Surface condition poor + signage/markings poor"))
        self.treatment_type.setItemText(3, _translate("ssir_generatorDockWidgetBase", "Signage/markings poor"))
        self.label_26.setText(_translate("ssir_generatorDockWidgetBase", "Change IL"))
        self.change_il.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Yes"))
        self.change_il.setItemText(1, _translate("ssir_generatorDockWidgetBase", "No"))
        self.label_27.setText(_translate("ssir_generatorDockWidgetBase", "Other action req"))
        self.other_action_req.setItemText(0, _translate("ssir_generatorDockWidgetBase", "Road marking survey"))
        self.other_action_req.setItemText(1, _translate("ssir_generatorDockWidgetBase", "Signage survey"))
        self.other_action_req.setItemText(2, _translate("ssir_generatorDockWidgetBase", "Road marking and signage survey"))
        self.other_action_req.setItemText(3, _translate("ssir_generatorDockWidgetBase", "Vegetation cutting"))
        self.other_action_req.setItemText(4, _translate("ssir_generatorDockWidgetBase", "VRS survey"))
        self.other_action_req.setItemText(5, _translate("ssir_generatorDockWidgetBase", "Adjust speed"))
        self.other_action_req.setItemText(6, _translate("ssir_generatorDockWidgetBase", "Consider protection of vunerable users"))
        self.other_action_req.setItemText(7, _translate("ssir_generatorDockWidgetBase", "Drainage survey"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("ssir_generatorDockWidgetBase", "Recomendation"))
        self.save_button.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Save as csv. Also sets &quot;csv&quot; attribute of corresponding feature.</p></body></html>"))
        self.save_button.setText(_translate("ssir_generatorDockWidgetBase", "Save..."))
        self.clear_button.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Change form to default values.</p></body></html>"))
        self.clear_button.setText(_translate("ssir_generatorDockWidgetBase", "Clear Form"))
        self.help_button.setToolTip(_translate("ssir_generatorDockWidgetBase", "<html><head/><body><p>Open help in default web browser.</p></body></html>"))
        self.help_button.setText(_translate("ssir_generatorDockWidgetBase", "Help"))
from ssir_generator.widgets.feature_widget import featureWidget
from ssir_generator.widgets.ssir_layer_box import ssirLayerBox
