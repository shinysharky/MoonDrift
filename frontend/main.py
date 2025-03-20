import PySide6.QtCore
import sys
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot
from frontend.mainpage import Homepage


class Loadingpage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1000)
        app_icon = QtGui.QIcon(os.path.abspath('C:/Moondrift/assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)
        layout = QtWidgets.QVBoxLayout()

        # Disable fullscreen and resizing
        self.setFixedSize(612, 1000)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)

        ##### GIF #####
        self.giflabel = QtWidgets.QLabel(self)
        self.giflabel.setMinimumSize(QtCore.QSize(500, 500))
        self.giflabel.setMaximumSize(QtCore.QSize(1000, 1000))
        self.giflabel.setAlignment(QtCore.Qt.AlignCenter)

        # Integrate QMovie to the label and initiate the GIF
        self.gif = QMovie('C:/Moondrift/assets/Logo/Videoprojekt.gif')
        self.giflabel.setMovie(self.gif)
        self.gif.start()
        layout.addWidget(self.giflabel)

        ##### LOGO #####
        self.imagelabel = QtWidgets.QLabel(self)
        self.logoname = QtGui.QPixmap('C:/Moondrift/assets/Logo/Group 5 (2).png')
        self.imagelabel.setPixmap(self.logoname)
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.imagelabel)

        layout.addStretch(1)

        ##### Timer Label (Countdown) #####
        self.timer_label = QtWidgets.QLabel("Loading...5 seconds", self)
        self.timer_label.setObjectName("settings_fillout_text")
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.timer_label)

        self.setLayout(layout)

        ##### Timer für den Countdown #####
        self.remaining_time = 5
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        """ Aktualisiert das Timer-Label jede Sekunde """
        if self.remaining_time > 0:
            self.timer_label.setText(f"Loading... {self.remaining_time} seconds")
            self.remaining_time -= 1
        else:
            self.switch_to_next_page()

    def switch_to_next_page(self):
        """ stopps timer and opens next page """
        self.timer.stop()  # Timer stop
        self.next_page = Homepage()  # new page
        self.next_page.show()  # new page open
        self.close()  # close previouse page


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Stylesheet aus einer Datei laden
    with open("style.css", "r", encoding="utf-8") as f:
        stylesheet = f.read()
        app.setStyleSheet(stylesheet)

    window = Loadingpage()
    window.show()
    sys.exit(app.exec())