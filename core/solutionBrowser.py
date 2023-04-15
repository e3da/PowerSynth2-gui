import os
from PySide2 import QtCore, QtGui, QtWidgets

import matplotlib

matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from gui.qt.py.solutionBrowser import Ui_CornerStitch_Dialog as UI_solution_browser
from core.CmdRun.cmd_layout_handler import export_solution_layout_attributes
import matplotlib.pyplot as plt



def showSolutionBrowser(gui):
        '''Function to Run the Solution Browser.  Final step of the main flow.'''
        solutionBrowser = QtWidgets.QDialog()
        ui = UI_solution_browser()
        ui.setupUi(solutionBrowser)
        gui.setWindow(solutionBrowser)

        ui.lineEdit_size_w.setReadOnly(True)
        ui.lineEdit_size_h.setReadOnly(True)
        ui.lineEdit_x.setReadOnly(True)
        ui.lineEdit_y.setReadOnly(True)

        i = 1
        
        while os.path.exists(os.path.join(gui.pathToFigs, f"initial_layout_I{i}.png")):
            graphics = QtWidgets.QGraphicsView()

            ui.tabWidget.insertTab(i-1, graphics, f"Layer {i}")
            i += 1
        
        if i > 2:
            graphics = QtWidgets.QGraphicsView()
            ui.tabWidget.insertTab(i-1, graphics, "All Layers")

        # Solutions Graph
        #gui.core.cmd.solutionsFigure.set_size_inches(5, 4)
        axes = gui.core.cmd.solutionsFigure.gca()
        axes.set_title("Solution Space")
        #fig=Figure()
        #ax=fig.add_subplot(111)
        #canvas_sol_browser = FigureCanvas(fig)

        data_x=[]
        data_y=[]
        perf_metrices=[]
        if gui.option:
            for sol in gui.core.cmd.structure_3D.solutions:
                for key in sol.parameters:
                    perf_metrices.append(key)
            if len(perf_metrices)>1:
                axes.set_xlabel(perf_metrices[0])
                axes.set_ylabel(perf_metrices[1])
            else:
                axes.set_xlabel(perf_metrices[0])
        else:
            axes.set_xlabel("Solution Index")
            axes.set_ylabel("Solution Index")

        for sol in gui.core.cmd.structure_3D.solutions:
            if gui.option == 0:
                data_x.append(sol.solution_id)
                data_y.append(sol.solution_id)
            else:
                data_x.append(sol.parameters[perf_metrices[0]])
                if (len(sol.parameters)>1):
                    data_y.append(sol.parameters[perf_metrices[1]])
                else:
                    data_y.append(sol.solution_id)

        
        def on_pick(event):
            gui.solution_ind = event.ind[0]
            sel_point = gui.solution_ind
            #axes.clear()
            #axes.scatter(data_x, data_y, picker=1, marker='o', c='b',s = 50)
            axes.scatter(data_x[sel_point], data_y[sel_point], picker=1, marker='o', c='r',s=100)
            canvas.draw()

            i = 1
            if gui.option==1:
                display_initial_layout()
            else:
                while os.path.exists(os.path.join(gui.pathToFigs, f"Mode_{gui.layoutMode}/layout_{event.ind[0]}_I{i}.png")):
                    pix = QtGui.QPixmap(os.path.join(gui.pathToFigs, f"Mode_{gui.layoutMode}/layout_{event.ind[0]}_I{i}.png"))
                    #pix = pix.scaledToWidth(500)
                    item = QtWidgets.QGraphicsPixmapItem(pix)
                    scene = QtWidgets.QGraphicsScene()
                    scene.addItem(item)
                    ui.tabWidget.widget(i-1).setScene(scene)
                    i += 1
                if i > 2:
                    pix = QtGui.QPixmap(os.path.join(gui.pathToFigs, f"Mode_{gui.layoutMode}/layout_all_layers_{event.ind[0]}.png"))
                    #pix = pix.scaledToWidth(500)
                    item = QtWidgets.QGraphicsPixmapItem(pix)
                    scene = QtWidgets.QGraphicsScene()
                    scene.addItem(item)
                    ui.tabWidget.widget(i-1).setScene(scene)

            solution = gui.core.cmd.structure_3D.solutions[gui.solution_ind]
            
            for feature in solution.features_list:
                if 'Ceramic' in feature.name:
                    ui.lineEdit_size_w.setText(str(feature.width))
                    
                    ui.lineEdit_size_h.setText(str(feature.length))
                    
                    break
            ui.lineEdit_size_w.setEnabled(False)
            ui.lineEdit_size_h.setEnabled(False)

            ui.lineEdit_x.setText(str(round(float(event.artist.get_offsets()[event.ind][0][0]), 3)))
            ui.lineEdit_y.setText(str(round(float(event.artist.get_offsets()[event.ind][0][1]), 3)))
            ui.lineEdit_x.setEnabled(False)
            ui.lineEdit_y.setEnabled(False)


        def display_initial_layout():
            i = 1
            while os.path.exists(os.path.join(gui.pathToFigs, f"initial_layout_I{i}.png")):
                pix = QtGui.QPixmap(os.path.join(gui.pathToFigs, f"initial_layout_I{i}.png"))
                #pix = pix.scaledToWidth(575)
                item = QtWidgets.QGraphicsPixmapItem(pix)
                scene = QtWidgets.QGraphicsScene()
                scene.addItem(item)
                ui.tabWidget.widget(i-1).setScene(scene)
                i += 1
            if i > 2:
                pix = QtGui.QPixmap(os.path.join(gui.pathToFigs, f"initial_layout_all_layers.png"))
                #pix = pix.scaledToWidth(650)
                item = QtWidgets.QGraphicsPixmapItem(pix)
                scene = QtWidgets.QGraphicsScene()
                scene.addItem(item)
                ui.tabWidget.widget(i-1).setScene(scene)


        axes.scatter(data_x, data_y, picker=True)
        canvas = FigureCanvas(gui.core.cmd.solutionsFigure)
        canvas.draw()
        canvas.callbacks.connect('pick_event', on_pick)
        scene2 = QtWidgets.QGraphicsScene()
        scene2.addWidget(canvas)
        ui.grview_sols_browser.setScene(scene2)

        if gui.option:
            if len(perf_metrices)>1:
                ui.x_label.setText(perf_metrices[0])
                ui.y_label.setText(perf_metrices[1])
            else:
                ui.x_label.setText(perf_metrices[0])

            # FIXME Currently hardcoding the units.
            ui.label_units1.setText("nH")
            ui.label_units2.setText("K")
        else:
            ui.x_label.hide()
            ui.lineEdit_x.hide()
            ui.y_label.hide()
            ui.lineEdit_y.hide()
            ui.label_units1.hide()
            ui.label_units2.hide()
            ui.lineEdit_size_w.setMaximumWidth(50)
            ui.lineEdit_size_h.setMaximumWidth(50)

        def show_info_messagebox(info):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setText(info)
            
            msg.setWindowTitle("Information")
            
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            
            return msg.exec_()

        def export_selected():
            #return

            if gui.solution_ind == None:
                print("Please select a solution.")
                return
            
            solution=gui.core.cmd.structure_3D.solutions[gui.solution_ind]
            for feature in solution.features_list:
                if 'Ceramic' in feature.name:
                    gui.floorPlan[0]=feature.width
                    
                    gui.floorPlan[1]=feature.length
                    
                    break
            if gui.core.cmd.structure_3D.solutions:                
                export_solution_layout_attributes(sol_path=gui.pathToSolutions, solutions=[gui.core.cmd.structure_3D.solutions[gui.solution_ind]], size=[float(gui.floorPlan[0]), float(gui.floorPlan[1])])
                show_info_messagebox(f"Layout #{gui.solution_ind} exported")
            else:
                show_info_messagebox("Error: Something went wrong.")
            
        def export_all():
            if gui.core.cmd.structure_3D.solutions:
                export_solution_layout_attributes(sol_path=gui.pathToSolutions, solutions=gui.core.cmd.structure_3D.solutions, size=[float(gui.floorPlan[0]), float(gui.floorPlan[1])])
            show_info_messagebox(f"All {len(gui.core.cmd.structure_3D.solutions)} Layouts exported")

        def close_GUI():
            solutionBrowser.close()

        ui.btn_export_selected.clicked.connect(export_selected)
        ui.btn_export_all.clicked.connect(export_all)
        ui.btn_exit.clicked.connect(close_GUI)
        ui.btn_initial_layout.clicked.connect(display_initial_layout)

        ui.btn_export_selected.setToolTip("Export solution selected in the above graph to a csv file in the Solutions folder. Also, exports the parasitic netlist for the selected solution.")
        ui.btn_export_all.setToolTip("Export all solutions to a csv file in the Solutions folder.")
        ui.btn_exit.setToolTip("Close and exit the GUI.")
        ui.btn_initial_layout.setToolTip("Display initial layout.")

        display_initial_layout()
        solutionBrowser.show()
