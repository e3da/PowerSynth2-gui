# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runMacro.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 100)
        Dialog.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_macro = QLineEdit(Dialog)
        self.line_macro.setObjectName(u"line_macro")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_macro.sizePolicy().hasHeightForWidth())
        self.line_macro.setSizePolicy(sizePolicy)
        self.line_macro.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.line_macro)

        self.btn_open_macro = QPushButton(Dialog)
        self.btn_open_macro.setObjectName(u"btn_open_macro")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
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
        sizePolicy1.setHeightForWidth(self.btn_create_project.sizePolicy().hasHeightForWidth())
        self.btn_create_project.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.btn_create_project.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_create_project)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Run Macro", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Macro Script", None))
        self.btn_open_macro.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.btn_create_project.setText(QCoreApplication.translate("Dialog", u"Run", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

