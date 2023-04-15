# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solutionBrowser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_CornerStitch_Dialog(object):
    def setupUi(self, CornerStitch_Dialog):
        if not CornerStitch_Dialog.objectName():
            CornerStitch_Dialog.setObjectName(u"CornerStitch_Dialog")
        CornerStitch_Dialog.resize(1373, 747)
        self.horizontalLayout_3 = QHBoxLayout(CornerStitch_Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.grbox_view = QGroupBox(CornerStitch_Dialog)
        self.grbox_view.setObjectName(u"grbox_view")
        self.grbox_view.setMinimumSize(QSize(600, 600))
        self.grbox_view.setMaximumSize(QSize(16777215, 16777215))
        self.grbox_view.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_2 = QVBoxLayout(self.grbox_view)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.grbox_view)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(1000, 1500))

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.grbox_view)

        self.groupBox_2 = QGroupBox(CornerStitch_Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grview_sols_browser = QGraphicsView(self.groupBox_2)
        self.grview_sols_browser.setObjectName(u"grview_sols_browser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.grview_sols_browser.sizePolicy().hasHeightForWidth())
        self.grview_sols_browser.setSizePolicy(sizePolicy1)
        self.grview_sols_browser.setMaximumSize(QSize(2000, 16777215))
        self.grview_sols_browser.setLayoutDirection(Qt.LeftToRight)
        self.grview_sols_browser.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.grview_sols_browser, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_initial_layout = QPushButton(self.groupBox_2)
        self.btn_initial_layout.setObjectName(u"btn_initial_layout")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_initial_layout.sizePolicy().hasHeightForWidth())
        self.btn_initial_layout.setSizePolicy(sizePolicy2)
        self.btn_initial_layout.setMaximumSize(QSize(200, 16777215))
        self.btn_initial_layout.setLayoutDirection(Qt.LeftToRight)
        self.btn_initial_layout.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.btn_initial_layout)

        self.btn_export_selected = QPushButton(self.groupBox_2)
        self.btn_export_selected.setObjectName(u"btn_export_selected")
        self.btn_export_selected.setMaximumSize(QSize(200, 16777215))
        self.btn_export_selected.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_export_selected)

        self.btn_export_all = QPushButton(self.groupBox_2)
        self.btn_export_all.setObjectName(u"btn_export_all")
        self.btn_export_all.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_export_all)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_exit = QPushButton(self.groupBox_2)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy2.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy2)
        self.btn_exit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_exit)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.x_label = QLabel(self.groupBox_2)
        self.x_label.setObjectName(u"x_label")

        self.horizontalLayout.addWidget(self.x_label)

        self.lineEdit_x = QLineEdit(self.groupBox_2)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        sizePolicy2.setHeightForWidth(self.lineEdit_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_x.setSizePolicy(sizePolicy2)
        self.lineEdit_x.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_x)

        self.label_units1 = QLabel(self.groupBox_2)
        self.label_units1.setObjectName(u"label_units1")

        self.horizontalLayout.addWidget(self.label_units1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.y_label = QLabel(self.groupBox_2)
        self.y_label.setObjectName(u"y_label")

        self.horizontalLayout.addWidget(self.y_label)

        self.lineEdit_y = QLineEdit(self.groupBox_2)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        sizePolicy2.setHeightForWidth(self.lineEdit_y.sizePolicy().hasHeightForWidth())
        self.lineEdit_y.setSizePolicy(sizePolicy2)
        self.lineEdit_y.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_y)

        self.label_units2 = QLabel(self.groupBox_2)
        self.label_units2.setObjectName(u"label_units2")

        self.horizontalLayout.addWidget(self.label_units2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_size_w = QLineEdit(self.groupBox_2)
        self.lineEdit_size_w.setObjectName(u"lineEdit_size_w")
        sizePolicy2.setHeightForWidth(self.lineEdit_size_w.sizePolicy().hasHeightForWidth())
        self.lineEdit_size_w.setSizePolicy(sizePolicy2)
        self.lineEdit_size_w.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_size_w)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_size_h = QLineEdit(self.groupBox_2)
        self.lineEdit_size_h.setObjectName(u"lineEdit_size_h")
        sizePolicy2.setHeightForWidth(self.lineEdit_size_h.sizePolicy().hasHeightForWidth())
        self.lineEdit_size_h.setSizePolicy(sizePolicy2)
        self.lineEdit_size_h.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_size_h)

        self.horizontalSpacer = QSpacerItem(1000, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(CornerStitch_Dialog)

        self.tabWidget.setCurrentIndex(-1)
        self.btn_export_selected.setDefault(False)
        self.btn_export_all.setDefault(False)
        self.btn_exit.setDefault(True)


        QMetaObject.connectSlotsByName(CornerStitch_Dialog)
    # setupUi

    def retranslateUi(self, CornerStitch_Dialog):
        CornerStitch_Dialog.setWindowTitle(QCoreApplication.translate("CornerStitch_Dialog", u"Solution Browser ", None))
        self.grbox_view.setTitle(QCoreApplication.translate("CornerStitch_Dialog", u"Layout Visualization", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CornerStitch_Dialog", u"Layout Selection", None))
        self.btn_initial_layout.setText(QCoreApplication.translate("CornerStitch_Dialog", u" View Initial Layout", None))
        self.btn_export_selected.setText(QCoreApplication.translate("CornerStitch_Dialog", u"Export Selected Solution", None))
        self.btn_export_all.setText(QCoreApplication.translate("CornerStitch_Dialog", u"Export All Solutions", None))
        self.btn_exit.setText(QCoreApplication.translate("CornerStitch_Dialog", u"Exit", None))
        self.x_label.setText(QCoreApplication.translate("CornerStitch_Dialog", u"text1", None))
        self.label_units1.setText(QCoreApplication.translate("CornerStitch_Dialog", u"units1", None))
        self.y_label.setText(QCoreApplication.translate("CornerStitch_Dialog", u"text2", None))
        self.label_units2.setText(QCoreApplication.translate("CornerStitch_Dialog", u"units2", None))
        self.label_4.setText(QCoreApplication.translate("CornerStitch_Dialog", u"size:", None))
        self.label.setText(QCoreApplication.translate("CornerStitch_Dialog", u"X", None))
    # retranslateUi

