import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate, QRect
import os


class Homepage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1000)
        app_icon = QtGui.QIcon(os.path.abspath('C:/Moondrift/assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        #  Fix Windowsize
        self.setFixedSize(612, 1000)

        # **GREETING LABEL**
        #### def for different greetings based on time ###
        self.hello_label = QtWidgets.QLabel(self)
        self.hello_label.setText("Good Morning")
        self.hello_label.setObjectName("moondrift_header")


        # **TIME LABEL **
        self.time_label = QtWidgets.QLabel(self)
        self.time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_label.setFont(QFont("Arial", 74, QFont.Bold))
        self.time_label.setStyleSheet("color: #16635B;")

        # **DATE LABEL **
        self.date_label = QtWidgets.QLabel(self)
        self.date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_label.setObjectName("moondrift_h1")
        self.date_label.setGeometry(QRect(0, 0, 0, 0))

        # **Labels Layout **
        layout.addWidget(self.hello_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        layout.addStretch(1)


        # **Timer für Updates**
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Jede Sekunde aktualisieren

        # **Datum initial setzen**
        self.update_date()
        self.update_time()

        self.setLayout(layout)

    def update_date(self):
        """Aktualisiert das Datum"""
        self.date_label.setText(QDate.currentDate().toString("dddd, d MMMM yyyy"))

    def update_time(self):
        """Aktualisiert die Zeit"""
        self.time_label.setText(QTime.currentTime().toString("hh:mm"))
