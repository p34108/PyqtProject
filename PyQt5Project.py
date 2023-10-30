from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QPalette, QColor

app = QApplication([])

# Создание MessageBox
msgBox = QMessageBox()
msgBox.setText("Пример MessageBox")
msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

# Получение палитры текущей темы оформления
palette = app.palette()

# Установка цвета текста
palette.setColor(QPalette.Text, QColor("red"))
msgBox.setPalette(palette)

msgBox.exec()