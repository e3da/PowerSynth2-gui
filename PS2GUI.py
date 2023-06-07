#!/usr/bin/env python
# This is the QT-based frontend for PowerSynth2

import sys
import os
import csv
import webbrowser
import traceback
from PySide2 import QtWidgets
from matplotlib.figure import Figure
from core.PSCore import PSEnv
from core.PS2CLI import PS2CLI
from gui.qt.py.openingWindow import Ui_Dialog as UI_opening_window
from gui.qt.py.runMacro import Ui_Dialog as UI_run_macro
from gui.qt.py.editLayout import Ui_Dialog as UI_edit_layout
from gui.qt.py.layerStack import Ui_Dialog as UI_layer_stack
from gui.qt.py.editConstraints import Ui_Dialog as UI_edit_constraints
from gui.core.MDKEditor import EditLibrary
from gui.core.generateLayout import generateLayout
from gui.qt.py.optimizationSetup import Ui_Dialog as UI_optimization_setup
from gui.qt.py.electricalSetup import Ui_Dialog as UI_electrical_setup
from gui.qt.py.thermalSetup import Ui_Dialog as UI_thermal_setup
from gui.qt.py.runOptions import Ui_Dialog as UI_run_options
from gui.core.solutionBrowser import showSolutionBrowser
from gui.core.createMacro import createMacro

class PS2GUI():
    '''GUI Class -- Stores Important Information for the GUI'''

    def __init__(self):
        self.core = PSEnv()

        self.app = None
        self.currentWindow = None
        self.pathToWorkFolder = None
        self.pathToLayoutScript = None
        self.pathToBondwireSetup = None
        self.pathToLayerStack = None
        self.pathToConstraints = None
        self.pathToParasiticModel = ""
        self.pathToTraceOri = ""
        self.pathToFigs = ""
        self.pathToSolutions = ""
        self.option = None
        self.optimizationUI = None
        self.extraConstraints = []
        self.setupsDone = [0, 0]
        self.device_dict = None
        self.lead_list = None
        self.solution_ind = None
        self.macro_script_path = None

        # Variables for Layout Generation Setup
        self.reliabilityAwareness = ""
        self.plotSolution = ""
        self.layoutMode = "0"
        self.floorPlan = ["", ""]
        self.numLayouts = "1"
        self.seed = "10"
        self.optimizationAlgorithm = "NG-RANDOM"
        self.numGenerations = "10"

        # Variables for Electrical Setup
        self.modelType = ""
        self.measureNameElectrical = ""
        self.measureType = ""
        self.deviceConnection = dict()
        self.source = ""
        self.sink = ""
        self.frequency = ""

        # Variables for Thermal Setup
        self.modelSelect = ""
        self.measureNameThermal = ""
        self.devicePower = dict()
        self.heatConvection = ""
        self.ambientTemperature = ""

    
    def RunPSCLI(self):
        try:
            self.core = PS2CLI(self.macro_script_path)
            self.core.run()
            showSolutionBrowser(self)
            return 0
        except:
            traceback.print_exc()
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle("Error:")
            popup.setText("PowerSynth excution failed :(. Plesae check your macro file.")
            popup.exec_()
        return 1

    def setWindow(self, newWindow):
        if self.currentWindow:
            self.currentWindow.close()
        self.currentWindow = newWindow

    def openingWindow(self):
        '''Function to create the main opening window and start to GUI'''
        openingWindow = QtWidgets.QDialog()
        ui = UI_opening_window()
        ui.setupUi(openingWindow)
        self.setWindow(openingWindow)

        def manual():
            #webbrowser.open_new("./GUI/pdfs/PowerSynth_v1.9.pdf") 
            try: 
                webbrowser.open_new("https://e3da.csce.uark.edu/release/PowerSynth/manual/PowerSynth_v2.0.pdf")
            except:
                print("Failed to open manual! Please look inside the package for PowerSynth_v2.0.pdf")
        
        def web():
            try: 
                webbrowser.open_new("https://e3da.csce.uark.edu/release/PowerSynth/")
            except:
                print("Failed to open website! Please open e3da.csce.uark.edu in your browser.")

        def create_macro():
            self.editLayout()

        def run_macro():
            self.runMacro()

        ui.open_manual.clicked.connect(manual)
        ui.open_web.clicked.connect(web)
        ui.create_macro.clicked.connect(create_macro)
        ui.run_macro.clicked.connect(run_macro)

        ui.open_manual.setToolTip("Opens the user manual for PowerSynth in default browser.")
        ui.open_web.setToolTip("Opens the Release Website for PowerSynth in default browser.")
        ui.create_macro.setToolTip("Create a new macro file.")
        ui.run_macro.setToolTip("Run a PowerSynth backend on the macro script.")

        openingWindow.show()

    def runMacro(self):
        '''Opens Window to directly run PowerSynth
           User must provide paths to macro_script.txt
        '''
        runMacro = QtWidgets.QDialog()
        ui = UI_run_macro()
        ui.setupUi(runMacro)
        self.setWindow(runMacro)

        def getMacroScript():
            if self.macro_script_path==None:
                ui.lineEdit_4.setText(QtWidgets.QFileDialog.getOpenFileName(runMacro, 'Open macro_script.txt', os.getcwd())[0])
            else:
                ui.lineEdit_4.setText(self.macro_script_path)
                self.currentWindow.close()
                return

        def runPowerSynth():
            
            if not os.path.exists(ui.lineEdit_4.text()) or not ui.lineEdit_4.text().endswith(".txt"):
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle("Error:")
                popup.setText("Please enter a valid path to the macro_script file.")
                popup.exec_()
                return

            self.macro_script_path = ui.lineEdit_4.text()

            self.currentWindow.close()
            self.currentWindow = None
            
            self.pathToWorkFolder=os.path.dirname(self.macro_script_path)
            os.chdir(self.pathToWorkFolder)         

            with open(self.macro_script_path, 'r') as file:
                for line in file:
                    if line.startswith("Constraint_file: "):
                        self.pathToConstraints = os.path.abspath(line.split()[1])

                    if line.startswith("Fig_dir: "):
                        self.pathToFigs = os.path.abspath(line.split()[1])

                    if line.startswith("Solution_dir: "):
                        self.pathToSolutions = os.path.abspath(line.split()[1])

                    if line.startswith("Option: "):
                        self.option = int(line.split()[1])
                    if line.startswith("Reliability-awareness: "):
                        self.reliabilityAwareness = int(line.split()[1])
                    if line.startswith("Floor_plan: "):
                        self.floorPlan[0] = line.split()[1].split(",")[0]
                        self.floorPlan[1] = line.split()[1].split(",")[1]
                    if line.startswith("Layout_Mode: "):
                        self.layoutMode = line.split()[1]

            self.RunPSCLI()

        ui.btn_create_project.clicked.connect(runPowerSynth)
        ui.btn_cancel.clicked.connect(self.openingWindow)
        ui.btn_open_macro.clicked.connect(getMacroScript)

        ui.btn_cancel.setToolTip("Return to opening window.")
        ui.btn_create_project.setToolTip("Click once you have entered correct paths.")
        ui.btn_open_macro.setToolTip("Open file explorer for macro_script.txt file.")

        runMacro.show()

    def editLayout(self):
        '''User Enters the Paths to Layer Stack, Bondwire Setup, Layout Script with this window'''
        editLayout = QtWidgets.QDialog()
        ui = UI_edit_layout()
        ui.setupUi(editLayout)
        self.setWindow(editLayout)

        def getLayerStack():
            ui.lineEdit_layer.setText(QtWidgets.QFileDialog.getOpenFileName(editLayout, 'Open layer_stack')[0])

        def getLayoutScript():
            ui.lineEdit_layout.setText(QtWidgets.QFileDialog.getOpenFileName(editLayout, 'Open layout_script')[0])

        def getBondwire():
            ui.lineEdit_bondwire.setText(QtWidgets.QFileDialog.getOpenFileName(editLayout, 'Open Connectivity_script')[0])

        def createLayout():

            #'''
            if not os.path.exists(ui.lineEdit_layer.text()) or not ui.lineEdit_layer.text().endswith(".csv"):
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle("Error:")
                popup.setText("Please enter a valid path to the layer_stack file.")
                popup.exec_()
                return

            if not os.path.exists(ui.lineEdit_layout.text()) or not ui.lineEdit_layout.text().endswith(".txt"):
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle("Error:")
                popup.setText("Please enter a valid path to the layout_script file.")
                popup.exec_()
                return
            
            if len(ui.lineEdit_bondwire.text()):
                if not os.path.exists(ui.lineEdit_bondwire.text()) or not ui.lineEdit_bondwire.text().endswith(".txt"):
                    
                        popup = QtWidgets.QMessageBox()
                        popup.setWindowTitle("Error:")
                        popup.setText("Please enter a valid path to the Connectivity_script file.")
                        popup.exec_()
                        return
            
            self.pathToLayerStack = ui.lineEdit_layer.text()
            self.pathToLayoutScript = ui.lineEdit_layout.text()
            self.pathToBondwireSetup = ui.lineEdit_bondwire.text()
			
            self.reliabilityAwareness = "0" if ui.combo_reliability_constraints.currentText() == "no constraint" else "1" if ui.combo_reliability_constraints.currentText() == "worst case" else "2"

            self.pathToWorkFolder = os.path.dirname(self.pathToLayoutScript)
            os.chdir(self.pathToWorkFolder)

            #default paths are relative to work folder
            self.pathToConstraints = "./constraint.csv"
            self.pathToFigs = "./Figs"
            self.pathToSolutions = "./Solutions"

            self.device_dict, self.lead_list = generateLayout(self.pathToLayoutScript, self.pathToBondwireSetup, self.pathToLayerStack, self.pathToConstraints, int(self.reliabilityAwareness))

            self.displayLayerStack()

        def openMDK():
            ui=EditLibrary(self.currentWindow,self.core.MatLib)
            ui.show()

        ui.btn_edit_materials.clicked.connect(openMDK)
        ui.btn_open_layer_stack.clicked.connect(getLayerStack)
        ui.btn_open_layout.clicked.connect(getLayoutScript)
        ui.btn_open_bondwire.clicked.connect(getBondwire)
        ui.btn_create_project.clicked.connect(createLayout)

        ui.btn_edit_materials.setToolTip("Open MDKEditor to create custom list of materials.")
        ui.btn_open_layer_stack.setToolTip("Open file explorer for layer_stack.csv file.")
        ui.btn_open_bondwire.setToolTip("Open file explorer for bondwire_setup.txt file.")
        ui.btn_open_layout.setToolTip("Open file explorer for layout_script.txt file.")
        ui.btn_create_project.setToolTip("Click once you have entered correct paths.")
        ui.default_mat_lib.setText(PSEnv.MatLib)

        editLayout.show()
    
    def displayLayerStack(self):
        '''Opens the layer stack file editor.'''
        displayLayerStack = QtWidgets.QDialog()
        ui = UI_layer_stack()
        ui.setupUi(displayLayerStack)
        self.setWindow(displayLayerStack)

        with open(self.pathToLayerStack, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)

            for i, row in enumerate(csvreader):
                if i:  # Skip the column headers
                    if i > 5:
                        ui.tableWidget.insertRow(i-1)
                    for j, val in enumerate(row):
                        if j:  # Skip the ID column
                            textedit = QtWidgets.QTableWidgetItem()
                            textedit.setText(val)
                            ui.tableWidget.setItem(i-1, j-1, textedit)
                            
                            if row[1][0]=='I':
                                self.floorPlan=[row[3],row[4]]

        def continue_UI():
            with open(self.pathToLayerStack, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)

                csvwriter.writerow(["ID", "Name" , "Origin" , "Width" , "Length" , "Thickness" , "Material" , "Type" , "Electrical"])

                for i in range(ui.tableWidget.rowCount()):
                    row = [i+1]
                    for j in range(ui.tableWidget.columnCount()):
                        if ui.tableWidget.item(i, j):
                            row.append(ui.tableWidget.item(i, j).text())
                    csvwriter.writerow(row)

            self.editConstraints()

        ui.btn_continue.clicked.connect(continue_UI)
        ui.btn_continue.setToolTip("Click to continue once you have edited the layer_stack file.")
        
        displayLayerStack.show()

    def editConstraints(self):
        '''Opens the constraint file editor.'''
        editConstraints = QtWidgets.QDialog()
        ui = UI_edit_constraints()
        ui.setupUi(editConstraints)
        self.setWindow(editConstraints)

        if int(self.reliabilityAwareness) == 0:
            ui.tabWidget.removeTab(5)


        print(f"INFO: Reading Constraints: {self.pathToConstraints}")
        # Fill out the constraints from the given constraint file
        with open(self.pathToConstraints, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)

            tableWidgets = [ui.tableWidget, ui.tableWidget_2, ui.tableWidget_3, ui.tableWidget_4, ui.tableWidget_5]
            k = -1
            DONE = False
            for row in csvreader:
                if DONE:  # Saves voltage specification and such
                    self.extraConstraints.append(row)
                    continue
                try:
                    float(row[-1])
                except ValueError:    # This is a header line
                    if k > 3:
                        self.extraConstraints.append(row)
                        DONE = True
                        continue
                    ui.tabWidget.setTabText(k+1, row[0])
                    for _ in range(len(row) - 5):
                        tableWidgets[k+1].insertColumn(tableWidgets[k+1].columnCount())
                    for header_index in range(len(row) - 1):
                        textedit = textedit = QtWidgets.QTableWidgetItem()
                        textedit.setText(row[header_index + 1])
                        tableWidgets[k+1].setHorizontalHeaderItem(header_index, textedit)
                    rowcount = 0
                    k += 1
                if rowcount + 1 > 5:
                    tableWidgets[k].insertRow(tableWidgets[k].rowCount())
                
                for j, val in enumerate(row):
                    textedit = QtWidgets.QTableWidgetItem()
                    textedit.setText(val)
                    if j:
                        tableWidgets[k].setItem(rowcount-1, j-1, textedit)
                    else:
                        tableWidgets[k].setVerticalHeaderItem(rowcount-1, textedit)
                rowcount += 1

        def continue_UI():
            
            with open(self.pathToConstraints, 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)

                    for k, tableWidget in enumerate([ui.tableWidget, ui.tableWidget_2, ui.tableWidget_3, ui.tableWidget_4, ui.tableWidget_5]):
                        l = [ui.tabWidget.tabText(k)]
                        for i in range(tableWidget.columnCount()):
                            l.append(tableWidget.horizontalHeaderItem(i).text())
                        csvwriter.writerow(l)
                        for i in range(tableWidget.rowCount()):
                            row = [tableWidget.verticalHeaderItem(i).text()]
                            for j in range(tableWidget.columnCount()):
                                row.append(tableWidget.item(i, j).text())
                            csvwriter.writerow(row)
                    for row in self.extraConstraints:
                        csvwriter.writerow(row)

            self.runOptions()

        ui.btn_continue.clicked.connect(continue_UI)
        ui.btn_continue.setToolTip("Click to continue once you have edited the constraints.")

        editConstraints.show()

    def runOptions(self):
        '''Opens Window for Run Options.  User chooses Option = 0,1,2 based on provided buttons.'''
        runOptions = QtWidgets.QDialog()
        ui = UI_run_options()
        ui.setupUi(runOptions)
        self.setWindow(runOptions)

        def option0():
            self.option = 0
            self.optimizationSetup()
        
        def option1():
            self.option = 1
            self.optimizationSetup()

        def option2():
            self.option = 2
            self.optimizationSetup()

        ui.pushButton.clicked.connect(option1)
        ui.pushButton_2.clicked.connect(option0)
        ui.pushButton_3.clicked.connect(option2)

        ui.pushButton.setToolTip("This option will bypass electrical/thermal evaluation.")
        ui.pushButton_2.setToolTip("This option will bypass layout evaluation.")
        ui.pushButton_3.setToolTip("This option will run both layout evaluation and electrical/thermal evaluation.")

        runOptions.show()

    def optimizationSetup(self):
        optimizationSetup = QtWidgets.QDialog()
        ui = UI_optimization_setup()
        self.optimizationUI = ui
        ui.setupUi(optimizationSetup)
        self.setWindow(optimizationSetup)
        optimizationSetup.setFixedHeight(410)
        optimizationSetup.setFixedWidth(400)
        ui.btn_run_powersynth.setEnabled(False)
        ui.seed.setText("0")

        def floorplan_assignment():
            if ui.combo_layout_mode.currentText() == "minimum-sized solutions" or ui.combo_layout_mode.currentText() == "variable-sized solutions":
                ui.floor_plan_x.setEnabled(False)
                ui.floor_plan_y.setEnabled(False)
                #ui.combo_optimization_algorithm.setEnabled(False)
                if ui.combo_layout_mode.currentText() == "minimum-sized solutions":
                    ui.num_layouts.setText("1")
                    ui.num_layouts.setEnabled(False)
                else:
                    ui.num_layouts.setEnabled(True)
        
                
            else:
                ui.floor_plan_x.setEnabled(True)
                ui.floor_plan_y.setEnabled(True)
                ui.num_layouts.setEnabled(True)

        if self.option == 1:
            #ui.btn_run_powersynth.setDisabled(True)
            ui.electrical_thermal_frame.show()
            ui.layout_generation_setup_frame.hide()
            optimizationSetup.setFixedHeight(205)
            ui.floor_plan_x.setText(self.floorPlan[0])
            ui.floor_plan_y.setText(self.floorPlan[1])
            ui.floor_plan_x.setEnabled(False)
            ui.floor_plan_y.setEnabled(False)
            ui.electrical_thermal_frame.show()
            ui.btn_run_powersynth.setEnabled(True)
        elif self.option == 0:
            optimizationSetup.setFixedHeight(350)
            ui.electrical_thermal_frame.hide()
            if ui.combo_layout_mode.currentText() == "minimum-sized solutions" or ui.combo_layout_mode.currentText() == "variable-sized solutions":
                ui.floor_plan_x.setEnabled(False)
                ui.floor_plan_y.setEnabled(False)
                ui.combo_optimization_algorithm.setEnabled(False)
                if ui.combo_layout_mode.currentText() == "minimum-sized solutions":
                    ui.num_layouts.setText("1")
                    ui.num_layouts.setEnabled(False)
                else:
                    ui.num_layouts.setEnabled(True)
            else:
                ui.num_layouts.setEnabled(True)
            ui.combo_layout_mode.currentIndexChanged.connect(floorplan_assignment)

            
            ui.combo_optimization_algorithm.setEnabled(False)
            ui.btn_run_powersynth.setEnabled(True)
        elif self.option == 2:
            if ui.combo_layout_mode.currentText() == "minimum-sized solutions" or ui.combo_layout_mode.currentText() == "variable-sized solutions":
                ui.floor_plan_x.setEnabled(False)
                ui.floor_plan_y.setEnabled(False)
                ui.combo_optimization_algorithm.setEnabled(False)
                if ui.combo_layout_mode.currentText() == "minimum-sized solutions":
                    ui.num_layouts.setText("1")
                    ui.num_layouts.setEnabled(False)
                else:
                    ui.num_layouts.setEnabled(True)
            else:
                ui.num_layouts.setEnabled(True)
                ui.combo_optimization_algorithm.setEnabled(True)
            ui.combo_layout_mode.currentIndexChanged.connect(floorplan_assignment)
            ui.btn_run_powersynth.setEnabled(True)

        
        def run():
            # SAVE VALUES HERE
            self.floorPlan[0] = ui.floor_plan_x.text()
            self.floorPlan[1] = ui.floor_plan_y.text()
            self.plotSolution = "1" if ui.checkbox_plot_solutions.isChecked() else "0"

            if self.option !=1:
                if ui.combo_layout_mode.currentText() == "minimum-sized solutions":
                    self.layoutMode = "0" 
                elif ui.combo_layout_mode.currentText() == "variable-sized solutions":
                    self.layoutMode = "1" 
                elif ui.combo_layout_mode.currentText() == "fixed-sized solutions":
                    self.layoutMode = "2" 
                
                self.numLayouts = ui.num_layouts.text()
                self.seed = ui.seed.text()
                self.optimizationAlgorithm = ui.combo_optimization_algorithm.currentText()
                self.numGenerations = ui.num_layouts.text()

            
            self.runPowerSynth()

        ui.btn_electrical_setup.clicked.connect(self.electricalSetup)
        ui.btn_thermal_setup.clicked.connect(self.thermalSetup)
        ui.btn_run_powersynth.clicked.connect(run)

        ui.btn_electrical_setup.setToolTip("Opens electrical setup in a separate window.")
        ui.btn_thermal_setup.setToolTip("Opens thermal setup in a separate window.")
        ui.btn_run_powersynth.setToolTip("Click to run PowerSynth once all setup options are entered correctly.")

        optimizationSetup.show()


    def electricalSetup(self):
        '''Creates window for the electrical setup'''
        electricalSetup = QtWidgets.QDialog(parent=self.currentWindow)
        ui = UI_electrical_setup()
        ui.setupUi(electricalSetup)

        def getParasiticModel():
            ui.parasitic_textedit.setText(QtWidgets.QFileDialog.getOpenFileName(electricalSetup, 'Open parasitic_model', os.getcwd())[0])

        def getTraceOri():
            ui.trace_textedit.setText(QtWidgets.QFileDialog.getOpenFileName(electricalSetup, 'Open trace_orientation', os.getcwd())[0])

        def continue_UI():
            # SAVE VALUES HERE
            self.modelType = ui.combo_model_type.currentText()
            self.measureNameElectrical = ui.lineedit_measure_name.text()
            if ui.combo_measure_type.currentText() == "inductance":
                self.measureType = "0"  
            elif ui.combo_measure_type.currentText() == "resistance":
                self.measureType = "1"
            elif ui.combo_measure_type.currentText() == "capacitance":
                self.measureType = "2"
            
            for i in range(ui.tableWidget.rowCount()):
                try:
                    self.deviceConnection[ui.tableWidget.cellWidget(i, 0).currentText()] = ui.tableWidget.cellWidget(i, 1).currentText()
                except AttributeError:
                    print("Error: Please specify a name for each device.")
            
            self.source = ui.combo_source.currentText()
            self.sink = ui.combo_sink.currentText()
            self.frequency = ui.frequency.text()

            self.pathToParasiticModel = ui.parasitic_textedit.text()
            self.pathToTraceOri = ui.trace_textedit.text()

            self.setupsDone[0] += 1
            if self.setupsDone[0] > 0 and self.setupsDone[1] > 0:
                self.optimizationUI.btn_run_powersynth.setDisabled(False)

            electricalSetup.close()

        def addAll():
            for i in range(len(self.device_dict) - ui.tableWidget.rowCount()):
                addRow()           

        def addRow():
            index = ui.tableWidget.rowCount()
            ui.tableWidget.insertRow(index)
            combo = QtWidgets.QComboBox()
            for device in self.device_dict.keys():
                combo.addItem(str(device))
            ui.tableWidget.setCellWidget(index, 0, combo)
            combo.setCurrentIndex(index if index<len(self.device_dict) else 0)

            combo2 = QtWidgets.QComboBox()
            for path in self.device_dict[combo.currentText()]:
                combo2.addItem(path[0] + " to " + path[1])
            ui.tableWidget.setCellWidget(index, 1, combo2)

            def adjustPaths():
                combo2 = QtWidgets.QComboBox()
                for path in self.device_dict[combo.currentText()]:
                    combo2.addItem(path[0] + " to " + path[1])
                ui.tableWidget.setCellWidget(index, 1, combo2)

            combo.currentIndexChanged.connect(adjustPaths)

        def removeRow():
            if ui.tableWidget.rowCount() > 0:
                ui.tableWidget.removeRow(ui.tableWidget.rowCount() - 1)

        
        ui.btn_open_parasitic.clicked.connect(getParasiticModel)
        ui.btn_open_trace.clicked.connect(getTraceOri)
        ui.btn_continue.clicked.connect(continue_UI)
        ui.btn_add_device.clicked.connect(addRow)
        ui.btn_add_all.clicked.connect(addAll)
        ui.btn_remove_device.clicked.connect(removeRow)

        ui.btn_open_parasitic.setToolTip("Open file explorer for parasitic_model.rsmdl file.")
        ui.btn_open_trace.setToolTip("Open file explorer for trace_ori.txt file.")
        ui.btn_continue.setToolTip("Save values for electrical setup.  Only click once electrical setup is complete.")
        ui.btn_add_device.setToolTip("Add a row to device connection table.")
        ui.btn_remove_device.setToolTip("Remove the last row of the device connection table.")

        def show_parasitic_path():
            if ui.combo_model_type.currentText() == "PEEC":
                ui.parasitic_model_frame.show()
            else:
                ui.parasitic_model_frame.hide()
        
        ui.parasitic_model_frame.hide()
        ui.parasitic_model_frame.setFrameStyle(0)
        ui.combo_model_type.currentIndexChanged.connect(show_parasitic_path)

        for lead in self.lead_list:
            ui.combo_source.addItem(lead)
            ui.combo_sink.addItem(lead)

        electricalSetup.show()

    def thermalSetup(self):
        '''Creates window for the thermal setup'''
        thermalSetup = QtWidgets.QDialog(parent=self.currentWindow)
        ui = UI_thermal_setup()
        ui.setupUi(thermalSetup)
        ui.combo_model_select.setEnabled(False)

        def continue_UI():
            # SAVE VALUES HERE
            #self.modelSelect = "0"  if ui.combo_model_select.currentText() == "TSFM" else "1" if ui.combo_model_select.currentText() == "Analytical" else "2"
            #ui.combo_model_select.setCurrentText= "ParaPower" 
            ui.combo_model_select.setEnabled(False)
            self.modelSelect="2" #default to ParaPower
            self.measureNameThermal = ui.lineedit_measure_name.text()

            for i in range(ui.tableWidget.rowCount()):
                try:
                    self.devicePower[ui.tableWidget.cellWidget(i, 0).currentText()] = ui.tableWidget.cellWidget(i, 1).text()
                except AttributeError:
                    print("Error: Please specify a name for each device.")

            self.heatConvection = ui.heat_convection.text()
            self.ambientTemperature = ui.ambient_temperature.text()

            self.setupsDone[1] += 1
            if self.setupsDone[0] > 0 and self.setupsDone[1] > 0:
                self.optimizationUI.btn_run_powersynth.setDisabled(False)

            thermalSetup.close()

        def addAll():
            for i in range(len(self.device_dict) - ui.tableWidget.rowCount()):
                addRow()           

        def addRow():
            index = ui.tableWidget.rowCount()
            ui.tableWidget.insertRow(index)
            combo = QtWidgets.QComboBox()
            for device in self.device_dict.keys():
                combo.addItem(str(device))
            combo.setCurrentIndex(index if index<len(self.device_dict) else 0)
            ui.tableWidget.setCellWidget(index, 0, combo)
            spinbox = QtWidgets.QDoubleSpinBox()
            spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # Removes buttons
            spinbox.setValue(10)
            spinbox.setMaximum(10000)
            ui.tableWidget.setCellWidget(index, 1, spinbox)

        def removeRow():
            if ui.tableWidget.rowCount() > 0:
                ui.tableWidget.removeRow(ui.tableWidget.rowCount() - 1)

        ui.btn_continue.clicked.connect(continue_UI)
        ui.btn_add_all.clicked.connect(addAll)
        ui.btn_add_device.clicked.connect(addRow)
        ui.btn_remove_device.clicked.connect(removeRow)

        ui.btn_continue.setToolTip("Save values for thermal setup.  Only click once thermal setup is complete.")
        ui.btn_add_device.setToolTip("Add a row to device power table.")
        ui.btn_remove_device.setToolTip("Remove the last row of the device power table.")

        thermalSetup.show()

        #self.currentWindow.close()
        #self.currentWindow = None
    def runPowerSynth(self):

        self.currentWindow.close()
        self.currentWindow = None

        self.pathToWorkFolder = os.path.dirname(self.pathToLayoutScript)
        self.macro_script_path = os.path.join(self.pathToWorkFolder, "macro_script.txt")

        with open(self.macro_script_path, "w") as file:
            createMacro(file, self)

        self.RunPSCLI()

    def run(self):
        '''Main Function to run the GUI'''

        self.app = QtWidgets.QApplication(sys.argv)

        self.openingWindow()

        self.app.exec_()


if __name__ == "__main__":  

    print("----------------------PowerSynth Version 2.0: GUI version------------------")
    application = PS2GUI()
    application.run()

