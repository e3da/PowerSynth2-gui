# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thermalSetup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 500)
        Dialog.setMinimumSize(QSize(350, 400))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.thermal_setup_2 = QFrame(Dialog)
        self.thermal_setup_2.setObjectName(u"thermal_setup_2")
        self.thermal_setup_2.setFrameShape(QFrame.StyledPanel)
        self.thermal_setup_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.thermal_setup_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_26 = QLabel(self.thermal_setup_2)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_18.addWidget(self.label_26)

        self.lineedit_measure_name = QLineEdit(self.thermal_setup_2)
        self.lineedit_measure_name.setObjectName(u"lineedit_measure_name")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineedit_measure_name.sizePolicy().hasHeightForWidth())
        self.lineedit_measure_name.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.lineedit_measure_name)


        self.gridLayout.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.label_24 = QLabel(self.thermal_setup_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_27 = QLabel(self.thermal_setup_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_19.addWidget(self.label_27)

        self.heat_convection = QLineEdit(self.thermal_setup_2)
        self.heat_convection.setObjectName(u"heat_convection")
        sizePolicy.setHeightForWidth(self.heat_convection.sizePolicy().hasHeightForWidth())
        self.heat_convection.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.heat_convection)


        self.gridLayout.addLayout(self.horizontalLayout_19, 5, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_28 = QLabel(self.thermal_setup_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_20.addWidget(self.label_28)

        self.ambient_temperature = QSpinBox(self.thermal_setup_2)
        self.ambient_temperature.setObjectName(u"ambient_temperature")
        sizePolicy.setHeightForWidth(self.ambient_temperature.sizePolicy().hasHeightForWidth())
        self.ambient_temperature.setSizePolicy(sizePolicy)
        self.ambient_temperature.setMinimumSize(QSize(15, 0))
        self.ambient_temperature.setMaximumSize(QSize(70, 16777215))
        self.ambient_temperature.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ambient_temperature.setMaximum(100000)

        self.horizontalLayout_20.addWidget(self.ambient_temperature)


        self.gridLayout.addLayout(self.horizontalLayout_20, 6, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.thermal_setup_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add_device = QPushButton(self.thermal_setup_2)
        self.btn_add_device.setObjectName(u"btn_add_device")
        sizePolicy.setHeightForWidth(self.btn_add_device.sizePolicy().hasHeightForWidth())
        self.btn_add_device.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btn_add_device)

        self.btn_add_all = QPushButton(self.thermal_setup_2)
        self.btn_add_all.setObjectName(u"btn_add_all")
        sizePolicy.setHeightForWidth(self.btn_add_all.sizePolicy().hasHeightForWidth())
        self.btn_add_all.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btn_add_all)

        self.btn_remove_device = QPushButton(self.thermal_setup_2)
        self.btn_remove_device.setObjectName(u"btn_remove_device")
        sizePolicy.setHeightForWidth(self.btn_remove_device.sizePolicy().hasHeightForWidth())
        self.btn_remove_device.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btn_remove_device)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.thermal_setup_2)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_17.addWidget(self.label_25)

        self.combo_model_select = QComboBox(self.thermal_setup_2)
        self.combo_model_select.addItem("")
        self.combo_model_select.addItem("")
        self.combo_model_select.addItem("")
        self.combo_model_select.addItem("")
        self.combo_model_select.setObjectName(u"combo_model_select")
        sizePolicy.setHeightForWidth(self.combo_model_select.sizePolicy().hasHeightForWidth())
        self.combo_model_select.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.combo_model_select)


        self.gridLayout.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.thermal_setup_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_continue = QPushButton(Dialog)
        self.btn_continue.setObjectName(u"btn_continue")
        sizePolicy.setHeightForWidth(self.btn_continue.sizePolicy().hasHeightForWidth())
        self.btn_continue.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_continue)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        self.btn_continue.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Thermal Setup", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Measure Name", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Thermal Setup</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Heat Convection (W/(m<span style=\" vertical-align:super;\">2</span>\u00b7K))</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Ambient Temperature (K)", None))
        self.ambient_temperature.setSpecialValueText(QCoreApplication.translate("Dialog", u"300", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Device", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Power", None));
        self.btn_add_device.setText(QCoreApplication.translate("Dialog", u"Add Device", None))
        self.btn_add_all.setText(QCoreApplication.translate("Dialog", u"Add All", None))
        self.btn_remove_device.setText(QCoreApplication.translate("Dialog", u"Remove Device", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Thermal Model", None))
        self.combo_model_select.setItemText(0, QCoreApplication.translate("Dialog", u"ParaPower", None))
        self.combo_model_select.setItemText(1, QCoreApplication.translate("Dialog", u"TSFM", None))
        self.combo_model_select.setItemText(2, QCoreApplication.translate("Dialog", u"Analytical", None))
        self.combo_model_select.setItemText(3, "")

        self.btn_continue.setText(QCoreApplication.translate("Dialog", u"Continue", None))
    # retranslateUi

