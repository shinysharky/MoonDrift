import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate, QRect
import os


#•······················•✦•······················•✦
class Homepage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1000)
        app_icon = QtGui.QIcon(os.path.abspath('../assets/Logo/Logo.ico'))
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

    # **DATE LABEL**✦•······················•✦•······················•✦
        self.date_label = QtWidgets.QLabel(self)
        self.date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_label.setObjectName("moondrift_h1")

    # **Labels Layout**✦•······················•✦•······················•✦
        layout.addLayout(hbox)
        layout.addSpacing(10)
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        layout.addStretch(1)

    # **Timer for Updates**✦•······················•✦•······················•✦
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.timeout.connect(self.update_text)
        self.timer.start(1000)

    # **Footer**✦•······················•✦•······················•✦
        self.bottom_frame = QtWidgets.QFrame(self)
        self.bottom_frame.setFixedSize(519, 103)  # Fixed size for bottom frame
        self.bottom_frame.setStyleSheet("""
                    QFrame {
                        background-image: url("C:/Moondrift/assets/footer_home.png");
                        background-repeat: no-repeat;
                        background-position: center;
                        background-color: transparent;
                    }
                """)
        self.bottom_frame.setGeometry(46, 869, 520, 120)  # Set exact position like Homepage (position at bottom)

        # Make sure the bottom frame and buttons are fixed by not relying on layouts
        self.bottom_frame.setLayout(None)  # No layout manager for the bottom frame

    # **Buttons in the footer**✦•······················•✦•······················•✦
        def home_button_click():
            print("switched to Homepage")

        def stats_button_click():
            from frontend.statistics import Stats
            self.next_page = Stats()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the Stats window to switch pages
            print("switched to Stats")

        def explore_button_click():
            from frontend.explore import Explore
            self.next_page = Explore()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the Stats window to switch pages
            print("switched to Explore")

        def profile_button_click():
            from frontend.profile import Profile
            self.next_page = Profile()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the Stats window to switch pages
            print("switched to Profile")

        # Home Button
        home_button = QtWidgets.QPushButton(self.bottom_frame)
        home_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        home_button.setFixedSize(75, 75)
        home_button.setGeometry(44, 7, 75, 75)
        home_button.setObjectName("footerButton")
        home_button.clicked.connect(home_button_click)

        # Stats Button
        stats_button = QtWidgets.QPushButton(self.bottom_frame)
        stats_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        stats_button.setFixedSize(75, 75)
        stats_button.setGeometry(156, 7, 75, 75)
        stats_button.setObjectName("footerButton")
        stats_button.clicked.connect(stats_button_click)

        # Explore Button
        explore_button = QtWidgets.QPushButton(self.bottom_frame)
        explore_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        explore_button.setFixedSize(75, 75)
        explore_button.setGeometry(269, 7, 75, 75)
        explore_button.setObjectName("footerButton")
        explore_button.clicked.connect(explore_button_click)

        # Profile Button
        profile_button = QtWidgets.QPushButton(self.bottom_frame)
        profile_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        profile_button.setFixedSize(75, 75)
        profile_button.setGeometry(398, 7, 75, 75)
        profile_button.setObjectName("footerButton")
        profile_button.clicked.connect(profile_button_click)


        # **Initialize Date and Time**
        self.update_date()
        self.update_time()
        self.update_text()

        self.setLayout(layout)

###function to display greeting based on time✦•······················•✦•······················•✦
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

###function to update time and date based on local time/date✦•······················•✦•······················•✦
    def update_date(self):
        """Update the date label."""
        self.date_label.setText(QDate.currentDate().toString("dddd, d MMMM yyyy"))

    def update_time(self):
        """Update the time label."""
        self.time_label.setText(QTime.currentTime().toString("hh:mm"))

