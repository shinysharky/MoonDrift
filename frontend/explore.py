import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate, QRect
import os

class Explore(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Moondrift")

        # Set window geometry (x, y, width, height)
        self.setGeometry(0, 0, 612, 1000)

        # Set window icon (ensure the path to the icon is correct)
        app_icon = QtGui.QIcon(os.path.abspath('C:/Moondrift/assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)

        # Set up the layout
        layout = QtWidgets.QVBoxLayout()

        # Create and configure a label for demonstration
        label = QtWidgets.QLabel("Welcome to Explore!")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center align text

        # Add the label to the layout
        layout.addWidget(label)

        # Set the layout for this widget
        self.setLayout(layout)