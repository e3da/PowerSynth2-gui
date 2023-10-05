# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editLayout.ui'
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
        Dialog.resize(489, 254)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btn_create_project = QPushButton(Dialog)
        self.btn_create_project.setObjectName(u"btn_create_project")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_project.sizePolicy().hasHeightForWidth())
        self.btn_create_project.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.btn_create_project)


        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.combo_reliability_constraints = QComboBox(Dialog)
        self.combo_reliability_constraints.addItem("")
        self.combo_reliability_constraints.addItem("")
        self.combo_reliability_constraints.addItem("")
        self.combo_reliability_constraints.setObjectName(u"combo_reliability_constraints")
        sizePolicy.setHeightForWidth(self.combo_reliability_constraints.sizePolicy().hasHeightForWidth())
        self.combo_reliability_constraints.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.combo_reliability_constraints)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lineEdit_bondwire = QLineEdit(Dialog)
        self.lineEdit_bondwire.setObjectName(u"lineEdit_bondwire")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_bondwire.sizePolicy().hasHeightForWidth())
        self.lineEdit_bondwire.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.lineEdit_bondwire, 0, 1, 1, 1)

        self.btn_open_bondwire = QPushButton(Dialog)
        self.btn_open_bondwire.setObjectName(u"btn_open_bondwire")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_open_bondwire.sizePolicy().hasHeightForWidth())
        self.btn_open_bondwire.setSizePolicy(sizePolicy3)
        self.btn_open_bondwire.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.btn_open_bondwire, 0, 2, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.btn_edit_materials = QPushButton(Dialog)
        self.btn_edit_materials.setObjectName(u"btn_edit_materials")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_edit_materials.sizePolicy().hasHeightForWidth())
        self.btn_edit_materials.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.btn_edit_materials, 1, 2, 1, 1)

        self.default_mat_lib = QLabel(Dialog)
        self.default_mat_lib.setObjectName(u"default_mat_lib")
        self.default_mat_lib.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.default_mat_lib, 1, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(1, 1)

        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_layout = QLineEdit(Dialog)
        self.lineEdit_layout.setObjectName(u"lineEdit_layout")
        sizePolicy2.setHeightForWidth(self.lineEdit_layout.sizePolicy().hasHeightForWidth())
        self.lineEdit_layout.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.lineEdit_layout, 1, 1, 1, 1)

        self.btn_open_layer_stack = QPushButton(Dialog)
        self.btn_open_layer_stack.setObjectName(u"btn_open_layer_stack")
        sizePolicy3.setHeightForWidth(self.btn_open_layer_stack.sizePolicy().hasHeightForWidth())
        self.btn_open_layer_stack.setSizePolicy(sizePolicy3)
        self.btn_open_layer_stack.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.btn_open_layer_stack, 0, 2, 1, 1)

        self.btn_open_layout = QPushButton(Dialog)
        self.btn_open_layout.setObjectName(u"btn_open_layout")
        sizePolicy3.setHeightForWidth(self.btn_open_layout.sizePolicy().hasHeightForWidth())
        self.btn_open_layout.setSizePolicy(sizePolicy3)
        self.btn_open_layout.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.btn_open_layout, 1, 2, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_layer = QLineEdit(Dialog)
        self.lineEdit_layer.setObjectName(u"lineEdit_layer")
        sizePolicy2.setHeightForWidth(self.lineEdit_layer.sizePolicy().hasHeightForWidth())
        self.lineEdit_layer.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.lineEdit_layer, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Initial Structure and Layout", None))
        self.btn_create_project.setText(QCoreApplication.translate("Dialog", u"Create Layout", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Required", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Reliability Constraints", None))
        self.combo_reliability_constraints.setItemText(0, QCoreApplication.translate("Dialog", u"no constraint", None))
        self.combo_reliability_constraints.setItemText(1, QCoreApplication.translate("Dialog", u"average case", None))
        self.combo_reliability_constraints.setItemText(2, QCoreApplication.translate("Dialog", u"worst case", None))

        self.btn_open_bondwire.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Connectivity Script", None))
        self.btn_edit_materials.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.default_mat_lib.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Materials", None))
        self.btn_open_layer_stack.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.btn_open_layout.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Layer Stack", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Layout Script", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Optional", None))
    # retranslateUi

