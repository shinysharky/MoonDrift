import PySide6.QtCore
import sys
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow


class MoonDrift(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1017)
        app_icon = QtGui.QIcon(os.path.abspath('C:\Moondrift/assets/Logo.ico'))  # Hier den Pfad zu deinem Icon angeben
        self.setWindowIcon(app_icon)
        self.setStyleSheet("background-color: #092139;")
        layout = QtWidgets.QVBoxLayout()

        # Setze den Abstand zwischen den Widgets auf einen kleinen Wert (z.B. 5)
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
        self.welcome.setStyleSheet("padding: 0; margin: 5;")
        layout.addWidget(self.info)

        layout.addStretch(1)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Stylesheet aus einer Datei laden
    with open("style.css", "r", encoding="utf-8") as f:
        stylesheet = f.read()
        app.setStyleSheet(stylesheet)  # Das Stylesheet anwenden

    window = MoonDrift()
    window.show()
    sys.exit(app.exec())