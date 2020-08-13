from src.stylesheet import blue_btn
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
import time
from PyQt5.QtCore import  QTimer
from PyQt5.QtWidgets import *
from random import *

end_score = 0

class GameOver(QtWidgets.QWidget):
    global end_score
    def __init__(self):
        super(GameOver, self).__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 0, 0, 30)
        game_over_label = QLabel("GAME OVER")
        game_over_label.setFont( QFont('Arial', 16, QFont.Bold))
        game_over_label.setAlignment(QtCore.Qt.AlignCenter)
        score_label = QLabel(f"Score was: {str(end_score)}")
        score_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(game_over_label)
        layout.addWidget(score_label)
        self.setLayout(layout)
        self.show()

class GameHome(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GameHome, self).__init__(parent)
        self.game_over = False
        self.correct_btn = []
        self.points = 0
        self.time_press = 0
        self.btn_pressed_in_time = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.time_to_press = 50
        self.current_time = 0
        self.last_btn = [0, 0]
        self.timer.start(100)
        self.initUI()
    def reset_round(self):
        self.timer.stop()
        self.game_over = False
        self.btn_pressed_in_time = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.time_to_press = 50
        self.current_time = 0

        time.sleep(1)
        self.timer.start(100)

    def set_game_over(self):
        self.timer.stop()
        self.point_label.setParent(None)
        self.horizontalGroupBox.setParent(None)
        self.window_layout.addWidget(GameOver())
    def check_time(self):

        global end_score
        if not self.game_over:
            if self.current_time > 0:
                if self.btn_pressed_in_time and self.current_time < self.time_to_press:
                    print("correct")
                    self.points += 1
                    self.point_label.setText(f"Current score: {str(self.points)}")
                    self.reset_btn()
                    self.reset_round()
                    self.select_btn()
                elif self.current_time > self.time_to_press:
                    end_score = self.points
                    self.game_over = True
                    self.set_game_over()

            else:
                self.select_btn()
            self.current_time += 1
        else:
            print("Game over")
            self.set_game_over()
            self.timer.stop()

    def game_btn_press(self, x_y):
        def handle_x_y():
            if x_y == self.correct_btn:
                self.btn_pressed_in_time = True
        return handle_x_y

    def initUI(self):
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        self.point_label = QLabel(f"Current Score: {str(self.points)}")
        self.point_label.setFont(QFont("Arial", 16, QFont.Black))
        self.point_label.setAlignment(QtCore.Qt.AlignCenter)
        windowLayout.addWidget(self.point_label)
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
        self.window_layout = windowLayout

        #     self.correct_btn = [rand_x, rand_y]
    def create_btn(self):
        btn = QPushButton("")
        btn.setFixedWidth(150)
        btn.setFixedHeight(100)
        return btn

    def reset_btn(self):
        btn = self.create_btn()
        btn.setStyleSheet("background-color: slategrey")
        self.grid.addWidget(btn, self.correct_btn[0], self.correct_btn[1])

    def select_btn(self):
        found_new_btn = False

        while not found_new_btn:
            rand_x = randint(0, 3)
            rand_y = randint(0, 3)
            x_y = [rand_x, rand_y]
            if x_y != self.last_btn:
                self.correct_btn = [rand_x, rand_y]
                self.last_btn  = x_y
                btn = self.create_btn()
                btn.setStyleSheet("background-color: red")
                btn.clicked.connect(self.game_btn_press(self.correct_btn))
                self.grid.addWidget(btn, self.correct_btn[0], self.correct_btn[1])
                found_new_btn = True
                self.show()

    def createGridLayout(self):
            self.horizontalGroupBox = QGroupBox()
            layout = QGridLayout()
            for x in range(4):
                for y in range(4):
                    btn = QPushButton("")
                    btn.setFixedWidth(150)
                    btn.setFixedHeight(100)
                    btn.setStyleSheet("background-color: slategrey")
                    x_y = [x, y]
                    btn.clicked.connect(self.game_btn_press(x_y))
                    layout.addWidget(btn, x, y)
            self.grid = layout
            self.horizontalGroupBox.setLayout(layout)



