# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'electricalSetupConverter.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 565)
        Dialog.setMinimumSize(QSize(350, 400))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.electrical_setup = QVBoxLayout()
        self.electrical_setup.setObjectName(u"electrical_setup")
        self.electrical_setup.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_24.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.combo_model_type = QComboBox(Dialog)
        self.combo_model_type.addItem("")
        self.combo_model_type.addItem("")
        self.combo_model_type.setObjectName(u"combo_model_type")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_model_type.sizePolicy().hasHeightForWidth())
        self.combo_model_type.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.combo_model_type)


        self.electrical_setup.addLayout(self.horizontalLayout_17)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.electrical_setup.addItem(self.verticalSpacer)

        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")

        self.electrical_setup.addWidget(self.label_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.lineedit_measure_name = QLineEdit(Dialog)
        self.lineedit_measure_name.setObjectName(u"lineedit_measure_name")
        self.lineedit_measure_name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lineedit_measure_name.sizePolicy().hasHeightForWidth())
        self.lineedit_measure_name.setSizePolicy(sizePolicy)
        self.lineedit_measure_name.setReadOnly(False)

        self.horizontalLayout_12.addWidget(self.lineedit_measure_name)


        self.electrical_setup.addLayout(self.horizontalLayout_12)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout.addWidget(self.tableWidget)


        self.electrical_setup.addLayout(self.verticalLayout)

        self.parasitic_model_frame = QFrame(Dialog)
        self.parasitic_model_frame.setObjectName(u"parasitic_model_frame")
        sizePolicy.setHeightForWidth(self.parasitic_model_frame.sizePolicy().hasHeightForWidth())
        self.parasitic_model_frame.setSizePolicy(sizePolicy)
        self.parasitic_model_frame.setMinimumSize(QSize(0, 0))
        self.parasitic_model_frame.setFrameShape(QFrame.StyledPanel)
        self.parasitic_model_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.parasitic_model_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.electrical_setup.addWidget(self.parasitic_model_frame)


        self.verticalLayout_2.addLayout(self.electrical_setup)

        self.thermal_setup_2 = QVBoxLayout()
        self.thermal_setup_2.setObjectName(u"thermal_setup_2")
        self.thermal_setup_2.setContentsMargins(4, 4, 4, 4)
        self.label_30 = QLabel(Dialog)
        self.label_30.setObjectName(u"label_30")

        self.thermal_setup_2.addWidget(self.label_30)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_31 = QLabel(Dialog)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_22.addWidget(self.label_31)

        self.lineedit_measure_name_3 = QLineEdit(Dialog)
        self.lineedit_measure_name_3.setObjectName(u"lineedit_measure_name_3")
        self.lineedit_measure_name_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lineedit_measure_name_3.sizePolicy().hasHeightForWidth())
        self.lineedit_measure_name_3.setSizePolicy(sizePolicy)
        self.lineedit_measure_name_3.setReadOnly(False)

        self.horizontalLayout_22.addWidget(self.lineedit_measure_name_3)


        self.thermal_setup_2.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_32 = QLabel(Dialog)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_23.addWidget(self.label_32)

        self.combo_model_select_2 = QComboBox(Dialog)
        self.combo_model_select_2.addItem("")
        self.combo_model_select_2.addItem("")
        self.combo_model_select_2.addItem("")
        self.combo_model_select_2.addItem("")
        self.combo_model_select_2.setObjectName(u"combo_model_select_2")
        sizePolicy.setHeightForWidth(self.combo_model_select_2.sizePolicy().hasHeightForWidth())
        self.combo_model_select_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_23.addWidget(self.combo_model_select_2)


        self.thermal_setup_2.addLayout(self.horizontalLayout_23)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.thermal_setup_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_33 = QLabel(Dialog)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_24.addWidget(self.label_33)

        self.heat_convection_2 = QLineEdit(Dialog)
        self.heat_convection_2.setObjectName(u"heat_convection_2")
        sizePolicy.setHeightForWidth(self.heat_convection_2.sizePolicy().hasHeightForWidth())
        self.heat_convection_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_24.addWidget(self.heat_convection_2)


        self.thermal_setup_2.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_34 = QLabel(Dialog)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_25.addWidget(self.label_34)

        self.ambient_temperature_2 = QSpinBox(Dialog)
        self.ambient_temperature_2.setObjectName(u"ambient_temperature_2")
        sizePolicy.setHeightForWidth(self.ambient_temperature_2.sizePolicy().hasHeightForWidth())
        self.ambient_temperature_2.setSizePolicy(sizePolicy)
        self.ambient_temperature_2.setMinimumSize(QSize(15, 0))
        self.ambient_temperature_2.setMaximumSize(QSize(70, 16777215))
        self.ambient_temperature_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ambient_temperature_2.setMaximum(100000)

        self.horizontalLayout_25.addWidget(self.ambient_temperature_2)


        self.thermal_setup_2.addLayout(self.horizontalLayout_25)


        self.verticalLayout_2.addLayout(self.thermal_setup_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_continue = QPushButton(Dialog)
        self.btn_continue.setObjectName(u"btn_continue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_continue.sizePolicy().hasHeightForWidth())
        self.btn_continue.setSizePolicy(sizePolicy1)
        self.btn_continue.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_continue)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        self.btn_continue.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Models Setup", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Converter Type", None))
        self.combo_model_type.setItemText(0, QCoreApplication.translate("Dialog", u"Boost", None))
        self.combo_model_type.setItemText(1, QCoreApplication.translate("Dialog", u"Buck", None))

        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Electrical Setup</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Measure Name", None))
        self.lineedit_measure_name.setText(QCoreApplication.translate("Dialog", u"Efficiency", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Items", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Value", None));
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Thermal Setup</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Measure Name", None))
        self.lineedit_measure_name_3.setText(QCoreApplication.translate("Dialog", u"Maximum Temperature", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Thermal Model", None))
        self.combo_model_select_2.setItemText(0, QCoreApplication.translate("Dialog", u"ParaPower", None))
        self.combo_model_select_2.setItemText(1, QCoreApplication.translate("Dialog", u"TSFM", None))
        self.combo_model_select_2.setItemText(2, QCoreApplication.translate("Dialog", u"Analytical", None))
        self.combo_model_select_2.setItemText(3, "")

        self.label_33.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Heat Convection (W/(m<span style=\" vertical-align:super;\">2</span>\u00b7K))</p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"Ambient Temperature (K)", None))
        self.ambient_temperature_2.setSpecialValueText(QCoreApplication.translate("Dialog", u"300", None))
        self.btn_continue.setText(QCoreApplication.translate("Dialog", u"Continue", None))
    # retranslateUi

