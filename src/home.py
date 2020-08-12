import sys
from src.stylesheet import blue_btn
from src.game import GameHome
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import *

class Home(QtWidgets.QWidget):
    # Init our Home screen widget
    def __init__(self, *args, **kwargs):
        super(Home, self).__init__(*args, **kwargs)

        #create a layout for all out widgets. QVBox means widgets will be aligned vertically.
        layout = QVBoxLayout()

        # Set padding to layout:
        layout.setContentsMargins(30, 30, 30, 30)

        # To add anything to the screen we need to create it
        # and add it to the layout

        label = QLabel("Welcome to TimelyClicks")
        label.setFont(QFont("Arial", 16, QFont.Bold))
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)

        desc_label = QLabel("This game is all about reaction speed!\nOn the next page there is a 4x4 square of buttons. They will randomly show up an appear!\n Your job is to hit them before they go grey.")
        layout.addWidget(desc_label)

        btn_group = QVBoxLayout()
        btn_group.setAlignment(QtCore.Qt.AlignCenter)

        self.start_game_btn = QPushButton("Start Game")
        self.start_game_btn.setFixedWidth(100)
        self.start_game_btn.setStyleSheet(blue_btn())
        self.start_game_btn.clicked.connect(self.button_clicked)

        layout.addWidget(self.start_game_btn)

        #set the home layout
        self.setLayout(layout)

    def button_clicked(self):
        print("start game btn pressed")



