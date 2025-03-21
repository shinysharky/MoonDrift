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

        self.bottom_frame = QtWidgets.QFrame(self.footerimg_label)
        self.bottom_frame.setFixedSize(519, 103)
        self.bottom_frame.setStyleSheet("background-color: transparent;")

        def home_button_click():
            print("switched to Homepage")

        def stats_button_click():
            from frontend.statistics import Stats
            self.next_page = Stats()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the main window to switch pages
            print("switched to Statistics")

        def explore_button_click():
            from frontend.explore import Explore
            self.next_page = Explore()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the main window to switch pages
            print("switched to Explore")

        def profile_button_click():
            from frontend.profile import Profile
            self.next_page = Profile()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the main window to switch pages
            print("switched to Statistics")

        home_button = QtWidgets.QPushButton(self.bottom_frame)
        home_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        home_button_radius = QtCore.QSize(75, 79)
        home_button.setFixedSize(75, 75)  # Ensure width & height are the same
        home_button.setFixedSize(home_button_radius)
        home_button.setGeometry(91, 12, 75, 75)
        home_button.setObjectName("footerButton")

        home_button.clicked.connect(home_button_click)

        stats_button = QtWidgets.QPushButton(self.bottom_frame)
        stats_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        stats_button_radius = QtCore.QSize(75, 79)
        stats_button.setFixedSize(75, 75)  # Ensure width & height are the same
        stats_button.setFixedSize(stats_button_radius)
        stats_button.setGeometry(203, 12, 75, 75)
        stats_button.setObjectName("footerButton")

        stats_button.clicked.connect(stats_button_click)

        explore_button = QtWidgets.QPushButton(self.bottom_frame)
        explore_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        explore_button_radius = QtCore.QSize(75, 79)
        explore_button.setFixedSize(75, 75)  # Ensure width & height are the same
        explore_button.setFixedSize(explore_button_radius)
        explore_button.setGeometry(316, 12, 75, 75)
        explore_button.setObjectName("footerButton")

        explore_button.clicked.connect(explore_button_click)

        profile_button = QtWidgets.QPushButton(self.bottom_frame)
        profile_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        profile_button_radius = QtCore.QSize(75, 79)
        profile_button.setFixedSize(75, 75)  # Ensure width & height are the same
        profile_button.setFixedSize(profile_button_radius)
        profile_button.setGeometry(444, 12, 75, 75)
        profile_button.setObjectName("footerButton")

        profile_button.clicked.connect(profile_button_click)

        button_layout = QtWidgets.QHBoxLayout(self.bottom_frame)
        button_layout.setContentsMargins(1, 1, 1, 1)
        button_layout.setSpacing(15)  # Space between the buttons
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

