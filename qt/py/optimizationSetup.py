# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optimizationSetup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(453, 425)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_generation_setup_frame_2 = QFrame(Dialog)
        self.layout_generation_setup_frame_2.setObjectName(u"layout_generation_setup_frame_2")
        self.layout_generation_setup_frame_2.setFrameShape(QFrame.StyledPanel)
        self.layout_generation_setup_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.layout_generation_setup_frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_17 = QLabel(self.layout_generation_setup_frame_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.layout_generation_setup_frame_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.floor_plan_x = QLineEdit(self.layout_generation_setup_frame_2)
        self.floor_plan_x.setObjectName(u"floor_plan_x")

        self.horizontalLayout_8.addWidget(self.floor_plan_x)

        self.label_13 = QLabel(self.layout_generation_setup_frame_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_8.addWidget(self.label_13)

        self.floor_plan_y = QLineEdit(self.layout_generation_setup_frame_2)
        self.floor_plan_y.setObjectName(u"floor_plan_y")

        self.horizontalLayout_8.addWidget(self.floor_plan_y)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(self.layout_generation_setup_frame_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.checkbox_plot_solutions = QCheckBox(self.layout_generation_setup_frame_2)
        self.checkbox_plot_solutions.setObjectName(u"checkbox_plot_solutions")
        self.checkbox_plot_solutions.setLayoutDirection(Qt.LeftToRight)
        self.checkbox_plot_solutions.setChecked(True)

        self.horizontalLayout_17.addWidget(self.checkbox_plot_solutions)


        self.gridLayout.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.layout_generation_setup_frame_2)

        self.layout_generation_setup_frame = QFrame(Dialog)
        self.layout_generation_setup_frame.setObjectName(u"layout_generation_setup_frame")
        self.layout_generation_setup_frame.setFrameShape(QFrame.StyledPanel)
        self.layout_generation_setup_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.layout_generation_setup_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.layout_generation_setup_frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.combo_layout_mode = QComboBox(self.layout_generation_setup_frame)
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.setObjectName(u"combo_layout_mode")

        self.gridLayout_4.addWidget(self.combo_layout_mode, 0, 1, 1, 1)

        self.num_layouts = QLineEdit(self.layout_generation_setup_frame)
        self.num_layouts.setObjectName(u"num_layouts")
        sizePolicy.setHeightForWidth(self.num_layouts.sizePolicy().hasHeightForWidth())
        self.num_layouts.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.num_layouts, 1, 1, 1, 1)

        self.label_11 = QLabel(self.layout_generation_setup_frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)

        self.seed = QLineEdit(self.layout_generation_setup_frame)
        self.seed.setObjectName(u"seed")
        sizePolicy.setHeightForWidth(self.seed.sizePolicy().hasHeightForWidth())
        self.seed.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.seed, 2, 1, 1, 1)

        self.label_14 = QLabel(self.layout_generation_setup_frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_15 = QLabel(self.layout_generation_setup_frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_16 = QLabel(self.layout_generation_setup_frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 3, 0, 1, 1)

        self.combo_optimization_algorithm = QComboBox(self.layout_generation_setup_frame)
        self.combo_optimization_algorithm.addItem("")
        self.combo_optimization_algorithm.addItem("")
        self.combo_optimization_algorithm.setObjectName(u"combo_optimization_algorithm")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_optimization_algorithm.sizePolicy().hasHeightForWidth())
        self.combo_optimization_algorithm.setSizePolicy(sizePolicy3)
        self.combo_optimization_algorithm.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_4.addWidget(self.combo_optimization_algorithm, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.layout_generation_setup_frame)

        self.electrical_thermal_frame = QFrame(Dialog)
        self.electrical_thermal_frame.setObjectName(u"electrical_thermal_frame")
        self.electrical_thermal_frame.setFrameShape(QFrame.StyledPanel)
        self.electrical_thermal_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.electrical_thermal_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.electrical_thermal_frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.btn_electrical_setup = QPushButton(self.electrical_thermal_frame)
        self.btn_electrical_setup.setObjectName(u"btn_electrical_setup")

        self.gridLayout_2.addWidget(self.btn_electrical_setup, 1, 0, 1, 1)

        self.btn_thermal_setup = QPushButton(self.electrical_thermal_frame)
        self.btn_thermal_setup.setObjectName(u"btn_thermal_setup")

        self.gridLayout_2.addWidget(self.btn_thermal_setup, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.electrical_thermal_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_run_powersynth = QPushButton(Dialog)
        self.btn_run_powersynth.setObjectName(u"btn_run_powersynth")
        self.btn_run_powersynth.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_run_powersynth)


        self.retranslateUi(Dialog)

        self.btn_run_powersynth.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Optimization Setup", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Macro Script Setup:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Floor Plan:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Plot Solution:", None))
        self.checkbox_plot_solutions.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Layout Generation Setup:</span></p></body></html>", None))
        self.combo_layout_mode.setItemText(0, QCoreApplication.translate("Dialog", u"minimum-sized solutions", None))
        self.combo_layout_mode.setItemText(1, QCoreApplication.translate("Dialog", u"variable-sized solutions", None))
        self.combo_layout_mode.setItemText(2, QCoreApplication.translate("Dialog", u"fixed-sized solutions", None))

        self.label_11.setText(QCoreApplication.translate("Dialog", u"Layout_Mode:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Layout Count (per generation):", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Seed:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Optimization Algorithm:", None))
        self.combo_optimization_algorithm.setItemText(0, QCoreApplication.translate("Dialog", u"NG-RANDOM", None))
        self.combo_optimization_algorithm.setItemText(1, QCoreApplication.translate("Dialog", u"NSGAII", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Layout Model Setup:</span></p></body></html>", None))
        self.btn_electrical_setup.setText(QCoreApplication.translate("Dialog", u"Electrical Setup", None))
        self.btn_thermal_setup.setText(QCoreApplication.translate("Dialog", u"Thermal Setup", None))
        self.btn_run_powersynth.setText(QCoreApplication.translate("Dialog", u"Run Powersynth", None))
    # retranslateUi

