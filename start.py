from PyQt5 import QtWidgets
import sys
from src.home import Home
def main():
    app = QtWidgets.QApplication([])
    home = Home()
    home.setWindowTitle("Welcome!")
    home.show()

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
