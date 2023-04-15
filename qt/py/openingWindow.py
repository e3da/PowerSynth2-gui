# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openingWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from  . import png_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(444, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/png/PS2_logo.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_web = QPushButton(Dialog)
        self.open_web.setObjectName(u"open_web")

        self.horizontalLayout.addWidget(self.open_web)

        self.open_manual = QPushButton(Dialog)
        self.open_manual.setObjectName(u"open_manual")

        self.horizontalLayout.addWidget(self.open_manual)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.create_macro = QPushButton(Dialog)
        self.create_macro.setObjectName(u"create_macro")

        self.horizontalLayout_2.addWidget(self.create_macro)

        self.run_macro = QPushButton(Dialog)
        self.run_macro.setObjectName(u"run_macro")

        self.horizontalLayout_2.addWidget(self.run_macro)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        self.create_macro.setDefault(False)
        self.run_macro.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"PowerSynth", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Welcome to PowerSynth 2!</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; font-style:italic;\">Developed by </span><span style=\" font-size:10pt; font-weight:700;\">E</span><span style=\" font-size:10pt; font-weight:700; vertical-align:super;\">3</span><span style=\" font-size:10pt; font-weight:700;\">DA</span><span style=\" font-size:10pt; font-weight:700; font-style:italic;\"> and </span><span style=\" font-size:10pt; font-weight:700;\">MSCAD</span><span style=\" font-size:10pt; font-weight:700; font-style:italic;\"> Labs</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Click on Create a Macro to start a new project<br/>or click on Run a Macro to run a pre-existing macro_script.</p></body></html>", None))
        self.open_web.setText(QCoreApplication.translate("Dialog", u"Open Website", None))
        self.open_manual.setText(QCoreApplication.translate("Dialog", u"Open Manual", None))
        self.create_macro.setText(QCoreApplication.translate("Dialog", u"Create a Macro", None))
        self.run_macro.setText(QCoreApplication.translate("Dialog", u"Run PowerSynth", None))
    # retranslateUi

