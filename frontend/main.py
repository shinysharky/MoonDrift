import PySide6.QtCore
import sys
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot


class MoonDrift(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1017)
        app_icon = QtGui.QIcon(os.path.abspath('C:/Moondrift/assets/Logo.ico'))
        self.setWindowIcon(app_icon)
        layout = QtWidgets.QVBoxLayout()

        # Disable fullscreen and resizing
        self.setFixedSize(612, 1017)

        # Set the spacing and margins
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Header
        self.header = QtWidgets.QLabel("Hello Sleepy(˶ᵔ ᵕ ᵔ˶)", alignment=QtCore.Qt.AlignCenter)
        self.header.setObjectName("moondrift_header")
        self.header.setStyleSheet("padding: 0; margin: 5;")
        layout.addWidget(self.header)

        # Welcome
        self.welcome = QtWidgets.QLabel("Welcome to Moondrift૮₍ ˃ ⤙ ˂ ₎ა", alignment=QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("moondrift_h1")
        self.welcome.setStyleSheet("padding: 0; margin: 5;")
        layout.addWidget(self.welcome)

        # Info
        self.info = QtWidgets.QLabel(
            "Sadly there is not much here yet, check out the read me for more info( •̯́ ₃ •̯̀) ",
            alignment=QtCore.Qt.AlignCenter)
        self.info.setObjectName("settings_text")
        self.info.setStyleSheet("padding: 0; margin: 5;")
        layout.addWidget(self.info)

        ### Button Layout (Horizontal Layout) ###
        button_layout = QtWidgets.QHBoxLayout()  # Create a horizontal layout for buttons
        button_layout.setSpacing(50)

        # Define button click action
        @Slot()
        def button_click():
            print("button clicked")

        # Create two buttons
        start_sleep = QPushButton("Start Sleep")
        start_sleep.setObjectName("start_sleep")
        start_sleep.setMinimumSize(20, 30)
        start_sleep.setMaximumSize(112, 40)
        start_sleep.clicked.connect(button_click)

        set_alarm = QPushButton("Set Alarm")
        set_alarm.setObjectName("set_alarm")
        set_alarm.setMinimumSize(100, 30)
        set_alarm.setMaximumSize(112, 40)
        set_alarm.clicked.connect(button_click)

        # Add the buttons to the horizontal layout
        button_layout.addWidget(start_sleep)
        button_layout.addWidget(set_alarm)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        ##### GIF ####
        self.giflabel = QtWidgets.QLabel(self)
        self.giflabel.setMinimumSize(QtCore.QSize(500, 500))
        self.giflabel.setMaximumSize(QtCore.QSize(1000, 1000))
        self.giflabel.setAlignment(QtCore.Qt.AlignCenter)

        # Integrate QMovie to the label and initiate the GIF
        self.gif = QMovie('C:/Moondrift/assets/test.gif')
        self.giflabel.setMovie(self.gif)
        self.gif.start()
        # Add the GIF label to the layout
        layout.addWidget(self.giflabel)

        layout.addStretch(1)

        ### Loading Gif ###
        self.loadinggiflabel = QtWidgets.QLabel(self)
        self.loadinggiflabel.setMinimumSize(QtCore.QSize(200, 200))
        self.loadinggiflabel.setMaximumSize(QtCore.QSize(1000, 1000))
        self.loadinggiflabel.setAlignment(QtCore.Qt.AlignCenter)

        # Integrate QMovie to the label and initiate the GIF
        self.loadinggif = QMovie('C:/Moondrift/assets/Eclipse@1x-0.7s-200px-200px (1).gif')
        self.loadinggiflabel.setMovie(self.loadinggif)
        self.loadinggif.start()
        # Add the GIF label to the layout
        layout.addWidget(self.loadinggiflabel)

        self.setLayout(layout)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Stylesheet aus einer Datei laden
    with open("style.css", "r", encoding="utf-8") as f:
        stylesheet = f.read()
        app.setStyleSheet(stylesheet)  # Das Stylesheet anwenden

    window = MoonDrift()
    window.show()
    sys.exit(app.exec())