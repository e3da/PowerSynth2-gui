# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_Library.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MDKWindow(object):
    def setupUi(self, MDKWindow):
        if not MDKWindow.objectName():
            MDKWindow.setObjectName(u"MDKWindow")
        MDKWindow.resize(944, 542)
        self.actionImport = QAction(MDKWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionSave = QAction(MDKWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionImport_file = QAction(MDKWindow)
        self.actionImport_file.setObjectName(u"actionImport_file")
        self.actionType_Material = QAction(MDKWindow)
        self.actionType_Material.setObjectName(u"actionType_Material")
        self.actionImport_2 = QAction(MDKWindow)
        self.actionImport_2.setObjectName(u"actionImport_2")
        self.actionOpen_explanation = QAction(MDKWindow)
        self.actionOpen_explanation.setObjectName(u"actionOpen_explanation")
        self.centralwidget = QWidget(MDKWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 741, 491))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 711, 411))
        self.remove_all_button = QPushButton(self.tab)
        self.remove_all_button.setObjectName(u"remove_all_button")
        self.remove_all_button.setGeometry(QRect(480, 430, 75, 23))
        self.remove_all_button.setMouseTracking(True)
        self.add_all_button = QPushButton(self.tab)
        self.add_all_button.setObjectName(u"add_all_button")
        self.add_all_button.setGeometry(QRect(120, 430, 75, 23))
        self.add_all_button.setMouseTracking(True)
        self.update_all_button = QPushButton(self.tab)
        self.update_all_button.setObjectName(u"update_all_button")
        self.update_all_button.setGeometry(QRect(360, 430, 75, 23))
        self.update_all_button.setMouseTracking(True)
        self.clone_all_button = QPushButton(self.tab)
        self.clone_all_button.setObjectName(u"clone_all_button")
        self.clone_all_button.setGeometry(QRect(240, 430, 75, 23))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 11):
            self.tableWidget_2.setColumnCount(11)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 10, 711, 411))
        self.remove_pcm_button = QPushButton(self.tab_2)
        self.remove_pcm_button.setObjectName(u"remove_pcm_button")
        self.remove_pcm_button.setGeometry(QRect(480, 430, 75, 23))
        self.remove_pcm_button.setMouseTracking(True)
        self.add_pcm_button = QPushButton(self.tab_2)
        self.add_pcm_button.setObjectName(u"add_pcm_button")
        self.add_pcm_button.setGeometry(QRect(120, 430, 75, 23))
        self.add_pcm_button.setMouseTracking(True)
        self.update_pcm_button = QPushButton(self.tab_2)
        self.update_pcm_button.setObjectName(u"update_pcm_button")
        self.update_pcm_button.setGeometry(QRect(360, 430, 75, 23))
        self.update_pcm_button.setMouseTracking(True)
        self.clone_pcm_button = QPushButton(self.tab_2)
        self.clone_pcm_button.setObjectName(u"clone_pcm_button")
        self.clone_pcm_button.setGeometry(QRect(240, 430, 75, 23))
        self.clone_pcm_button.setMouseTracking(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget_3 = QTableWidget(self.tab_3)
        if (self.tableWidget_3.columnCount() < 10):
            self.tableWidget_3.setColumnCount(10)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem35)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 10, 711, 411))
        self.tableWidget_3.setAutoScroll(True)
        self.add_con_button = QPushButton(self.tab_3)
        self.add_con_button.setObjectName(u"add_con_button")
        self.add_con_button.setGeometry(QRect(120, 430, 75, 23))
        self.add_con_button.setMouseTracking(True)
        self.clone_con_button = QPushButton(self.tab_3)
        self.clone_con_button.setObjectName(u"clone_con_button")
        self.clone_con_button.setGeometry(QRect(240, 430, 75, 23))
        self.clone_con_button.setMouseTracking(True)
        self.update_con_button = QPushButton(self.tab_3)
        self.update_con_button.setObjectName(u"update_con_button")
        self.update_con_button.setGeometry(QRect(360, 430, 75, 23))
        self.update_con_button.setMouseTracking(True)
        self.remove_con_button = QPushButton(self.tab_3)
        self.remove_con_button.setObjectName(u"remove_con_button")
        self.remove_con_button.setGeometry(QRect(480, 430, 75, 23))
        self.remove_con_button.setMouseTracking(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableWidget_4 = QTableWidget(self.tab_4)
        if (self.tableWidget_4.columnCount() < 10):
            self.tableWidget_4.setColumnCount(10)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem45)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(10, 10, 711, 411))
        self.remove_ins_button = QPushButton(self.tab_4)
        self.remove_ins_button.setObjectName(u"remove_ins_button")
        self.remove_ins_button.setGeometry(QRect(480, 430, 75, 23))
        self.remove_ins_button.setMouseTracking(True)
        self.add_ins_button = QPushButton(self.tab_4)
        self.add_ins_button.setObjectName(u"add_ins_button")
        self.add_ins_button.setGeometry(QRect(120, 430, 75, 23))
        self.add_ins_button.setMouseTracking(True)
        self.update_ins_button = QPushButton(self.tab_4)
        self.update_ins_button.setObjectName(u"update_ins_button")
        self.update_ins_button.setGeometry(QRect(360, 430, 75, 23))
        self.update_ins_button.setMouseTracking(True)
        self.clone_ins_button = QPushButton(self.tab_4)
        self.clone_ins_button.setObjectName(u"clone_ins_button")
        self.clone_ins_button.setGeometry(QRect(240, 430, 75, 23))
        self.clone_ins_button.setMouseTracking(True)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tableWidget_5 = QTableWidget(self.tab_5)
        if (self.tableWidget_5.columnCount() < 10):
            self.tableWidget_5.setColumnCount(10)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, __qtablewidgetitem55)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(10, 10, 711, 411))
        self.remove_sem_button = QPushButton(self.tab_5)
        self.remove_sem_button.setObjectName(u"remove_sem_button")
        self.remove_sem_button.setGeometry(QRect(480, 430, 75, 23))
        self.remove_sem_button.setMouseTracking(True)
        self.add_sem_button = QPushButton(self.tab_5)
        self.add_sem_button.setObjectName(u"add_sem_button")
        self.add_sem_button.setGeometry(QRect(120, 430, 75, 23))
        self.add_sem_button.setMouseTracking(True)
        self.update_sem_button = QPushButton(self.tab_5)
        self.update_sem_button.setObjectName(u"update_sem_button")
        self.update_sem_button.setGeometry(QRect(360, 430, 75, 23))
        self.update_sem_button.setMouseTracking(True)
        self.clone_sem_button = QPushButton(self.tab_5)
        self.clone_sem_button.setObjectName(u"clone_sem_button")
        self.clone_sem_button.setGeometry(QRect(240, 430, 75, 23))
        self.clone_sem_button.setMouseTracking(True)
        self.tabWidget.addTab(self.tab_5, "")
        MDKWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDKWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MDKWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MDKWindow)
        self.statusbar.setObjectName(u"statusbar")
        MDKWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QDockWidget(MDKWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setMinimumSize(QSize(170, 189))
        self.dockWidget_2.setMaximumSize(QSize(170, 500))
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolBox = QToolBox(self.dockWidgetContents_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 152, 407))
        self.comboBox = QComboBox(self.page_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 0, 131, 22))
        self.SearchItem = QLineEdit(self.page_2)
        self.SearchItem.setObjectName(u"SearchItem")
        self.SearchItem.setGeometry(QRect(10, 30, 113, 20))
        self.search_button = QPushButton(self.page_2)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(20, 60, 75, 23))
        self.search_button.setMouseTracking(True)
        self.sort_button = QPushButton(self.page_2)
        self.sort_button.setObjectName(u"sort_button")
        self.sort_button.setGeometry(QRect(20, 90, 75, 23))
        self.sort_button.setMouseTracking(True)
        self.toolBox.addItem(self.page_2, u"Search Material")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.load_default_button = QPushButton(self.dockWidgetContents_2)
        self.load_default_button.setObjectName(u"load_default_button")
        self.load_default_button.setMouseTracking(True)

        self.gridLayout.addWidget(self.load_default_button, 1, 0, 1, 1)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MDKWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionImport_2)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuHelp.addAction(self.actionOpen_explanation)

        self.retranslateUi(MDKWindow)

        self.tabWidget.setCurrentIndex(4)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MDKWindow)
    # setupUi

    def retranslateUi(self, MDKWindow):
        MDKWindow.setWindowTitle(QCoreApplication.translate("MDKWindow", u"PowerSynth MDK Window", None))
        self.actionImport.setText(QCoreApplication.translate("MDKWindow", u"Import", None))
        self.actionSave.setText(QCoreApplication.translate("MDKWindow", u"Export", None))
        self.actionImport_file.setText(QCoreApplication.translate("MDKWindow", u"Import File", None))
        self.actionType_Material.setText(QCoreApplication.translate("MDKWindow", u"Type Material", None))
        self.actionImport_2.setText(QCoreApplication.translate("MDKWindow", u"Import", None))
        self.actionOpen_explanation.setText(QCoreApplication.translate("MDKWindow", u"Open explanation", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MDKWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MDKWindow", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MDKWindow", u"Young Modulus", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MDKWindow", u"Poisson's Ratio", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MDKWindow", u"Melting Temperature", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MDKWindow", u"Density(Solid)", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MDKWindow", u"Density(Liquid)", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity(Solid)", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity(Liquid)", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity (Solid)", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity (Liquid)", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MDKWindow", u"Electrical Resistivity", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MDKWindow", u"Relative permittivity", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MDKWindow", u"Relative Permeability", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MDKWindow", u"CTE", None));
#if QT_CONFIG(tooltip)
        self.remove_all_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Chosen material is removed from the table", None))
#endif // QT_CONFIG(tooltip)
        self.remove_all_button.setText(QCoreApplication.translate("MDKWindow", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.add_all_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Add blank line to below of the table", None))
#endif // QT_CONFIG(tooltip)
        self.add_all_button.setText(QCoreApplication.translate("MDKWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.update_all_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Changed values are updated", None))
#endif // QT_CONFIG(tooltip)
        self.update_all_button.setText(QCoreApplication.translate("MDKWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.clone_all_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Make clone material and show it top of the table", None))
#endif // QT_CONFIG(tooltip)
        self.clone_all_button.setText(QCoreApplication.translate("MDKWindow", u"Clone", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MDKWindow", u"ALL", None))
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MDKWindow", u"Name", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MDKWindow", u"Young Modulus", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MDKWindow", u"Poisson's Ratio", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MDKWindow", u"CTE", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MDKWindow", u"Melting Temperature", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MDKWindow", u"Density(Solid)", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MDKWindow", u"Density(Liquid)", None));
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity (Solid)", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity (Liquid)", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity (Solid)", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity (Liquid)", None));
#if QT_CONFIG(tooltip)
        self.remove_pcm_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Chosen material is removed from the table", None))
#endif // QT_CONFIG(tooltip)
        self.remove_pcm_button.setText(QCoreApplication.translate("MDKWindow", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.add_pcm_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Add blank line to below of the table", None))
#endif // QT_CONFIG(tooltip)
        self.add_pcm_button.setText(QCoreApplication.translate("MDKWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.update_pcm_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Changed values are updated", None))
#endif // QT_CONFIG(tooltip)
        self.update_pcm_button.setText(QCoreApplication.translate("MDKWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.clone_pcm_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Make clone material and show it top of the table", None))
#endif // QT_CONFIG(tooltip)
        self.clone_pcm_button.setText(QCoreApplication.translate("MDKWindow", u"Clone", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MDKWindow", u"PCM", None))
        ___qtablewidgetitem26 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MDKWindow", u"Name", None));
        ___qtablewidgetitem27 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MDKWindow", u"Young Modulus", None));
        ___qtablewidgetitem28 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MDKWindow", u"Poisson's Ratio", None));
        ___qtablewidgetitem29 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MDKWindow", u"Density", None));
        ___qtablewidgetitem30 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity", None));
        ___qtablewidgetitem31 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity", None));
        ___qtablewidgetitem32 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MDKWindow", u"Electrical Resistivity", None));
        ___qtablewidgetitem33 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MDKWindow", u"Relative Permittivity", None));
        ___qtablewidgetitem34 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MDKWindow", u"Relative permeability", None));
        ___qtablewidgetitem35 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MDKWindow", u"CTE", None));
#if QT_CONFIG(tooltip)
        self.add_con_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Add blank line to below of the table", None))
#endif // QT_CONFIG(tooltip)
        self.add_con_button.setText(QCoreApplication.translate("MDKWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.clone_con_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Make clone material and show it top of the table", None))
#endif // QT_CONFIG(tooltip)
        self.clone_con_button.setText(QCoreApplication.translate("MDKWindow", u"Clone", None))
#if QT_CONFIG(tooltip)
        self.update_con_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Changed values are updated", None))
#endif // QT_CONFIG(tooltip)
        self.update_con_button.setText(QCoreApplication.translate("MDKWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.remove_con_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Chosen material is removed from the table", None))
#endif // QT_CONFIG(tooltip)
        self.remove_con_button.setText(QCoreApplication.translate("MDKWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MDKWindow", u"Conductor", None))
        ___qtablewidgetitem36 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MDKWindow", u"Name", None));
        ___qtablewidgetitem37 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MDKWindow", u"Young Modulus", None));
        ___qtablewidgetitem38 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MDKWindow", u"Poisson's Ratio", None));
        ___qtablewidgetitem39 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MDKWindow", u"Density", None));
        ___qtablewidgetitem40 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity", None));
        ___qtablewidgetitem41 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity", None));
        ___qtablewidgetitem42 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MDKWindow", u"Electrical Resistivity", None));
        ___qtablewidgetitem43 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MDKWindow", u"Relative Permittivity", None));
        ___qtablewidgetitem44 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MDKWindow", u"Relative Permeability", None));
        ___qtablewidgetitem45 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MDKWindow", u"CTE", None));
#if QT_CONFIG(tooltip)
        self.remove_ins_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Chosen material is removed from the table", None))
#endif // QT_CONFIG(tooltip)
        self.remove_ins_button.setText(QCoreApplication.translate("MDKWindow", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.add_ins_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Add blank line to below of the table", None))
#endif // QT_CONFIG(tooltip)
        self.add_ins_button.setText(QCoreApplication.translate("MDKWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.update_ins_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Changed values are updated", None))
#endif // QT_CONFIG(tooltip)
        self.update_ins_button.setText(QCoreApplication.translate("MDKWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.clone_ins_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Make clone material and show it top of the table", None))
#endif // QT_CONFIG(tooltip)
        self.clone_ins_button.setText(QCoreApplication.translate("MDKWindow", u"Clone", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MDKWindow", u"Insulator", None))
        ___qtablewidgetitem46 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MDKWindow", u"Name", None));
        ___qtablewidgetitem47 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MDKWindow", u"Young Modulus", None));
        ___qtablewidgetitem48 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MDKWindow", u"Poisson's Ratio", None));
        ___qtablewidgetitem49 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MDKWindow", u"Density", None));
        ___qtablewidgetitem50 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MDKWindow", u"Thermal Conductivity", None));
        ___qtablewidgetitem51 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity", None));
        ___qtablewidgetitem52 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MDKWindow", u"Electrical Resistivity", None));
        ___qtablewidgetitem53 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MDKWindow", u"Relative Permittivity", None));
        ___qtablewidgetitem54 = self.tableWidget_5.horizontalHeaderItem(8)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MDKWindow", u"Relative Permeability", None));
        ___qtablewidgetitem55 = self.tableWidget_5.horizontalHeaderItem(9)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MDKWindow", u"CTE", None));
#if QT_CONFIG(tooltip)
        self.remove_sem_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Chosen material is removed from the table", None))
#endif // QT_CONFIG(tooltip)
        self.remove_sem_button.setText(QCoreApplication.translate("MDKWindow", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.add_sem_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Add blank line to below of the table", None))
#endif // QT_CONFIG(tooltip)
        self.add_sem_button.setText(QCoreApplication.translate("MDKWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.update_sem_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Changed values are updated", None))
#endif // QT_CONFIG(tooltip)
        self.update_sem_button.setText(QCoreApplication.translate("MDKWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.clone_sem_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Make clone material and show it top of the table", None))
#endif // QT_CONFIG(tooltip)
        self.clone_sem_button.setText(QCoreApplication.translate("MDKWindow", u"Clone", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MDKWindow", u"Semiconductor", None))
        self.menuFile.setTitle(QCoreApplication.translate("MDKWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MDKWindow", u"Help", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MDKWindow", u"Name", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MDKWindow", u"Young Modulus", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MDKWindow", u"Poisson's Ratio", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MDKWindow", u"Melting Temperature", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MDKWindow", u"Electrical Resistivity", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MDKWindow", u"Density", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MDKWindow", u"Density(Solid)", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MDKWindow", u"Density(Liquid)", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity (Solid)", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MDKWindow", u"Specific Heat Capacity (Liquid)", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MDKWindow", u"Thermal Conductivity", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MDKWindow", u"Thermal Conductivity (Solid)", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MDKWindow", u"Thermal Conductivity (Liquid)", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MDKWindow", u"Relative Permittivity", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MDKWindow", u"Relative Permeability", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MDKWindow", u"CTE", None))

#if QT_CONFIG(tooltip)
        self.search_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Search specific material, and it show the top of the table", None))
#endif // QT_CONFIG(tooltip)
        self.search_button.setText(QCoreApplication.translate("MDKWindow", u"Search", None))
#if QT_CONFIG(tooltip)
        self.sort_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Sort materials based on the field", None))
#endif // QT_CONFIG(tooltip)
        self.sort_button.setText(QCoreApplication.translate("MDKWindow", u"Sort", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MDKWindow", u"Search Material", None))
#if QT_CONFIG(tooltip)
        self.load_default_button.setToolTip(QCoreApplication.translate("MDKWindow", u"Open MDK file and upload it to the table", None))
#endif // QT_CONFIG(tooltip)
        self.load_default_button.setText(QCoreApplication.translate("MDKWindow", u"Load Default", None))
    # retranslateUi
