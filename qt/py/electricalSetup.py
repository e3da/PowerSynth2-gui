# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'electricalSetup.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
        Dialog.resize(400, 500)
        Dialog.setMinimumSize(QSize(350, 400))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.electrical_setup = QVBoxLayout()
        self.electrical_setup.setObjectName(u"electrical_setup")
        self.electrical_setup.setContentsMargins(4, 4, 4, 4)
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")

        self.electrical_setup.addWidget(self.label_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.lineedit_measure_name = QLineEdit(Dialog)
        self.lineedit_measure_name.setObjectName(u"lineedit_measure_name")
        sizePolicy.setHeightForWidth(self.lineedit_measure_name.sizePolicy().hasHeightForWidth())
        self.lineedit_measure_name.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.lineedit_measure_name)


        self.electrical_setup.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_17.addWidget(self.label_24)

        self.combo_model_type = QComboBox(Dialog)
        self.combo_model_type.addItem("")
        self.combo_model_type.addItem("")
        self.combo_model_type.setObjectName(u"combo_model_type")
        sizePolicy.setHeightForWidth(self.combo_model_type.sizePolicy().hasHeightForWidth())
        self.combo_model_type.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.combo_model_type)


        self.electrical_setup.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.combo_measure_type = QComboBox(Dialog)
        self.combo_measure_type.addItem("")
        self.combo_measure_type.addItem("")
        self.combo_measure_type.setObjectName(u"combo_measure_type")
        sizePolicy.setHeightForWidth(self.combo_measure_type.sizePolicy().hasHeightForWidth())
        self.combo_measure_type.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.combo_measure_type)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.label_23 = QLabel(Dialog)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.frequency = QSpinBox(Dialog)
        self.frequency.setObjectName(u"frequency")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frequency.sizePolicy().hasHeightForWidth())
        self.frequency.setSizePolicy(sizePolicy2)
        self.frequency.setMinimumSize(QSize(20, 0))
        self.frequency.setMaximumSize(QSize(70, 16777215))
        self.frequency.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.frequency.setMaximum(1000000000)

        self.horizontalLayout_13.addWidget(self.frequency)


        self.electrical_setup.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(Dialog)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_15.addWidget(self.label_21)

        self.combo_source = QComboBox(Dialog)
        self.combo_source.setObjectName(u"combo_source")
        sizePolicy.setHeightForWidth(self.combo_source.sizePolicy().hasHeightForWidth())
        self.combo_source.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.combo_source)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)

        self.label_22 = QLabel(Dialog)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_15.addWidget(self.label_22)

        self.combo_sink = QComboBox(Dialog)
        self.combo_sink.setObjectName(u"combo_sink")
        sizePolicy.setHeightForWidth(self.combo_sink.sizePolicy().hasHeightForWidth())
        self.combo_sink.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.combo_sink)


        self.electrical_setup.addLayout(self.horizontalLayout_15)

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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.btn_add_device = QPushButton(Dialog)
        self.btn_add_device.setObjectName(u"btn_add_device")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_add_device.sizePolicy().hasHeightForWidth())
        self.btn_add_device.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.btn_add_device)

        self.btn_add_all = QPushButton(Dialog)
        self.btn_add_all.setObjectName(u"btn_add_all")
        sizePolicy3.setHeightForWidth(self.btn_add_all.sizePolicy().hasHeightForWidth())
        self.btn_add_all.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.btn_add_all)

        self.btn_remove_device = QPushButton(Dialog)
        self.btn_remove_device.setObjectName(u"btn_remove_device")
        sizePolicy3.setHeightForWidth(self.btn_remove_device.sizePolicy().hasHeightForWidth())
        self.btn_remove_device.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.btn_remove_device)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.electrical_setup.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.trace_textedit = QLineEdit(Dialog)
        self.trace_textedit.setObjectName(u"trace_textedit")
        sizePolicy1.setHeightForWidth(self.trace_textedit.sizePolicy().hasHeightForWidth())
        self.trace_textedit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.trace_textedit)

        self.btn_open_trace = QPushButton(Dialog)
        self.btn_open_trace.setObjectName(u"btn_open_trace")
        sizePolicy2.setHeightForWidth(self.btn_open_trace.sizePolicy().hasHeightForWidth())
        self.btn_open_trace.setSizePolicy(sizePolicy2)
        self.btn_open_trace.setMinimumSize(QSize(0, 0))
        self.btn_open_trace.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_open_trace)


        self.electrical_setup.addLayout(self.horizontalLayout_4)

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
        self.label_6 = QLabel(self.parasitic_model_frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label_6)

        self.parasitic_textedit = QLineEdit(self.parasitic_model_frame)
        self.parasitic_textedit.setObjectName(u"parasitic_textedit")
        sizePolicy1.setHeightForWidth(self.parasitic_textedit.sizePolicy().hasHeightForWidth())
        self.parasitic_textedit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.parasitic_textedit)

        self.btn_open_parasitic = QPushButton(self.parasitic_model_frame)
        self.btn_open_parasitic.setObjectName(u"btn_open_parasitic")
        sizePolicy2.setHeightForWidth(self.btn_open_parasitic.sizePolicy().hasHeightForWidth())
        self.btn_open_parasitic.setSizePolicy(sizePolicy2)
        self.btn_open_parasitic.setMinimumSize(QSize(0, 0))
        self.btn_open_parasitic.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_open_parasitic)


        self.electrical_setup.addWidget(self.parasitic_model_frame)


        self.verticalLayout_2.addLayout(self.electrical_setup)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_continue = QPushButton(Dialog)
        self.btn_continue.setObjectName(u"btn_continue")
        sizePolicy3.setHeightForWidth(self.btn_continue.sizePolicy().hasHeightForWidth())
        self.btn_continue.setSizePolicy(sizePolicy3)
        self.btn_continue.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_continue)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        self.btn_continue.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Electrical Setup", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Electrical Setup</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Measure Name", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Electrical Model", None))
        self.combo_model_type.setItemText(0, QCoreApplication.translate("Dialog", u"FastHenry", None))
        self.combo_model_type.setItemText(1, QCoreApplication.translate("Dialog", u"PEEC", None))

        self.label_20.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.combo_measure_type.setItemText(0, QCoreApplication.translate("Dialog", u"inductance", None))
        self.combo_measure_type.setItemText(1, QCoreApplication.translate("Dialog", u"resistance", None))

        self.label_23.setText(QCoreApplication.translate("Dialog", u"Freq. (kHz)", None))
        self.frequency.setSpecialValueText(QCoreApplication.translate("Dialog", u"10000", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Source", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Sink", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Device", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Options", None));
        self.btn_add_device.setText(QCoreApplication.translate("Dialog", u"Add Device", None))
        self.btn_add_all.setText(QCoreApplication.translate("Dialog", u"Add All", None))
        self.btn_remove_device.setText(QCoreApplication.translate("Dialog", u"Remove Device", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Trace Orientation", None))
        self.btn_open_trace.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Parasitic Model", None))
        self.btn_open_parasitic.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.btn_continue.setText(QCoreApplication.translate("Dialog", u"Continue", None))
    # retranslateUi

