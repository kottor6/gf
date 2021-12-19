import os
from PyQt5.Qtcore import Qt
from PyQt5.Qwidgets import (QApplication, QWidget, QFileDialog, QLabel, QPushButton, QLisWidget, QHBoxLayout, QVBoxLayout)
app = QApplication
win = Qwidgets
win.setWindowTitle('EasyEditor')
win.resize(700,500)

lb_image = Qlable('Картинка')
btn_dir = QPushButton('Папка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_lw = QPushButton('Ч/Б')
btn_shapr = QPushButton('Резкость')
btn_flip = QPushButton('Зеркало')
lw_files = QListWidget()

row = QHBoxLayout()
main_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

col_1.addWidget(btn_dir)
col_2.addWidget(row)
main_layout.addLayout(col_1, 2)
main_layout.addLayout(col_2, 8)


win.setLayout(main_layout)
win.show()
app_exec_()