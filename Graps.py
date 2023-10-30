import io
import numexpr as ne
import sys
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, tan
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTabWidget
import warnings


import warnings

warnings.filterwarnings("ignore", category=Warning)

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QWidget" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1340</width>
    <height>794</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>13</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="draw">
    <property name="geometry">
     <rect>
      <x>790</x>
      <y>320</y>
      <width>261</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>13</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Построить граффик</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="input_textEdit">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>130</y>
      <width>761</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QSpinBox" name="minvalue">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>290</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="minimum">
     <number>-500</number>
    </property>
    <property name="maximum">
     <number>500</number>
    </property>
   </widget>
   <widget class="QSpinBox" name="maxvalue">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>400</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="minimum">
     <number>-500</number>
    </property>
    <property name="maximum">
     <number>500</number>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>280</y>
      <width>271</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>13</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите минимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>390</y>
      <width>271</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>13</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите максимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>120</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>13</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите функцию y=</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>30</y>
      <width>341</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>17</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Построитель графиков функций.</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1340</width>
     <height>29</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Graph_draw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('grapics.ui', self)
        self.draw.clicked.connect(self.draw_graph)

    def draw_graph(self):
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

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Graph_draw()
    ex.show()
    sys.exit(app.exec_())
