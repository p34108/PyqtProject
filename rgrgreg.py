import numexpr as ne
import sys
import io
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QWidget, QPushButton, QComboBox, QColorDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets
import warnings

warnings.filterwarnings("ignore", category=Warning)


class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1340, 794)
        self.ui = uic.loadUi('projectstate.ui', self)
        self.tabWidget.setTabIcon(0, QIcon('free-icon-algebra-5090382.png'))
        self.tabWidget.setTabIcon(1, QIcon('free-icon-calculator-5351432.png'))
        self.tabWidget.setTabIcon(2, QIcon('free-icon-graph-bar-888000.png'))
        self.tabWidget.setTabIcon(3, QIcon('free-icon-about-7647315.png'))
        layout_cal = QtWidgets.QVBoxLayout()
        layout_grap = QtWidgets.QVBoxLayout()
        self.CalculatorTab.setLayout(layout_cal)
        self.calculator = Calculator()
        self.CalculatorTab.layout().addWidget(self.calculator)

        self.grapdisplay.setLayout(layout_grap)
        self.graphic = Graph_draw()
        self.grapdisplay.layout().addWidget(self.graphic)


class InputError(Exception):
    pass


class InputTypeLineError(InputError):
    pass


class InputColourGraphError(InputError):
    pass


class Graph_draw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.array_colourgraph, self.array_colourmain, self.array_typeline = [
            (0, 0, 0)], [(255, 255, 255)], ['-']
        self.ui = uic.loadUi('grapics.ui', self)
        self.draw.clicked.connect(self.draw_graph)
        self.draw.setIcon(QIcon('free-icon-build-603832.png'))
        self.resertButton.setIcon(QIcon('free-icon-reset-8651174.png'))
        self.resertButton.clicked.connect(self.resert)
        self.opshionButton.setIcon(QIcon('free-icon-settings-4043261.png'))
        self.opshionButton.clicked.connect(self.opshion)

    def draw_graph(self):
        try:
            xmin = int(self.minvalue.text())
            xmax = int(self.maxvalue.text())
            dx = 0.01
            x = np.arange(xmin, xmax, dx)
            funcs = self.input_textEdit.toPlainText().split('\n')
            new_funcs = [f if 'x' in f else 'x ** 0 * ({})'.format(f) for f in funcs]
            if self.flag:
                [plt.plot(x, ne.evaluate(new_funcs[f]), linewidth=1.5,
                          color='#%02x%02x%02x' % self.array_colourgraph[f], linestyle=self.array_typeline[f]) for f in
                 range(len(new_funcs))]
                plt.title('Графики функций')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.legend(funcs)
                plt.show()
            else:
                self.array_typeline *= len(self.input_textEdit.toPlainText().split('\n'))
                self.array_colourgraph *= len(self.input_textEdit.toPlainText().split('\n'))
                [plt.plot(x, ne.evaluate(new_funcs[f]), linewidth=1.5,
                          color='#%02x%02x%02x' % self.array_colourgraph[f],
                          linestyle=self.array_typeline[f]) for f in range(len(new_funcs))]
                plt.title('Графики функций')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.legend(funcs)
                plt.show()
            # new_funcs = [f if 'x' in f else 'x ** 0 * ({})'.format(f) for f in funcs]
            # [plt.plot(x, ne.evaluate(f), linewidth=1.5) for f in new_funcs]
            # plt.title('Графики функций')
            # plt.xlabel('x')
            # plt.ylabel('y')
            # plt.legend(funcs)
            # plt.show()
        except KeyError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Ошибка ввода, пожалуйста введите верную функуию</FONT>",
                                         QMessageBox.Ok)
        except SyntaxError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Ошибка ввода, пожалуйста введите верную функуию</FONT>",
                                         QMessageBox.Ok)
        except TypeError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Ошибка ввода, пожалуйста введите верную функуию</FONT>",
                                         QMessageBox.Ok)

    def opshion(self):
        self.flag = True
        self.second_form = SecondForm(self.array_colourgraph, self.array_colourmain, self.array_typeline,
                                      len(self.input_textEdit.toPlainText().split('\n')))
        self.second_form.show()

    def resert(self):
        self.flag = False
        valid = QMessageBox.question(self, 'Resert?',
                                     "<FONT COLOR='#ffffff'>Сбросить изменения*?</FONT>",
                                     QMessageBox.Yes, QMessageBox.No)
        if QMessageBox.Yes:
            valid = QMessageBox.question(self, 'Successfully',
                                         "<FONT COLOR='#ffffff'>Успешно</FONT>",
                                         QMessageBox.Ok)
            self.array_colourgraph, self.array_colourmain, self.array_typeline = [
                (0, 0, 0)], [(255, 255, 255)], ['-']


class SecondForm(QWidget):
    def __init__(self, *arg):
        super().__init__()
        self.sp1, self.sp2, self.sp3 = [], [], []
        self.a1, self.a2, self.a3, self.len_ofgraph = arg
        self.initUI()

    def initUI(self):
        self.setFixedSize(1100, 900)
        self.setStyleSheet("background-color: rgb(35, 40, 49)")
        self.setWindowTitle('Дополнительные настройки')
        self.text1 = QLabel('Задать цвет для графиков(кол нажний на кнопку = кол цветов = кол графиков)', self)
        self.text1.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 15px;
        ''')
        self.text1.move(50, 50)

        self.buttoncolour_graph = QPushButton('Задать цвет', self)
        self.buttoncolour_graph.resize(320, 60)
        self.buttoncolour_graph.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 15px;
        ''')
        self.buttoncolour_graph.move(700, 30)
        self.buttoncolour_graph.clicked.connect(self.graph_col)

        self.text2 = QLabel('Задать цвет для общего фона', self)
        self.text2.setStyleSheet('''
                color: rgb(255, 255, 255);
                font: bold 15px;
                ''')
        self.text2.move(50, 150)

        self.buttoncolour_main = QPushButton('Задать цвет', self)
        self.buttoncolour_main.resize(320, 60)
        self.buttoncolour_main.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 15px;
        ''')
        self.buttoncolour_main.move(300, 130)
        self.buttoncolour_main.clicked.connect(self.main_col)

        self.text3 = QLabel('Задать шрифт для графиков (кол нажний на кнопку = кол цветов = кол графиков)', self)
        self.text3.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 15px;
        ''')
        self.text3.move(50, 250)

        self.comboxColour = QComboBox(self)
        self.comboxColour.move(710, 245)
        self.comboxColour.resize(70, 30)
        self.comboxColour.addItem('-')
        self.comboxColour.addItem('--')
        self.comboxColour.addItem('-.')
        self.comboxColour.addItem(':')
        self.comboxColour.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 20px;
        ''')

        self.buttonline = QPushButton('Задать тип линий', self)
        self.buttonline.resize(300, 60)
        self.buttonline.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 15px;
        ''')
        self.buttonline.move(790, 230)
        self.buttonline.clicked.connect(self.type_line)

        self.savebutton = QPushButton('Сохранить изменения', self)
        self.savebutton.resize(300, 60)
        self.savebutton.setStyleSheet('''
        color: rgb(255, 255, 255);
        font: bold 15px;
        ''')
        self.savebutton.move(790, 350)
        self.savebutton.clicked.connect(self.save_progress)

    def main_col(self):
        color = QColorDialog.getColor()
        self.sp2.append((color.red(), color.green(), color.blue()))

    def graph_col(self):
        color = QColorDialog.getColor()
        self.sp1.append((color.red(), color.green(), color.blue()))

    def type_line(self):
        self.sp3.append(self.comboxColour.currentText())

    def save_progress(self):
        try:
            valid = QMessageBox.question(self, 'SaveExit',
                                         "<FONT COLOR='#ffffff'>Сохранить изменения?</FONT>",
                                         QMessageBox.Yes, QMessageBox.No)
            if QMessageBox.Yes:
                if len(self.sp1) != self.len_ofgraph:
                    raise InputColourGraphError
                if len(self.sp3) != self.len_ofgraph:
                    raise InputTypeLineError
                self.a1.clear()
                self.a2.clear()
                self.a3.clear()
                self.a1 += self.sp1
                self.a2 += self.sp2
                self.a3 += self.sp3
                print(self.a1, self.a2, self.a3)
                valid = QMessageBox.question(self, 'Successfully',
                                             "<FONT COLOR='#ffffff'>Измения успешно применены!</FONT>",
                                             QMessageBox.Ok)
                self.close()
        except InputTypeLineError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Количество типов линий не "
                                         "соответсвуют количествам графиков</FONT>",
                                         QMessageBox.Ok)
        except InputColourGraphError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Количество цветов для графиков не "
                                         "соответсвует количествам графиков</FONT>",
                                         QMessageBox.Ok)


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>371</width>
    <height>565</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Красивый калькулятор</string>
  </property>
  <widget class="QWidget" name="layoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>345</width>
     <height>481</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLCDNumber" name="table"/>
    </item>
    <item>
     <layout class="QGridLayout" name="gridLayout">
      <item row="2" column="1">
       <widget class="QPushButton" name="btn8">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>8</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="1">
       <widget class="QPushButton" name="btn2">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>2</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="3">
       <widget class="QPushButton" name="btn_plus">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>+</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="2">
       <widget class="QPushButton" name="btn_eq">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>=</string>
        </property>
       </widget>
      </item>
      <item row="3" column="0">
       <widget class="QPushButton" name="btn0">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>0</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="3">
       <widget class="QPushButton" name="btn_div">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>/</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="0">
       <widget class="QPushButton" name="btn1">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>1</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="2">
       <widget class="QPushButton" name="btn9">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>9</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="1">
       <widget class="QPushButton" name="btn_dot">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>.</string>
        </property>
       </widget>
      </item>
      <item row="0" column="2">
       <widget class="QPushButton" name="btn3">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>3</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="0">
       <widget class="QPushButton" name="btn4">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>4</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="1">
       <widget class="QPushButton" name="btn5">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>5</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="0">
       <widget class="QPushButton" name="btn7">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>7</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="2">
       <widget class="QPushButton" name="btn6">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>6</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="3">
       <widget class="QPushButton" name="btn_minus">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>-</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="3">
       <widget class="QPushButton" name="btn_mult">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>*</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="4" column="0">
       <widget class="QPushButton" name="btn_pow">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>^</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="4" column="1">
       <widget class="QPushButton" name="btn_sqrt">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>√</string>
        </property>
       </widget>
      </item>
      <item row="4" column="2">
       <widget class="QPushButton" name="btn_fact">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>!</string>
        </property>
       </widget>
      </item>
      <item row="4" column="3">
       <widget class="QPushButton" name="btn_clear">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">background-color: rgb(254, 166, 43);</string>
        </property>
        <property name="text">
         <string>С</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup_binary"/>
  <buttongroup name="buttonGroup_digits"/>
 </buttongroups>
</ui>"""


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        x = io.StringIO(template)
        uic.loadUi(x, self)
        self.btn0.clicked.connect(self.run)
        self.btn1.clicked.connect(self.run)
        self.btn2.clicked.connect(self.run)
        self.btn3.clicked.connect(self.run)
        self.btn4.clicked.connect(self.run)
        self.btn5.clicked.connect(self.run)
        self.btn6.clicked.connect(self.run)
        self.btn7.clicked.connect(self.run)
        self.btn8.clicked.connect(self.run)
        self.btn9.clicked.connect(self.run)

        self.btn_minus.clicked.connect(self.calc)
        self.btn_plus.clicked.connect(self.calc)
        self.btn_pow.clicked.connect(self.calc)
        self.btn_mult.clicked.connect(self.calc)
        self.btn_div.clicked.connect(self.calc)

        self.btn_dot.clicked.connect(self.run)
        self.btn_eq.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        self.opp = QPushButton('Настройки калькулятоа', self)
        self.opp.resize(320, 60)
        self.opp.setStyleSheet('''
        font: bold 15px;
        ''')
        self.opp.move(700, 30)
        self.opp.clicked.connect(self.oppion)

    def oppion(self):
        url = QtCore.QUrl("https://boulderbugle.com/mathpyqt5-yhgtb85m")
        QtGui.QDesktopServices.openUrl(url)

        self.data = ''
        self.data_eval = ''

    def real_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)

    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            self.result()

    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('')

    def run(self):
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)

    def sqrt(self):
        if self.data_eval:
            self.data_eval += '**0.5'
            self.result()

    def result(self):
        try:
            self.data = eval(self.data_eval)
            self.data_eval = str(self.data)
            self.table.display(self.data)
            self.data = ''
        except ZeroDivisionError:
            self.table.display('error')

    def calc(self):
        if self.data_eval:
            self.result()
            if self.data_eval[-1] not in ['+', '-', '/', '*']:
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval) - 1] + self.sender().text()
            self.data_eval = self.data_eval.replace('^', '**')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainClass()
    ex.show()
    sys.exit(app.exec_())