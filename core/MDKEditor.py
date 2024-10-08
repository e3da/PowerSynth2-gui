
import sys, csv
import os
from PySide6.QtGui import *
from PySide6 import QtCore, QtGui
from gui.core.StructureCode import MaterialProperties
from gui.qt.py.Edit_Library import *
from operator import itemgetter
from copy import deepcopy
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QApplication, QComboBox, QFileDialog

class EditLibrary(QMainWindow, Ui_MDKWindow):
    def __init__(self, parent=None, MatLib=None):
        self.bridge = None
        self.mat_lib = []        #Have all material information
        self.row_num = 0         #Num of ALL materials
        self.pcm_num = 0         #Num of PCM materials
        self.con_num = 0         #Num of Conductor materials
        self.ins_num = 0         #Num of Insulator materials
        self.sem_num = 0         #Num of Semiconductor materials

        self.material_lib=MatLib

        super(EditLibrary, self).__init__(parent)
        self.setupUi(self)
        self.actionImport_2.triggered.connect(self.load)
        self.actionSave.triggered.connect(self.save)
        self.actionOpen_explanation.triggered.connect(self.explanation)
        self.load_default_button.clicked.connect(self.load(self.material_lib))
        self.search_button.clicked.connect(self.search)
        self.sort_button.clicked.connect(self.sort)
        self.add_all_button.clicked.connect(self.add_all)
        self.clone_all_button.clicked.connect(self.clone_all)
        self.update_all_button.clicked.connect(self.update_all)
        self.remove_all_button.clicked.connect(self.remove_all)
        self.add_pcm_button.clicked.connect(self.add_pcm)
        self.clone_pcm_button.clicked.connect(self.clone_pcm)
        self.update_pcm_button.clicked.connect(self.update_pcm)
        self.remove_pcm_button.clicked.connect(self.remove_pcm)
        self.add_con_button.clicked.connect(self.add_conductor)
        self.clone_con_button.clicked.connect(self.clone_conductor)
        self.update_con_button.clicked.connect(self.update_conductor)
        self.remove_con_button.clicked.connect(self.remove_conductor)
        self.add_ins_button.clicked.connect(self.add_insulator)
        self.clone_ins_button.clicked.connect(self.clone_insulator)
        self.update_ins_button.clicked.connect(self.update_insulator)
        self.remove_ins_button.clicked.connect(self.remove_insulator)
        self.add_sem_button.clicked.connect(self.add_semiconductor)
        self.clone_sem_button.clicked.connect(self.clone_semiconductor)
        self.update_sem_button.clicked.connect(self.update_semiconductor)
        self.remove_sem_button.clicked.connect(self.remove_semiconductor)

        self.load(self.material_lib)

        self.show()

    def check_alpha(self, name):
        """
        Return true if value is alphabetical
        :return:True or False
        """
        return name.isalpha()

    def check_num(self, value):
        """
        Return true if value is numerical value with allowed special characters
        :return:True or False
        """
        try: 
            float(value) 
            return True 
        except ValueError: 
            return False

    def check_same(self, name):
        """
        Return true if there is no same name material in the library
        :param name:
        :return:True or False
        """
        check = True
        rows = self.mat_lib
        num = 0
        for row in rows:
            if row.name == name:
                if num == 0:
                    num += 1
                else:
                    check = False
                    break
        return check

    def load(self,MatLib=None):
        """
        Open another window to get file name
        :return: Nothing
        """
        self.mat_lib = []
        if not MatLib:
            filename, ok = QFileDialog.getOpenFileName(parent=self, caption='Select Open File', filter='CSV Files (*.csv)')
        else:
            filename=MatLib
        if not filename:
            return
        with open(filename, newline='') as data:
            reader = csv.DictReader(data)
            for row in reader:
                p_rat = None
                th_cond = None
                th_condL = None
                dens = None
                densL = None
                spec = None
                specL = None
                melt = None
                e_res = None
                pmit = None
                pmea = None
                cte = None
                y_mdl = row['young_modulus']
                p_rat = row['poissons_ratios']
                th_cond = row['thermal_cond']
                th_condL = row['thermal_cond_liq']
                dens = row['density']
                densL = row['density_liq']
                spec = row['spec_heat_cap']
                specL = row['spec_heat_cap_liq']
                melt = row['melting_temp']
                e_res = row['electrical_res']
                pmit = row['rel_permit']
                pmea = row['rel_permeab']
                cte = row['thermal_expansion_coeffcient']
                data = MaterialProperties(name=row['name'], thermal_cond_so=th_cond, thermal_cond_liq=th_condL,
                        spec_heat_cap_so=spec, spec_heat_cap_liq=specL, density_so=dens,
                        density_liq=densL, electrical_res=e_res, rel_permit=pmit, rel_permeab=pmea,
                        young_modulus=y_mdl, poisson_ratio=p_rat, thermal_expansion_coefficient=cte,
                        type=row['type'], melting_temp=melt)
                self.mat_lib.append(data)
        self.ok()

    def save(self,MatLib=None):
        """
        Open another window and choose or create file to save materials
        :return: Nothing
        """
        rows = self.mat_lib
        if not MatLib:
            filename, ok = QFileDialog.getSaveFileName(parent=self, caption='Select Save File', filter='CSV Files (*.csv)')
        else:
            filename=MatLib

        if not filename:
            return

        with open(filename, 'w', newline='') as csvFile:
            header = ["name", "thermal_cond", "thermal_cond_liq", "spec_heat_cap",
                    "spec_heat_cap_liq", "density", "density_liq", "electrical_res",
                    "rel_permit", "rel_permeab", "q3d_id", "young_modulus", "poissons_ratios",
                    "thermal_expansion_coeffcient", "type",
                    "melting_temp"]
            writer = csv.DictWriter(csvFile, fieldnames=header)
            writer.writeheader()
            for row in rows:
                data={'name':None, 'thermal_cond':None, 'thermal_cond_liq':None, 'spec_heat_cap':None,
                        'spec_heat_cap_liq':None, 'density':None, 'density_liq':None, 'electrical_res':None,
                        'rel_permit':None, 'rel_permeab':None, 'q3d_id':None, 'young_modulus':None, 'poissons_ratios':None,
                        'thermal_expansion_coeffcient':None, 'type':None, 'melting_temp':None}
                data['name'] = row.name
                data['thermal_cond'] = row.thermal_cond_so
                data['thermal_cond_liq'] = row.thermal_cond_liq
                data['spec_heat_cap'] = row.spec_heat_cap_so
                data['spec_heat_cap_liq'] = row.spec_heat_cap_liq
                data['density'] = row.density_so
                data['density_liq'] = row.density_liq
                data['electrical_res'] = row.electrical_res
                data['rel_permit'] = row.rel_permit
                data['rel_permeab'] = row.rel_permeab
                data['q3d_id'] = row.name
                data['young_modulus'] = row.young_modulus
                data['poissons_ratios'] = row.poisson_ratio
                data['thermal_expansion_coeffcient'] = row.thermal_expansion_coefficient
                data['type'] = row.type
                data['melting_temp'] = row.melting_temp
                writer.writerow(data)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Materials are saved to "+filename)
        msg.setWindowTitle("Message")
        msg.exec()

    def explanation(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Import : Import your file to the table")
        msg.setInformativeText("Export : Save materials to your own file")
        msg.setWindowTitle("Message")
        msg.exec()

    def ok(self):
        """
        This function creates tables with mat_lib
        Also, get number of materials of each type
        :return: Nothing
        """
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4.clearContents()
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_5.clearContents()
        self.tableWidget_5.setRowCount(0)
        row_id = 0
        id2 = 0
        id3 = 0
        id4 = 0
        id5 = 0
        rows = self.mat_lib
        for row in rows:        #Insert row each table depend on materials' types
            self.tableWidget.insertRow(row_id)
            if row.type == 'PCM':
                self.tableWidget_2.insertRow(id2)
                id2 += 1
            if row.type == 'Conductor':
                self.tableWidget_3.insertRow(id3)
                id3 += 1
            if row.type == 'Insulator':
                self.tableWidget_4.insertRow(id4)
                id4 += 1
            if row.type == 'Semiconductor':
                self.tableWidget_5.insertRow(id5)
                id5 += 1
        id2 = 0
        id3 = 0
        id4 = 0
        id5 = 0
        for row in rows:
            # ALL table contents
            self.tableWidget.setItem(row_id, 0, QTableWidgetItem(row.name))
            type = row.type
            combo = QComboBox()
            option = ["PCM", "Conductor", "Insulator", "Semiconductor", "None"]
            for t in option:
                combo.addItem(t)
            if type == 'PCM':
                combo.setCurrentIndex(0)
            elif type == 'Conductor':
                combo.setCurrentIndex(1)
            elif type == 'Insulator':
                combo.setCurrentIndex(2)
            elif type == 'Semiconductor':
                combo.setCurrentIndex(3)
            else:
                combo.setCurrentIndex(4)
            self.tableWidget.setCellWidget(row_id, 1, combo)
            self.tableWidget.setItem(row_id, 2, QTableWidgetItem(row.young_modulus))
            self.tableWidget.setItem(row_id, 3, QTableWidgetItem(row.poisson_ratio))
            self.tableWidget.setItem(row_id, 4, QTableWidgetItem(row.melting_temp))
            self.tableWidget.setItem(row_id, 5, QTableWidgetItem(row.density_so))
            self.tableWidget.setItem(row_id, 6, QTableWidgetItem(row.density_liq))
            self.tableWidget.setItem(row_id, 7, QTableWidgetItem(row.thermal_cond_so))
            self.tableWidget.setItem(row_id, 8, QTableWidgetItem(row.thermal_cond_liq))
            self.tableWidget.setItem(row_id, 9, QTableWidgetItem(row.spec_heat_cap_so))
            self.tableWidget.setItem(row_id, 10, QTableWidgetItem(row.spec_heat_cap_liq))
            self.tableWidget.setItem(row_id, 11, QTableWidgetItem(row.electrical_res))
            self.tableWidget.setItem(row_id, 12, QTableWidgetItem(row.rel_permit))
            self.tableWidget.setItem(row_id, 13, QTableWidgetItem(row.rel_permeab))
            self.tableWidget.setItem(row_id, 14, QTableWidgetItem(row.thermal_expansion_coefficient))
            # PCM table contents
            if row.type == 'PCM':
                self.tableWidget_2.setItem(id2, 0, QTableWidgetItem(row.name))
                self.tableWidget_2.setItem(id2, 1, QTableWidgetItem(row.young_modulus))
                self.tableWidget_2.setItem(id2, 2, QTableWidgetItem(row.poisson_ratio))
                self.tableWidget_2.setItem(id2, 3, QTableWidgetItem(row.thermal_expansion_coefficient))
                self.tableWidget_2.setItem(id2, 4, QTableWidgetItem(row.melting_temp))
                self.tableWidget_2.setItem(id2, 5, QTableWidgetItem(row.density_so))
                self.tableWidget_2.setItem(id2, 6, QTableWidgetItem(row.density_liq))
                self.tableWidget_2.setItem(id2, 7, QTableWidgetItem(row.thermal_cond_so))
                self.tableWidget_2.setItem(id2, 8, QTableWidgetItem(row.thermal_cond_liq))
                self.tableWidget_2.setItem(id2, 9, QTableWidgetItem(row.spec_heat_cap_so))
                self.tableWidget_2.setItem(id2, 10, QTableWidgetItem(row.spec_heat_cap_liq))
                id2 += 1
            # Conductor table contents
            if row.type == 'Conductor':
                self.tableWidget_3.setItem(id3, 0, QTableWidgetItem(row.name))
                self.tableWidget_3.setItem(id3, 1, QTableWidgetItem(row.young_modulus))
                self.tableWidget_3.setItem(id3, 2, QTableWidgetItem(row.poisson_ratio))
                self.tableWidget_3.setItem(id3, 3, QTableWidgetItem(row.density_so))
                self.tableWidget_3.setItem(id3, 4, QTableWidgetItem(row.thermal_cond_so))
                self.tableWidget_3.setItem(id3, 5, QTableWidgetItem(row.spec_heat_cap_so))
                self.tableWidget_3.setItem(id3, 6, QTableWidgetItem(row.electrical_res))
                self.tableWidget_3.setItem(id3, 7, QTableWidgetItem(row.rel_permit))
                self.tableWidget_3.setItem(id3, 8, QTableWidgetItem(row.rel_permeab))
                self.tableWidget_3.setItem(id3, 9, QTableWidgetItem(row.thermal_expansion_coefficient))
                id3 += 1
            # Insulator table contents
            if row.type == 'Insulator':
                self.tableWidget_4.setItem(id4, 0, QTableWidgetItem(row.name))
                self.tableWidget_4.setItem(id4, 1, QTableWidgetItem(row.young_modulus))
                self.tableWidget_4.setItem(id4, 2, QTableWidgetItem(row.poisson_ratio))
                self.tableWidget_4.setItem(id4, 3, QTableWidgetItem(row.density_so))
                self.tableWidget_4.setItem(id4, 4, QTableWidgetItem(row.thermal_cond_so))
                self.tableWidget_4.setItem(id4, 5, QTableWidgetItem(row.spec_heat_cap_so))
                self.tableWidget_4.setItem(id4, 6, QTableWidgetItem(row.electrical_res))
                self.tableWidget_4.setItem(id4, 7, QTableWidgetItem(row.rel_permit))
                self.tableWidget_4.setItem(id4, 8, QTableWidgetItem(row.rel_permeab))
                self.tableWidget_4.setItem(id4, 9, QTableWidgetItem(row.thermal_expansion_coefficient))
                id4 += 1
            # Semiconductor tablecontents
            if row.type == 'Semiconductor':
                self.tableWidget_5.setItem(id5, 0, QTableWidgetItem(row.name))
                self.tableWidget_5.setItem(id5, 1, QTableWidgetItem(row.young_modulus))
                self.tableWidget_5.setItem(id5, 2, QTableWidgetItem(row.poisson_ratio))
                self.tableWidget_5.setItem(id5, 3, QTableWidgetItem(row.density_so))
                self.tableWidget_5.setItem(id5, 4, QTableWidgetItem(row.thermal_cond_so))
                self.tableWidget_5.setItem(id5, 5, QTableWidgetItem(row.spec_heat_cap_so))
                self.tableWidget_5.setItem(id5, 6, QTableWidgetItem(row.electrical_res))
                self.tableWidget_5.setItem(id5, 7, QTableWidgetItem(row.rel_permit))
                self.tableWidget_5.setItem(id5, 8, QTableWidgetItem(row.rel_permeab))
                self.tableWidget_5.setItem(id5, 9, QTableWidgetItem(row.thermal_expansion_coefficient))
                id5 += 1
            row_id += 1
        #Adjust table columns' sizes
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_4.resizeColumnsToContents()
        self.tableWidget_5.resizeColumnsToContents()
        self.row_num = row_id
        self.pcm_num = id2
        self.con_num = id3
        self.ins_num = id4
        self.sem_num = id5

    def search(self):
        """
        Find specific material and come it to the top of the table
        :return: Nothing
        """
        rows = self.mat_lib
        text = self.comboBox.currentText()
        item = self.SearchItem.text()
        value2 = item
        if text == 'Name':
            row_id = 0
            for row in rows:
                if value2 == row.name:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    message = item + " is found"
                    msg.setText(message)
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Thermal Conductivity' or text == 'Thermal Conductivity(Solid)':
            row_id = 0
            for row in rows:
                if value2 == row.thermal_cond_so:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Thermal Conductivity(Liquid)':
            row_id = 0
            for row in rows:
                if value2 == row.thermal_cond_liq:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Specific Heat Capacity' or text == 'Specific Heat Capacity(Solid)':
            row_id = 0
            for row in rows:
                if value2 == row.spec_heat_cap_so:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Specific Heat Capacity(Liquid)':
            row_id = 0
            for row in rows:
                if value2 == row.spec_heat_cap_liq:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Density' or text == 'Density(Solid)':
            row_id = 0
            for row in rows:
                if value2 == row.density_so:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Density(Liquid)':
            row_id = 0
            for row in rows:
                if value2 == row.density_liq:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Electrical Resistivity':
            row_id = 0
            for row in rows:
                if value2 == row.electrical_res:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Relative Permittivity':
            row_id = 0
            for row in rows:
                if value2 == row.rel_permit:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Relative Permeability':
            row_id = 0
            for row in rows:
                if value2 == row.rel_permeab:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'Young Modulus':
            row_id = 0
            for row in rows:
                if value2 == row.young_modulus:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == "Poisson's Ratio":
            row_id = 0
            for row in rows:
                if value2 == row.poisson_ratio:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1
        if text == 'CTE':
            row_id = 0
            for row in rows:
                if value2 == row.thermal_expansion_coefficient:
                    value = rows[row_id]
                    rows.pop(row_id)
                    rows.insert(0, value)
                    self.mat_lib = rows
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Material is found")
                    msg.setWindowTitle("Message")
                    msg.exec()
                    self.ok()
                row_id += 1

    def sort(self):
        """
        Sort materials based on name
        :return: Nothing
        """
        line = self.mat_lib
        rows = []
        for row in line:
            data = {'name': None, 'thermal_cond': None, 'thermal_cond_liq': None, 'spec_heat_cap': None,
                    'spec_heat_cap_liq': None, 'density': None, 'density_liq': None, 'electrical_res': None,
                    'rel_permit': None, 'rel_permeab': None, 'q3d_id': None, 'young_modulus': None,
                    'poissons_ratios': None,
                    'thermal_expansion_coeffcient': None, 'type': None, 'melting_temp': None}
            data['name'] = row.name
            data['thermal_cond'] = row.thermal_cond_so
            data['thermal_cond_liq'] = row.thermal_cond_liq
            data['spec_heat_cap'] = row.spec_heat_cap_so
            data['spec_heat_cap_liq'] = row.spec_heat_cap_liq
            data['density'] = row.density_so
            data['density_liq'] = row.density_liq
            data['electrical_res'] = row.electrical_res
            data['rel_permit'] = row.rel_permit
            data['rel_permeab'] = row.rel_permeab
            data['q3d_id'] = row.name
            data['young_modulus'] = row.young_modulus
            data['poissons_ratios'] = row.poisson_ratio
            data['thermal_expansion_coeffcient'] = row.thermal_expansion_coefficient
            data['type'] = row.type
            data['melting_temp'] = row.melting_temp
            rows.append(data)
        item = 'Name'
        if item == 'Name':
            def sort(lines):
                return lines['name']
            rows.sort(key=sort)
        self.mat_lib = []
        for row in rows:
            p_rat = None
            th_cond = None
            th_condL = None
            dens = None
            densL = None
            spec = None
            specL = None
            melt = None
            e_res = None
            pmit = None
            pmea = None
            cte = None
            y_mdl = row['young_modulus']
            p_rat = row['poissons_ratios']
            th_cond = row['thermal_cond']
            th_condL = row['thermal_cond_liq']
            dens = row['density']
            densL = row['density_liq']
            spec = row['spec_heat_cap']
            specL = row['spec_heat_cap_liq']
            melt = row['melting_temp']
            e_res = row['electrical_res']
            pmit = row['rel_permit']
            pmea = row['rel_permeab']
            cte = row['thermal_expansion_coeffcient']
            data = MaterialProperties(name=row['name'], thermal_cond_so=th_cond, thermal_cond_liq=th_condL,
                    spec_heat_cap_so=spec, spec_heat_cap_liq=specL, density_so=dens,
                    density_liq=densL, electrical_res=e_res, rel_permit=pmit, rel_permeab=pmea,
                    young_modulus=y_mdl, poisson_ratio=p_rat, thermal_expansion_coefficient=cte,
                    type=row['type'], melting_temp=melt)
            self.mat_lib.append(data)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = "Materials are sorted"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def add_material(self, type):
        """
        Add blank line to tableWidget
        :return: Nothing
        """
        name = None
        y_mdl = None
        p_rat = None
        th_cond = None
        th_condL = None
        dens = None
        densL = None
        spec = None
        specL = None
        melt = None
        e_res = None
        pmit = None
        pmea = None
        cte = None
        data = MaterialProperties(name=name, thermal_cond_so=th_cond, thermal_cond_liq=th_condL,
                spec_heat_cap_so=spec, spec_heat_cap_liq=specL, density_so=dens,
                density_liq=densL, electrical_res=e_res, rel_permit=pmit, rel_permeab=pmea,
                young_modulus=y_mdl, poisson_ratio=p_rat, thermal_expansion_coefficient=cte,
                type=type, melting_temp=melt)
        self.mat_lib.append(data)
        self.ok()

    def add_all(self):
        """
        Add blank line to tableWidget
        :return: Nothing
        """
        type = None
        self.add_material(type)

    def clone_all(self):
        """
        Create clone material in tableWidget
        :return: Nothing
        """
        value = self.tableWidget.currentRow()
        if value == -1:
            print("Error: No value is selected.")
            return
        rows = self.mat_lib
        item = rows[value]
        clone = deepcopy(item)
        clone.name = clone.name + 'Cloned'
        name = item.name
        rows.pop(value)
        rows.insert(0, clone)
        rows.insert(0, item)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is cloned"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def update_all(self):
        """
        Edit material with value checker in tableWidget
        :return: Nothing
        """
        num = self.tableWidget.currentRow()
        name = self.tableWidget.item(num,0).text()
        widget = self.tableWidget.cellWidget(num, 1)
        type = widget.currentText()
        y_mdl = self.tableWidget.item(num, 2).text()
        p_rat = self.tableWidget.item(num, 3).text()
        melt = self.tableWidget.item(num, 4).text()
        dens = self.tableWidget.item(num, 5).text()
        densL = self.tableWidget.item(num, 6).text()
        th_cond = self.tableWidget.item(num, 7).text()
        th_condL = self.tableWidget.item(num, 8).text()
        sp_cap = self.tableWidget.item(num, 9).text()
        sp_capL = self.tableWidget.item(num, 10).text()
        e_res = self.tableWidget.item(num,11).text()
        pmit = self.tableWidget.item(num, 12).text()
        pmea = self.tableWidget.item(num, 13).text()
        tm_co = self.tableWidget.item(num,14).text()
        check = False
        while not check:
            if check == self.check_alpha(name):
                break
            if check == self.check_same(name):
                break
            if check == self.check_num(y_mdl):
                break
            if check == self.check_num(p_rat):
                break
            if melt != '':
                if check == self.check_num(melt):
                    break
            if dens != '':
                if check == self.check_num(dens):
                    break
            if densL != '':
                if check == self.check_num(densL):
                    break
            if th_cond != '':
                if check == self.check_num(th_cond):
                    break
            if th_condL != '':
                if check == self.check_num(th_condL):
                    break
            if sp_cap != '':
                if check == self.check_num(sp_cap):
                    break
            if sp_capL != '':
                if check == self.check_num(sp_capL):
                    break
            if e_res != '':
                if check == self.check_num(e_res):
                    break
            if pmit != '':
                if check == self.check_num(pmit):
                    break
            if pmea != '':
                if check == self.check_num(pmea):
                    break
            if tm_co != '':
                if check == self.check_num(tm_co):
                    break
            check = True
            break
        if check:
            rows = self.mat_lib
            id2 = 0
            for row in rows:
                if num == id2:
                    row.name = name
                    row.type = type
                    row.young_modulus = y_mdl
                    row.poisson_ratio = p_rat
                    row.melting_temp = melt
                    row.density_so = dens
                    row.density_liq = densL
                    row.thermal_cond_so = th_cond
                    row.thermal_cond_liq = th_condL
                    row.spec_heat_cap_so = sp_cap
                    row.spec_heat_cap_liq = sp_capL
                    row.electrical_res = e_res
                    row.rel_permit = pmit
                    row.rel_permeab = pmea
                    row.thermal_expansion_coefficient = tm_co
                id2 += 1
            self.mat_lib = rows
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = name + " is updated"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = "Some values are inappropriate"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()

    def remove_all(self):
        """
        Remove material of tableWidget
        :return: Nothing
        """
        value = self.tableWidget.currentRow()
        rows = self.mat_lib
        num = 0
        name = None
        for row in rows:
            if value == num:
                name = row.name
                name = name
            num += 1
        rows.pop(value)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is removed"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def clone_material(self,type):
        """
        Create clone material in tableWidget
        :return: Nothing
        """
        value = self.tableWidget_2.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for i,row in rows:
            if row.type == type:
                if value == num:
                    self.pcm_num = id2
                num += 1
            id2 += 1
        item = rows[self.pcm_num]
        clone = deepcopy(item)
        clone.name = clone.name + ' copy'
        rows.append(item)
        self.ok()

    def add_pcm(self):
        """
        Add blank line to tableWidget_2
        :return: Nothing
        """
        type = "PCM"
        self.add_material(type)

    def clone_pcm(self):
        """
        Create clone material in tableWidget_2
        :return: Nothing
        """
        value = self.tableWidget_2.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'PCM':
                if value == num:
                    self.pcm_num = id2
                num += 1
            id2 += 1
        item = rows[self.pcm_num]
        clone = deepcopy(item)
        clone.name = clone.name + 'Cloned'
        name = item.name
        rows.pop(self.pcm_num)
        rows.insert(0, clone)
        rows.insert(0, item)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is cloned"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def update_pcm(self):
        """
        Edit material with value checker in tableWidget_2
        :return: Nothing
        """
        num = self.tableWidget_2.currentRow()
        name = self.tableWidget_2.item(num, 0).text()
        y_mdl = self.tableWidget_2.item(num, 1).text()
        p_rat = self.tableWidget_2.item(num, 2).text()
        tm_co = self.tableWidget_2.item(num, 3).text()
        melt = self.tableWidget_2.item(num, 4).text()
        dens = self.tableWidget_2.item(num, 5).text()
        densL = self.tableWidget_2.item(num, 6).text()
        th_cond = self.tableWidget_2.item(num, 7).text()
        th_condL = self.tableWidget_2.item(num, 8).text()
        sp_cap = self.tableWidget_2.item(num, 9).text()
        sp_capL = self.tableWidget_2.item(num, 10).text()
        check = False
        while not check:
            if check == self.check_alpha(name):
                break
            if check == self.check_same(name):
                break
            if check == self.check_num(y_mdl):
                break
            if check == self.check_num(p_rat):
                break
            if melt != '':
                if check == self.check_num(melt):
                    break
            if dens != '':
                if check == self.check_num(dens):
                    break
            if densL != '':
                if check == self.check_num(densL):
                    break
            if th_cond != '':
                if check == self.check_num(th_cond):
                    break
            if th_condL != '':
                if check == self.check_num(th_condL):
                    break
            if sp_cap != '':
                if check == self.check_num(sp_cap):
                    break
            if sp_capL != '':
                if check == self.check_num(sp_capL):
                    break
            if tm_co != '':
                if check == self.check_num(tm_co):
                    break
            check = True
            break
        if check:
            rows = self.mat_lib
            number = 0
            id2 = 0
            for row in rows:
                if row.type == 'PCM':
                    if num == number:
                        row.name = name
                        row.young_modulus = y_mdl
                        row.poisson_ratio = p_rat
                        row.melting_temp = melt
                        row.density_so = dens
                        row.density_liq = densL
                        row.thermal_cond_so = th_cond
                        row.thermal_cond_liq = th_condL
                        row.spec_heat_cap_so = sp_cap
                        row.spec_heat_cap_liq = sp_capL
                        row.thermal_expansion_coefficient = tm_co
                    number += 1
                id2 += 1
            self.mat_lib = rows
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = name + " is updated"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = "Some values are inappropriate"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()

    def remove_pcm(self):
        """
        Remove material of tableWidget_2
        :return: Nothing
        """
        value = self.tableWidget_2.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'PCM':
                if value == num:
                    self.pcm_num = id2
                num += 1
            id2 += 1
        item = rows[self.pcm_num]
        name = item.name
        rows.pop(self.pcm_num)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is removed"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def add_conductor(self):
        """
        Add blank line to tableWidget_3
        :return: Nothing
        """
        type = "Conductor"
        self.add_material(type)

    def clone_conductor(self):
        """
        Create clone material in tableWidget_2
        :return: Nothing
        """
        value = self.tableWidget_3.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'Conductor':
                if value == num:
                    self.con_num = id2
                    name = row.name
                num += 1
            id2 += 1
        item = rows[self.con_num]
        clone = deepcopy(item)
        clone.name = clone.name + 'Cloned'
        rows.pop(self.con_num)
        rows.insert(0, clone)
        rows.insert(0, item)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is cloned"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def update_conductor(self):
        """
        Edit material with value checker in tableWidget_3
        :return: Nothing
        """
        num = self.tableWidget_3.currentRow()
        name = self.tableWidget_3.item(num, 0).text()
        y_mdl = self.tableWidget_3.item(num, 1).text()
        p_rat = self.tableWidget_3.item(num, 2).text()
        dens = self.tableWidget_3.item(num, 3).text()
        th_cond = self.tableWidget_3.item(num, 4).text()
        sp_cap = self.tableWidget_3.item(num, 5).text()
        e_res = self.tableWidget_3.item(num, 6).text()
        pmit = self.tableWidget_3.item(num, 7).text()
        pmea = self.tableWidget_3.item(num, 8).text()
        tm_co = self.tableWidget_3.item(num, 9).text()
        check = False
        while not check:
            if check == self.check_alpha(name):
                break
            if check == self.check_same(name):
                break
            if check == self.check_num(y_mdl):
                break
            if check == self.check_num(p_rat):
                break
            if dens != '':
                if check == self.check_num(dens):
                    break
            if th_cond != '':
                if check == self.check_num(th_cond):
                    break
            if sp_cap != '':
                if check == self.check_num(sp_cap):
                    break
            if e_res != '':
                if check == self.check_num(e_res):
                    break
            if pmit != '':
                if check == self.check_num(pmit):
                    break
            if pmea != '':
                if check == self.check_num(pmea):
                    break
            if tm_co != '':
                if check == self.check_num(tm_co):
                    break
            check = True
            break
        if check:
            rows = self.mat_lib
            number = 0
            id2 = 0
            for row in rows:
                if row.type == 'Conductor':
                    if num == number:
                        self.con_num = id2
                        row.name = name
                        row.young_modulus = y_mdl
                        row.poisson_ratio = p_rat
                        row.density_so = dens
                        row.thermal_cond_so = th_cond
                        row.spec_heat_cap_so = sp_cap
                        row.electrical_res = e_res
                        row.rel_permit = pmit
                        row.rel_permeab = pmea
                        row.thermal_expansion_coefficient = tm_co
                        print(row)
                    number += 1
                id2 += 1
            self.mat_lib = rows
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = name + " is updated"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = "Some values are inappropriate"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()

    def remove_conductor(self):
        """
        Remove material of tableWidget_3
        :return: Nothing
        """
        value = self.tableWidget_3.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'Conductor':
                if value == num:
                    self.con_num = id2
                num += 1
            id2 += 1
        item = rows[self.con_num]
        name = item.name
        rows.pop(self.con_num)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is removed"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def add_insulator(self):
        """
        Add blank line to tableWidget_4
        :return: Nothing
        """
        type = "Insulator"
        self.add_material(type)

    def clone_insulator(self):
        """
        Create clone material in tableWidget_4
        :return: Nothing
        """
        value = self.tableWidget_4.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'Insulator':
                if value == num:
                    self.ins_num = id2
                    name = row.name
                num += 1
            id2 += 1
        item = rows[self.ins_num]
        clone = deepcopy(item)
        clone.name = clone.name + 'Cloned'
        rows.pop(self.ins_num)
        rows.insert(0, clone)
        rows.insert(0, item)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is cloned"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def update_insulator(self):
        """
        Edit material with value checker in tableWidget_4
        :return: Nothing
        """
        num = self.tableWidget_4.currentRow()
        name = self.tableWidget_4.item(num, 0).text()
        y_mdl = self.tableWidget_4.item(num, 1).text()
        p_rat = self.tableWidget_4.item(num, 2).text()
        dens = self.tableWidget_4.item(num, 3).text()
        th_cond = self.tableWidget_4.item(num, 4).text()
        sp_cap = self.tableWidget_4.item(num, 5).text()
        e_res = self.tableWidget_4.item(num, 6).text()
        pmit = self.tableWidget_4.item(num, 7).text()
        pmea = self.tableWidget_4.item(num, 8).text()
        tm_co = self.tableWidget_4.item(num, 9).text()
        value = self.tableWidget_4.currentRow()
        check = False
        while not check:
            if check == self.check_alpha(name):
                break
            if check == self.check_same(name):
                break
            if check == self.check_num(y_mdl):
                break
            if check == self.check_num(p_rat):
                break
            if dens != '':
                if check == self.check_num(dens):
                    break
            if th_cond != '':
                if check == self.check_num(th_cond):
                    break
            if sp_cap != '':
                if check == self.check_num(sp_cap):
                    break
            if e_res != '':
                if check == self.check_num(e_res):
                    break
            if pmit != '':
                if check == self.check_num(pmit):
                    break
            if pmea != '':
                if check == self.check_num(pmea):
                    break
            if tm_co != '':
                if check == self.check_num(tm_co):
                    break
            check = True
            break
        if check:
            rows = self.mat_lib
            number = 0
            id2 = 0
            for row in rows:
                if row.type == 'Insulator':
                    if value == number:
                        self.ins_num = id2
                        row.name = name
                        row.young_modulus = y_mdl
                        row.poisson_ratio = p_rat
                        row.density_so = dens
                        row.thermal_cond_so = th_cond
                        row.spec_heat_cap_so = sp_cap
                        row.electrical_res = e_res
                        row.rel_permit = pmit
                        row.rel_permeab = pmea
                        row.thermal_expansion_coefficient = tm_co
                    number += 1
                id2 += 1
            self.mat_lib = rows
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = name + " is updated"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = "Some values are inappropriate"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()

    def remove_insulator(self):
        """
        Remove material of tableWidget_4
        :return: Nothing
        """
        value = self.tableWidget_4.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'Insulator':
                if value == num:
                    self.ins_num = id2
                num += 1
            id2 += 1
        item = rows[self.ins_num]
        name = item.name
        rows.pop(self.ins_num)
        self.mat_lib = rows
        print ('Material is removed')
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is removed"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def add_semiconductor(self):
        """
        Add blank line to tableWidget_5
        :return: Nothing
        """
        type = "Semiconductor"
        self.add_material(type)

    def clone_semiconductor(self):
        """
        Create clone material in tableWidget_5
        :return: Nothing
        """
        rows = self.mat_lib
        value = self.tableWidget_5.currentRow()
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'Semiconductor':
                if value == num:
                    self.sem_num = id2
                num += 1
            id2 += 1
        item = rows[self.sem_num]
        name = item.name
        clone = deepcopy(item)
        clone.name = clone.name + 'Cloned'
        rows.pop(self.sem_num)
        rows.insert(0, clone)
        rows.insert(0, item)
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is cloned"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()

    def update_semiconductor(self):
        """
        Edit material with value checker in tableWidget_5
        :return: Nothing
        """
        num = self.tableWidget_5.currentRow()
        name = self.tableWidget_5.item(num, 0).text()
        y_mdl = self.tableWidget_5.item(num, 1).text()
        p_rat = self.tableWidget_5.item(num, 2).text()
        dens = self.tableWidget_5.item(num, 3).text()
        th_cond = self.tableWidget_5.item(num, 4).text()
        sp_cap = self.tableWidget_5.item(num, 5).text()
        e_res = self.tableWidget_5.item(num, 6).text()
        pmit = self.tableWidget_5.item(num, 7).text()
        pmea = self.tableWidget_5.item(num, 8).text()
        tm_co = self.tableWidget_5.item(num, 9).text()
        check = False
        while not check:
            if check == self.check_alpha(name):
                break
            if check == self.check_same(name):
                break
            if check == self.check_num(y_mdl):
                break
            if check == self.check_num(p_rat):
                break
            if dens != '':
                if check == self.check_num(dens):
                    break
            if th_cond != '':
                if check == self.check_num(th_cond):
                    break
            if sp_cap != '':
                if check == self.check_num(sp_cap):
                    break
            if e_res != '':
                if check == self.check_num(e_res):
                    break
            if pmit != '':
                if check == self.check_num(pmit):
                    break
            if pmea != '':
                if check == self.check_num(pmea):
                    break
            if tm_co != '':
                if check == self.check_num(tm_co):
                    break
            check = True
            break
        if check:
            rows = self.mat_lib
            num2 = 0
            id2 = 0
            for row in rows:
                if row.type == 'Semiconductor':
                    if num == num2:
                        self.sem_num = id2
                        row.name = name
                        row.young_modulus = y_mdl
                        row.poisson_ratio = p_rat
                        row.density_so = dens
                        row.thermal_cond_so = th_cond
                        row.spec_heat_cap_so = sp_cap
                        row.electrical_res = e_res
                        row.rel_permit = pmit
                        row.rel_permeab = pmea
                        row.thermal_expansion_coefficient = tm_co
                        print(row)
                    num2 += 1
                id2 += 1
            self.mat_lib = rows
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = name + " is updated"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            message = "Some values are inappropriate"
            msg.setText(message)
            msg.setWindowTitle("Message")
            msg.exec()
            self.ok()

    def remove_semiconductor(self):
        """
        Remove material of tableWidget_5
        :return: Nothing
        """
        value = self.tableWidget_5.currentRow()
        rows = self.mat_lib
        num = 0
        id2 = 0
        for row in rows:
            if row.type == 'Semiconductor':
                if value == num:
                    self.sem_num = id2
                num += 1
            id2 += 1
        item = rows[self.sem_num]
        rows.pop(self.sem_num)
        name = item.name
        self.mat_lib = rows
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        message = name + " is removed"
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()
        self.ok()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = self()
    gui = app.exec()
    sys.exit(gui)
