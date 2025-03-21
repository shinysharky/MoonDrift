import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate, QRect
import os


class Stats(QtWidgets.QWidget):
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

        # **Label for Stats Page**
        label = QtWidgets.QLabel("Welcome to Stats!")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center align text
        layout.addWidget(label)

        # Add some space before footer (ensure footer is at the bottom)
        layout.addStretch(1)

        # **Footer**
        self.footerimg_label = QtWidgets.QLabel(self)
        self.footerimg = QtGui.QPixmap('C:/Moondrift/assets/footer_home.png')
        self.footerimg_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.footerimg_label.setPixmap(self.footerimg)

        # Bottom Frame for footer buttons (this should match the layout from Homepage)
        self.bottom_frame = QtWidgets.QFrame(self)
        self.bottom_frame.setFixedSize(519, 103)  # Fixed size for bottom frame
        self.bottom_frame.setStyleSheet("background-color: transparent;")
        self.bottom_frame.setGeometry(46, 897, 519, 103)  # Set exact position like Homepage (position at bottom)

        # Make sure the bottom frame and buttons are fixed by not relying on layouts
        self.bottom_frame.setLayout(None)  # No layout manager for the bottom frame

        # **Buttons in the footer**

        def home_button_click():
            from frontend.mainpage import Homepage
            self.next_page = Homepage()
            self.next_page.show()  # Show the Stats page
            self.close()  # Optionally, close the Stats window to switch pages
            print("switched to Homepage")

        def stats_button_click():
            print("switched to Statistics")

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
        home_button.setGeometry(91, 12, 75, 75)
        home_button.setObjectName("footerButton")
        home_button.clicked.connect(home_button_click)

        # Stats Button
        stats_button = QtWidgets.QPushButton(self.bottom_frame)
        stats_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        stats_button.setFixedSize(75, 75)
        stats_button.setGeometry(203, 12, 75, 75)
        stats_button.setObjectName("footerButton")
        stats_button.clicked.connect(stats_button_click)

        # Explore Button
        explore_button = QtWidgets.QPushButton(self.bottom_frame)
        explore_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        explore_button.setFixedSize(75, 75)
        explore_button.setGeometry(316, 12, 75, 75)
        explore_button.setObjectName("footerButton")
        explore_button.clicked.connect(explore_button_click)

        # Profile Button
        profile_button = QtWidgets.QPushButton(self.bottom_frame)
        profile_button.setAttribute(QtCore.Qt.WidgetAttribute.WA_Hover, True)
        profile_button.setFixedSize(75, 75)
        profile_button.setGeometry(444, 12, 75, 75)
        profile_button.setObjectName("footerButton")
        profile_button.clicked.connect(profile_button_click)

        # Add the footer image to the layout
        layout.addWidget(self.footerimg_label)

        # Set the layout to this widget
        self.setLayout(layout)
