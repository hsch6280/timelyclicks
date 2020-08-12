import sys
from src.stylesheet import blue_btn
from src.game import GameHome
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import *

class HomeWidget (QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(HomeWidget, self).__init__(*args, **kwargs)

        #create a layout for all out widgets. QVBox means widgets will be aligned vertically.
        self.layout = QVBoxLayout()

        # Set padding to layout:
        self.layout.setContentsMargins(30, 30, 30, 30)

        # To add anything to the screen we need to create it
        # and add it to the layout

        label = QLabel("Welcome to TimelyClicks")
        label.setFont(QFont("Arial", 16, QFont.Bold))
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(label)

        desc_label = QLabel("This game is all about reaction speed!\nOn the next page there is a 4x4 square of buttons. They will randomly show up an appear!\n Your job is to hit them before they go grey.")
        self.layout.addWidget(desc_label)

        btn_group = QVBoxLayout()
        btn_group.setAlignment(QtCore.Qt.AlignCenter)

        self.start_game_btn = QPushButton("Start Game")
        self.start_game_btn.setFixedWidth(100)
        self.start_game_btn.setStyleSheet(blue_btn())

        self.layout.addWidget(self.start_game_btn)
        self.setLayout(self.layout)
        self.show()

        #set the home layout

class Home(QtWidgets.QMainWindow):
    # Init our Home screen widget
    def __init__(self, *args, **kwargs):
        super(Home, self).__init__(*args, **kwargs)
        self.homeWidget = HomeWidget()
        self.homeWidget.start_game_btn.clicked.connect(self.start_game)
        self.setCentralWidget(self.homeWidget)
        self.show()

    def start_game(self):
        self.game_widget = GameHome()
        self.setCentralWidget(self.game_widget)
        self.show()

if __name__ == "__main__":
    home= Home()

