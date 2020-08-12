from src.stylesheet import blue_btn
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import *


class GameHome(QtWidgets.QWidget):
    def __init__(self, window, **kwargs):
        super(GameHome, self).__init__(*args, **kwargs)

        #create a layout for all out widgets. QVBox means widgets will be aligned vertically.
        layout = QVBoxLayout()

        self.row_1 = QHBoxLayout()

        self.btn_1_1 = QLabel("")
        self.btn_1_1.setStyleSheet("background-color: grey")
        self.btn_1_1.setFixedWidth(500)
        self.row_1.addWidget(self.btn_1_1)

        layout.addChildLayout(self.row_1)
        window.setLayout()



