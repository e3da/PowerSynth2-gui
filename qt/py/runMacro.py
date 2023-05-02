# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runMacro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
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
        Dialog.resize(503, 100)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.btn_open_macro = QPushButton(Dialog)
        self.btn_open_macro.setObjectName(u"btn_open_macro")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_open_macro.sizePolicy().hasHeightForWidth())
        self.btn_open_macro.setSizePolicy(sizePolicy1)
        self.btn_open_macro.setMinimumSize(QSize(0, 0))
        self.btn_open_macro.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_open_macro)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.btn_create_project = QPushButton(Dialog)
        self.btn_create_project.setObjectName(u"btn_create_project")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_create_project.sizePolicy().hasHeightForWidth())
        self.btn_create_project.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.btn_create_project)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy2.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Run Project", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"macro_script", None))
        self.btn_open_macro.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.btn_create_project.setText(QCoreApplication.translate("Dialog", u"Run Project", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

