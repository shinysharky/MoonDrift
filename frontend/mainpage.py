import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate, QRect
import os


class Homepage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1000)
        app_icon = QtGui.QIcon(os.path.abspath('C:/Moondrift/assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)

        # Main layout (Vertical)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Horizontal layout for hello_label
        hbox = QtWidgets.QHBoxLayout()

        # Fix Window Size
        self.setFixedSize(612, 1000)

        # **GREETING LABEL**
        self.hello_label = QtWidgets.QLabel(self)
        self.hello_label.setObjectName("moondrift_header")

        # Add spacing before the greeting label
        hbox.addSpacing(50)  # Adjust this value for left spacing
        hbox.addWidget(self.hello_label)
        hbox.addSpacing(50)  # Adjust this value for right spacing

        layout.addSpacing(50)

        # **TIME LABEL**
        self.time_label = QtWidgets.QLabel(self)
        self.time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_label.setFont(QFont("Arial", 74, QFont.Bold))
        self.time_label.setStyleSheet("color: #16635B;")

        # **DATE LABEL**
        self.date_label = QtWidgets.QLabel(self)
        self.date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_label.setObjectName("moondrift_h1")

        # **Labels Layout**
        layout.addLayout(hbox)
        layout.addSpacing(10)
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        layout.addStretch(1)

        # **Timer for Updates**
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.timeout.connect(self.update_text)
        self.timer.start(1000)

        # **Footer**
        self.footerimg_label = QtWidgets.QLabel(self)
        self.footerimg = QtGui.QPixmap('C:/Moondrift/assets/footer_home.png')
        self.footerimg_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.footerimg_label.setPixmap(self.footerimg)
        layout.addWidget(self.footerimg_label)

        # **Initialize Date and Time**
        self.update_date()
        self.update_time()
        self.update_text()

        self.setLayout(layout)

    def update_text(self):
        """Update text based on the current time."""
        current_time = QTime.currentTime()
        hour = current_time.hour()

        if 6 <= hour < 12:
            self.hello_label.setText("Good morning!")
        elif 12 <= hour < 14:
            self.hello_label.setText("Hello!")
        elif 14 <= hour < 18:
            self.hello_label.setText("Good afternoon!")
        elif 18 <= hour < 22:
            self.hello_label.setText("Good evening!")
        else:
            self.hello_label.setText("Good night!")

    def update_date(self):
        """Update the date label."""
        self.date_label.setText(QDate.currentDate().toString("dddd, d MMMM yyyy"))

    def update_time(self):
        """Update the time label."""
        self.time_label.setText(QTime.currentTime().toString("hh:mm"))

