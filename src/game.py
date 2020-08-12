from src.stylesheet import blue_btn
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import *


class GameHome(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GameHome, self).__init__(parent)
        self.initUI()
    def initUI(self):

            self.createGridLayout()

            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)
            self.setLayout(windowLayout)

            self.show()

    def createGridLayout(self):
            self.horizontalGroupBox = QGroupBox("Grid")
            layout = QGridLayout()

            for x in range(3):
                for y in range(3):
                    btn = QPushButton("")
                    btn.setFixedWidth(100)
                    btn.setFixedHeight(100)
                    layout.addWidget(btn, x, y)


            self.horizontalGroupBox.setLayout(layout)
    def game_btn_press(self, x, y):
        print(f"btn: {x}, {y} pressed")



