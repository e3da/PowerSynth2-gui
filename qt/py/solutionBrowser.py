# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solutionBrowser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CornerStitch_Dialog(object):
    def setupUi(self, CornerStitch_Dialog):
        if not CornerStitch_Dialog.objectName():
            CornerStitch_Dialog.setObjectName(u"CornerStitch_Dialog")
        CornerStitch_Dialog.resize(1203, 747)
        self.horizontalLayout_3 = QHBoxLayout(CornerStitch_Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.grbox_view = QGroupBox(CornerStitch_Dialog)
        self.grbox_view.setObjectName(u"grbox_view")
        self.grbox_view.setMinimumSize(QSize(0, 0))
        self.grbox_view.setMaximumSize(QSize(16777215, 16777215))
        self.grbox_view.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_2 = QVBoxLayout(self.grbox_view)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.tabWidget = QTabWidget(self.grbox_view)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(300, 300))
        self.tabWidget.setMaximumSize(QSize(1000, 1500))

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.x_label = QLabel(self.grbox_view)
        self.x_label.setObjectName(u"x_label")

        self.horizontalLayout.addWidget(self.x_label)

        self.lineEdit_x = QLineEdit(self.grbox_view)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_x.setSizePolicy(sizePolicy1)
        self.lineEdit_x.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_x)

        self.label_units1 = QLabel(self.grbox_view)
        self.label_units1.setObjectName(u"label_units1")

        self.horizontalLayout.addWidget(self.label_units1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.y_label = QLabel(self.grbox_view)
        self.y_label.setObjectName(u"y_label")

        self.horizontalLayout.addWidget(self.y_label)

        self.lineEdit_y = QLineEdit(self.grbox_view)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        sizePolicy1.setHeightForWidth(self.lineEdit_y.sizePolicy().hasHeightForWidth())
        self.lineEdit_y.setSizePolicy(sizePolicy1)
        self.lineEdit_y.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_y)

        self.label_units2 = QLabel(self.grbox_view)
        self.label_units2.setObjectName(u"label_units2")

        self.horizontalLayout.addWidget(self.label_units2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.lineEdit_size_w = QLineEdit(self.grbox_view)
        self.lineEdit_size_w.setObjectName(u"lineEdit_size_w")
        sizePolicy1.setHeightForWidth(self.lineEdit_size_w.sizePolicy().hasHeightForWidth())
        self.lineEdit_size_w.setSizePolicy(sizePolicy1)
        self.lineEdit_size_w.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_size_w)

        self.label = QLabel(self.grbox_view)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_size_h = QLineEdit(self.grbox_view)
        self.lineEdit_size_h.setObjectName(u"lineEdit_size_h")
        sizePolicy1.setHeightForWidth(self.lineEdit_size_h.sizePolicy().hasHeightForWidth())
        self.lineEdit_size_h.setSizePolicy(sizePolicy1)
        self.lineEdit_size_h.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_size_h)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.grbox_view)

        self.groupBox_2 = QGroupBox(CornerStitch_Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.grview_sols_browser = QGraphicsView(self.groupBox_2)
        self.grview_sols_browser.setObjectName(u"grview_sols_browser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.grview_sols_browser.sizePolicy().hasHeightForWidth())
        self.grview_sols_browser.setSizePolicy(sizePolicy2)
        self.grview_sols_browser.setMinimumSize(QSize(400, 400))
        self.grview_sols_browser.setMaximumSize(QSize(2000, 16777215))
        self.grview_sols_browser.setLayoutDirection(Qt.LeftToRight)
        self.grview_sols_browser.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.grview_sols_browser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_initial_layout = QPushButton(self.groupBox_2)
        self.btn_initial_layout.setObjectName(u"btn_initial_layout")
        sizePolicy1.setHeightForWidth(self.btn_initial_layout.sizePolicy().hasHeightForWidth())
        self.btn_initial_layout.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_exit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


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
        self.x_label.setText(QCoreApplication.translate("CornerStitch_Dialog", u"text1", None))
        self.label_units1.setText(QCoreApplication.translate("CornerStitch_Dialog", u"units1", None))
        self.y_label.setText(QCoreApplication.translate("CornerStitch_Dialog", u"text2", None))
        self.label_units2.setText(QCoreApplication.translate("CornerStitch_Dialog", u"units2", None))
        self.label.setText(QCoreApplication.translate("CornerStitch_Dialog", u"X", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CornerStitch_Dialog", u"Layout Selection", None))
        self.btn_initial_layout.setText(QCoreApplication.translate("CornerStitch_Dialog", u" View Initial Layout", None))
        self.btn_export_selected.setText(QCoreApplication.translate("CornerStitch_Dialog", u"Export Selected Solution", None))
        self.btn_export_all.setText(QCoreApplication.translate("CornerStitch_Dialog", u"Export All Solutions", None))
        self.btn_exit.setText(QCoreApplication.translate("CornerStitch_Dialog", u"Exit", None))
    # retranslateUi

