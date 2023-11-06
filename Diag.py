import csv
import io
import numexpr as ne
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTabWidget, QFileDialog, QTableWidgetItem, QMessageBox
import warnings


class Diagram(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('diag.ui', self)
        self.draw_diag.clicked.connect(self.draw_diagram)
        self.open_menu()
        self.choose_file.clicked.connect(self.choose)
        self.clean_up.clicked.connect(self.clean)
        self.list1 = []
        self.list2 = []
        self.list3 = []

    def draw_diagram(self):
        try:
            assert len(self.list2) == 1
            if self.choose_diag.currentText() == 'Столбчатая диаграмма':
                plt.bar(self.list1, [float(i) for i in self.list2[0]])
                plt.title('Столбчатая диаграмма')
                plt.show()
            elif self.choose_diag.currentText() == 'Круговая диаграмма':
                plt.pie([float(i) for i in self.list2[0]], labels=self.list1, autopct='%1.1f%%')
                plt.title("Круговая диаграмма")
                plt.show()
        except AssertionError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Выделите два столбца</FONT>",
                                         QMessageBox.Ok)

    def choose(self):
        name = QFileDialog.getOpenFileName(
            self, 'Выбор', '',
            'Csv файл (*.csv)')[0]
        self.loadTable(name)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected):
        for ix in selected.indexes():
            print(ix.row(), ix.column(), self.tableWidget.item(ix.row(), ix.column()).text())
            if ix.column() == 0:
                self.list1.append(self.tableWidget.item(ix.row(), ix.column()).text())
            else:
                if ix.column() not in self.list3:
                    self.list3.append(ix.column())
                    self.list2.append([self.tableWidget.item(ix.row(), ix.column()).text()])
                else:
                    self.list2[ix.column() - 1].append(self.tableWidget.item(ix.row(), ix.column()).text())
        # print(self.list1)
        # print(self.list2)

    def open_menu(self):
        self.choose_diag.addItems(['Столбчатая диаграмма', 'Круговая диаграмма'])
        self.choose_diag.setStyleSheet('''
                color: rgb(255, 255, 255);
                ''')

    def clean(self):
        self.list1 = []
        self.list2 = []
        self.list3 = []


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Diagram()
    ex.show()
    sys.exit(app.exec_())