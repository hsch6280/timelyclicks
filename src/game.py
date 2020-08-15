import keyboard
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
import time
from PyQt5.QtCore import  QTimer
from PyQt5.QtWidgets import *
from random import *
end_score = 0
key_layout =[['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
reaction_time_to_level = {
    1: 30,
    0.5: 25,
    2: 20,
    2.5: 15,
    3: 10,
    6: 15,
    7: 10,
    10: 5,
    15: 1,
}

class GameOver(QtWidgets.QWidget):
    global end_score
    def __init__(self):
        super(GameOver, self).__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 0, 0, 30)

        # Updates the highscore if score was higher
        check_highscore(int(end_score))
        # Store highscore in h
        h = display_leaderboard()

        # Displays game over
        game_over_label = QLabel("GAME OVER")
        game_over_label.setFont( QFont('Arial', 16, QFont.Bold))
        game_over_label.setAlignment(QtCore.Qt.AlignCenter)

        # Displays score
        score_label = QLabel(f"Score was: {str(end_score)}")
        score_label.setAlignment(QtCore.Qt.AlignCenter)

        # Displays highscore
        highscore_label = QLabel(f"Highscore is: {h}")
        highscore_label.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(game_over_label)
        layout.addWidget(score_label)
        layout.addWidget(highscore_label)
        self.setLayout(layout)
        self.show()

class GameHome(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GameHome, self).__init__(parent)
        self.game_over = False
        self.correct_btn = []
        self.points = 0
        self.btn_pressed_in_time = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.time_to_press = 50
        self.current_time = 0
        self.last_btn = [0, 0]
        self.level = 0
        self.timer.start(100)
        self.initUI()
        keyboard.on_press(self.key_press)

    def key_press(self, name):
        global key_layout
        if name.name != "unknown":
            if str(name.name) == key_layout[self.correct_btn[0]][self.correct_btn[1]]:
                self.btn_pressed_in_time = True
            else:
                self.game_over = True

    def reset_round(self):
        self.timer.stop()
        self.game_over = False
        self.btn_pressed_in_time = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.current_time = 0
        time.sleep(self.time_to_press/100)
        self.timer.start(100)

    def set_game_over(self):
        global  end_score
        end_score = self.points
        self.timer.stop()
        self.point_label.setParent(None)
        self.horizontalGroupBox.setParent(None)
        self.window_layout.addWidget(GameOver())
    def check_time(self):
        global end_score
        global key_layout
        global reaction_time_to_level
        if not self.game_over:
            if self.current_time > 0:
                if self.btn_pressed_in_time and self.current_time < self.time_to_press:
                    self.points += 1
                    try:
                        self.level = self.points/10
                        if reaction_time_to_level[self.level]:
                            self.time_to_press = reaction_time_to_level[self.level]
                    except KeyError:
                       self.level = self.level
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

    def create_btn(self):
        btn = QPushButton("")
        btn.setFixedWidth(150)
        btn.setFixedHeight(100)
        return btn

    def reset_btn(self):
        global key_layout
        btn = self.create_btn()
        btn.setText(key_layout[self.correct_btn[0]][self.correct_btn[1]])
        btn.setStyleSheet("background-color: slategrey")
        self.grid.addWidget(btn, self.correct_btn[0], self.correct_btn[1])

    def select_btn(self):
        global key_layout
        found_new_btn = False
        while not found_new_btn:
            rand_x = randint(0, 2)
            rand_y = randint(0, 2)
            x_y = [rand_x, rand_y]
            if x_y != self.last_btn:
                self.correct_btn = [rand_x, rand_y]
                self.last_btn  = x_y
                btn = self.create_btn()
                btn.setStyleSheet("background-color: red")
                btn.setText(key_layout[rand_x][rand_y])
                btn.clicked.connect(self.game_btn_press(self.correct_btn))
                self.grid.addWidget(btn, self.correct_btn[0], self.correct_btn[1])
                found_new_btn = True
                self.show()

    def createGridLayout(self):
            global key_layout
            self.horizontalGroupBox = QGroupBox()
            layout = QGridLayout()
            for x, keys in enumerate(key_layout):
                for y, key in enumerate(keys):
                    btn = self.create_btn()
                    btn.setText(str(key))
                    btn.setStyleSheet("background-color: slategrey")
                    x_y = [x,y]
                    btn.clicked.connect(self.game_btn_press(x_y))
                    layout.addWidget(btn, x, y)
            self.grid = layout
            self.horizontalGroupBox.setLayout(layout)

# Function to display the highest score
def display_leaderboard():

    #Open and read the file:
    f = open("src/score.txt", "r")

    highscore = f.read()

    # Return the highscore
    return(highscore)

# Function to check if there is a new highscore
def check_highscore(score):
    #Open and read the file:
    f = open("src/score.txt", "r")

    highscore = f.read()

    # If the score is greater than the highscore
    if int(score) > int(highscore):
        
        # Open the scores file and overwrite the last highscore with the new highscore
        f = open("src/score.txt", "w")
        f.write(str(score))