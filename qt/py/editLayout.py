# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editLayout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Macro_Input_Paths(object):
    def setupUi(self, Macro_Input_Paths):
        if not Macro_Input_Paths.objectName():
            Macro_Input_Paths.setObjectName(u"Macro_Input_Paths")
        Macro_Input_Paths.resize(547, 319)
        self.gridLayout = QGridLayout(Macro_Input_Paths)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Macro_Input_Paths)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_layer = QLineEdit(Macro_Input_Paths)
        self.lineEdit_layer.setObjectName(u"lineEdit_layer")

        self.horizontalLayout_4.addWidget(self.lineEdit_layer)

        self.btn_open_layer_stack = QPushButton(Macro_Input_Paths)
        self.btn_open_layer_stack.setObjectName(u"btn_open_layer_stack")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_layer_stack.sizePolicy().hasHeightForWidth())
        self.btn_open_layer_stack.setSizePolicy(sizePolicy)
        self.btn_open_layer_stack.setMinimumSize(QSize(0, 0))
        self.btn_open_layer_stack.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_open_layer_stack)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(Macro_Input_Paths)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_bondwire = QLineEdit(Macro_Input_Paths)
        self.lineEdit_bondwire.setObjectName(u"lineEdit_bondwire")

        self.horizontalLayout_6.addWidget(self.lineEdit_bondwire)

        self.btn_open_bondwire = QPushButton(Macro_Input_Paths)
        self.btn_open_bondwire.setObjectName(u"btn_open_bondwire")
        sizePolicy.setHeightForWidth(self.btn_open_bondwire.sizePolicy().hasHeightForWidth())
        self.btn_open_bondwire.setSizePolicy(sizePolicy)
        self.btn_open_bondwire.setMinimumSize(QSize(0, 0))
        self.btn_open_bondwire.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_open_bondwire)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Macro_Input_Paths)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_layout = QLineEdit(Macro_Input_Paths)
        self.lineEdit_layout.setObjectName(u"lineEdit_layout")

        self.horizontalLayout_2.addWidget(self.lineEdit_layout)

        self.btn_open_layout = QPushButton(Macro_Input_Paths)
        self.btn_open_layout.setObjectName(u"btn_open_layout")
        sizePolicy.setHeightForWidth(self.btn_open_layout.sizePolicy().hasHeightForWidth())
        self.btn_open_layout.setSizePolicy(sizePolicy)
        self.btn_open_layout.setMinimumSize(QSize(0, 0))
        self.btn_open_layout.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_open_layout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Macro_Input_Paths)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.combo_reliability_constraints = QComboBox(Macro_Input_Paths)
        self.combo_reliability_constraints.addItem("")
        self.combo_reliability_constraints.addItem("")
        self.combo_reliability_constraints.addItem("")
        self.combo_reliability_constraints.setObjectName(u"combo_reliability_constraints")

        self.horizontalLayout.addWidget(self.combo_reliability_constraints)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(Macro_Input_Paths)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(420, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.btn_create_project = QPushButton(Macro_Input_Paths)
        self.btn_create_project.setObjectName(u"btn_create_project")
        sizePolicy.setHeightForWidth(self.btn_create_project.sizePolicy().hasHeightForWidth())
        self.btn_create_project.setSizePolicy(sizePolicy)
        self.btn_create_project.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.btn_create_project)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)


        self.retranslateUi(Macro_Input_Paths)

        QMetaObject.connectSlotsByName(Macro_Input_Paths)
    # setupUi

    def retranslateUi(self, Macro_Input_Paths):
        Macro_Input_Paths.setWindowTitle(QCoreApplication.translate("Macro_Input_Paths", u"Initial Structure and Layout", None))
        self.label_4.setText(QCoreApplication.translate("Macro_Input_Paths", u"layer_stack", None))
        self.btn_open_layer_stack.setText(QCoreApplication.translate("Macro_Input_Paths", u"Open File", None))
        self.label_5.setText(QCoreApplication.translate("Macro_Input_Paths", u"Connectivity_script", None))
        self.btn_open_bondwire.setText(QCoreApplication.translate("Macro_Input_Paths", u"Open File", None))
        self.label_2.setText(QCoreApplication.translate("Macro_Input_Paths", u"layout_script", None))
        self.btn_open_layout.setText(QCoreApplication.translate("Macro_Input_Paths", u"Open File", None))
        self.label.setText(QCoreApplication.translate("Macro_Input_Paths", u"Reliability Constraints:", None))
        self.combo_reliability_constraints.setItemText(0, QCoreApplication.translate("Macro_Input_Paths", u"no constraints", None))
        self.combo_reliability_constraints.setItemText(1, QCoreApplication.translate("Macro_Input_Paths", u"average case", None))
        self.combo_reliability_constraints.setItemText(2, QCoreApplication.translate("Macro_Input_Paths", u"worst case consideration", None))

        self.pushButton.setText(QCoreApplication.translate("Macro_Input_Paths", u"Edit Materials", None))
        self.btn_create_project.setText(QCoreApplication.translate("Macro_Input_Paths", u"Create Layout", None))
    # retranslateUi

