import io
import numexpr as ne
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
import warnings

warnings.filterwarnings("ignore", category=Warning)


class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1340, 794)
        self.ui = uic.loadUi('projectstate.ui', self)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap('free-icon-algebra-5090382.png '))
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


class Graph_draw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('grapics.ui', self)
        self.draw.clicked.connect(self.draw_graph)

    def draw_graph(self):
        try:
            self.statusbar.showMessage("", 0)
            xmin = int(self.minvalue.text())
            xmax = int(self.maxvalue.text())
            dx = 1
            x = np.arange(xmin, xmax, dx)
            funcs = [self.input_textEdit.toPlainText()]
            new_funcs = [f if 'x' in f else 'x ** 0 * ({})'.format(f) for f in funcs]
            [plt.plot(x, ne.evaluate(f), linewidth=1.5) for f in new_funcs]
            plt.title('Графики функций')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend(funcs)
            plt.show()
        except KeyError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Ошибка ввода, пожалуйста введите верную функуию</FONT>",
                                         QMessageBox.Ok)
        except SyntaxError:
            valid = QMessageBox.question(self, 'ERROR',
                                         "<FONT COLOR='#ffffff'>Ошибка ввода, пожалуйста введите верную функуию</FONT>",
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
