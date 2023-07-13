import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        # Initialising the window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = ""
        self.password = ""
        self.ui.stackedWidget.setCurrentIndex(0)


        # Start assigning functions to widgets here
        self.ui.loginButton.clicked.connect(self.logUserIn)
        self.ui.usernameLineEdit.textChanged.connect(self.setUsername)
        self.ui.passwordLineEdit.textChanged.connect(self.setPassword)


    def logUserIn(self):
        if self.username == "admin" and self.password == "admin":
            self.ui.stackedWidget.setCurrentIndex(1)

    def setUsername(self, s):
        self.username = s

    def setPassword(self, s):
        self.password = s


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())