# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optimizationSetup.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(417, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.base_setup = QVBoxLayout()
        self.base_setup.setObjectName(u"base_setup")
        self.base_setup.setContentsMargins(4, 4, 4, 4)
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.base_setup.addWidget(self.label_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.floor_plan_x = QLineEdit(Dialog)
        self.floor_plan_x.setObjectName(u"floor_plan_x")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.floor_plan_x.sizePolicy().hasHeightForWidth())
        self.floor_plan_x.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.floor_plan_x)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_8.addWidget(self.label_13)

        self.floor_plan_y = QLineEdit(Dialog)
        self.floor_plan_y.setObjectName(u"floor_plan_y")
        sizePolicy1.setHeightForWidth(self.floor_plan_y.sizePolicy().hasHeightForWidth())
        self.floor_plan_y.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.floor_plan_y)


        self.base_setup.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.checkbox_plot_solutions = QCheckBox(Dialog)
        self.checkbox_plot_solutions.setObjectName(u"checkbox_plot_solutions")
        sizePolicy.setHeightForWidth(self.checkbox_plot_solutions.sizePolicy().hasHeightForWidth())
        self.checkbox_plot_solutions.setSizePolicy(sizePolicy)
        self.checkbox_plot_solutions.setLayoutDirection(Qt.LeftToRight)
        self.checkbox_plot_solutions.setChecked(True)

        self.horizontalLayout_17.addWidget(self.checkbox_plot_solutions)


        self.base_setup.addLayout(self.horizontalLayout_17)

        self.layout_synthesis_setup = QFrame(Dialog)
        self.layout_synthesis_setup.setObjectName(u"layout_synthesis_setup")
        self.layout_synthesis_setup.setFrameShape(QFrame.StyledPanel)
        self.layout_synthesis_setup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.layout_synthesis_setup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layout_synthesis_setup)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_4.addWidget(self.label_17)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.num_layouts = QLineEdit(self.layout_synthesis_setup)
        self.num_layouts.setObjectName(u"num_layouts")
        sizePolicy.setHeightForWidth(self.num_layouts.sizePolicy().hasHeightForWidth())
        self.num_layouts.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.num_layouts, 2, 1, 1, 1)

        self.combo_layout_mode = QComboBox(self.layout_synthesis_setup)
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.addItem("")
        self.combo_layout_mode.setObjectName(u"combo_layout_mode")
        sizePolicy.setHeightForWidth(self.combo_layout_mode.sizePolicy().hasHeightForWidth())
        self.combo_layout_mode.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.combo_layout_mode, 1, 1, 1, 1)

        self.seed = QLineEdit(self.layout_synthesis_setup)
        self.seed.setObjectName(u"seed")
        sizePolicy.setHeightForWidth(self.seed.sizePolicy().hasHeightForWidth())
        self.seed.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.seed, 3, 1, 1, 1)

        self.label_15 = QLabel(self.layout_synthesis_setup)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_14 = QLabel(self.layout_synthesis_setup)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.combo_optimization_algorithm = QComboBox(self.layout_synthesis_setup)
        self.combo_optimization_algorithm.addItem("")
        self.combo_optimization_algorithm.addItem("")
        self.combo_optimization_algorithm.addItem("")
        self.combo_optimization_algorithm.setObjectName(u"combo_optimization_algorithm")
        sizePolicy.setHeightForWidth(self.combo_optimization_algorithm.sizePolicy().hasHeightForWidth())
        self.combo_optimization_algorithm.setSizePolicy(sizePolicy)
        self.combo_optimization_algorithm.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_4.addWidget(self.combo_optimization_algorithm, 4, 1, 1, 1)

        self.label_11 = QLabel(self.layout_synthesis_setup)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_16 = QLabel(self.layout_synthesis_setup)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_16, 4, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.base_setup.addWidget(self.layout_synthesis_setup)

        self.optimization_setup = QFrame(Dialog)
        self.optimization_setup.setObjectName(u"optimization_setup")
        self.optimization_setup.setFrameShape(QFrame.StyledPanel)
        self.optimization_setup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.optimization_setup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.optimization_setup)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.misc_setup = QGridLayout()
        self.misc_setup.setObjectName(u"misc_setup")
        self.num_gen = QLineEdit(self.optimization_setup)
        self.num_gen.setObjectName(u"num_gen")
        sizePolicy.setHeightForWidth(self.num_gen.sizePolicy().hasHeightForWidth())
        self.num_gen.setSizePolicy(sizePolicy)

        self.misc_setup.addWidget(self.num_gen, 1, 1, 1, 1)

        self.label_4 = QLabel(self.optimization_setup)
        self.label_4.setObjectName(u"label_4")

        self.misc_setup.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.misc_setup)


        self.base_setup.addWidget(self.optimization_setup)

        self.analysis_model_setup = QFrame(Dialog)
        self.analysis_model_setup.setObjectName(u"analysis_model_setup")
        self.analysis_model_setup.setFrameShape(QFrame.StyledPanel)
        self.analysis_model_setup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.analysis_model_setup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.analysis_model_setup)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_electrical_setup = QPushButton(self.analysis_model_setup)
        self.btn_electrical_setup.setObjectName(u"btn_electrical_setup")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_electrical_setup.sizePolicy().hasHeightForWidth())
        self.btn_electrical_setup.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.btn_electrical_setup)

        self.btn_thermal_setup = QPushButton(self.analysis_model_setup)
        self.btn_thermal_setup.setObjectName(u"btn_thermal_setup")
        sizePolicy3.setHeightForWidth(self.btn_thermal_setup.sizePolicy().hasHeightForWidth())
        self.btn_thermal_setup.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.btn_thermal_setup)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.base_setup.addWidget(self.analysis_model_setup)


        self.verticalLayout.addLayout(self.base_setup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_run_powersynth = QPushButton(Dialog)
        self.btn_run_powersynth.setObjectName(u"btn_run_powersynth")
        sizePolicy.setHeightForWidth(self.btn_run_powersynth.sizePolicy().hasHeightForWidth())
        self.btn_run_powersynth.setSizePolicy(sizePolicy)
        self.btn_run_powersynth.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setBold(True)
        self.btn_run_powersynth.setFont(font)

        self.verticalLayout.addWidget(self.btn_run_powersynth)


        self.retranslateUi(Dialog)

        self.btn_run_powersynth.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Optimization Setup", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Floorplan Setup</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Size", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"W x H", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Plot Solution", None))
        self.checkbox_plot_solutions.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Layout Synthesis Setup</span></p></body></html>", None))
        self.combo_layout_mode.setItemText(0, QCoreApplication.translate("Dialog", u"minimum-sized solutions", None))
        self.combo_layout_mode.setItemText(1, QCoreApplication.translate("Dialog", u"variable-sized solutions", None))
        self.combo_layout_mode.setItemText(2, QCoreApplication.translate("Dialog", u"fixed-sized solutions", None))

        self.seed.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Random Seed", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Layout Count", None))
        self.combo_optimization_algorithm.setItemText(0, QCoreApplication.translate("Dialog", u"NG-RANDOM", None))
        self.combo_optimization_algorithm.setItemText(1, QCoreApplication.translate("Dialog", u"NSGAII", None))
        self.combo_optimization_algorithm.setItemText(2, QCoreApplication.translate("Dialog", u"MOPSO", None))

        self.label_11.setText(QCoreApplication.translate("Dialog", u"Layout Mode", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Optimization Algorithm", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Optimization Setup</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Number of Generations", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Analysis Model Setup</span></p></body></html>", None))
        self.btn_electrical_setup.setText(QCoreApplication.translate("Dialog", u"Electrical Setup", None))
        self.btn_thermal_setup.setText(QCoreApplication.translate("Dialog", u"Thermal Setup", None))
        self.btn_run_powersynth.setText(QCoreApplication.translate("Dialog", u"Run", None))
    # retranslateUi

