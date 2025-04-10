import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate, QRect
import os

from frontend.personalitytest import personalitytest_popup


class Profile(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Moondrift")

        # Set window geometry (x, y, width, height)
        self.setFixedSize(612, 1000)
        # Set window icon (ensure the path to the icon is correct)
        app_icon = QtGui.QIcon(os.path.abspath('../assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)

        # Set up the layout
        main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(main_layout)

        # **Label for Profile Page**
        label = QtWidgets.QLabel("Welcome to Profile!")
        label.setObjectName("moondrift_h1")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label, alignment=QtCore.Qt.AlignCenter)  # ← Add directly to main_layout

        main_layout.addStretch(1)

    # **Page**✦•······················•✦•······················•✦
        self.placeholer_frame = QtWidgets.QFrame(self)
        self.placeholer_frame.setFixedSize(500, 500)
        self.placeholer_frame.setStyleSheet(
            "background-color: transparent;"
            "border: 0px;"
            "border-radius: 0px;"
        )

        # Add the frame to the layout and center it
        main_layout.addWidget(self.placeholer_frame, alignment=QtCore.Qt.AlignCenter)

    ###function to open personality test✦•······················•✦•······················•✦
        def personality_button_click():
            from frontend.personalitytest import personalitytest_popup
            self.next_page = personalitytest_popup()  # instantiate the QWidget subclass
            self.next_page.show()  # show the popup window
            print("popup shown")


        personality_button = QtWidgets.QPushButton("start test", self.placeholer_frame)
        personality_button.setFixedSize(500, 500)
        personality_button.setGeometry(0, 0, 500, 500)
        personality_button.setObjectName("QPushButton")
        personality_button.clicked.connect(personality_button_click)

        main_layout.addStretch(2)

    # **Footer**✦•······················•✦•······················•✦
        self.bottom_frame = QtWidgets.QFrame(self)
        self.bottom_frame.setFixedSize(519, 103)  # Fixed size for bottom frame
        # self.bottom_frame.setStyleSheet("background-color: transparent;")
        self.bottom_frame.setStyleSheet("""
                    QFrame {
                        background-image: url("../assets/footer_profile.png");
                        background-repeat: no-repeat;
                        background-position: center;
                        background-color: transparent;
                    }
                """)
        self.bottom_frame.setGeometry(46, 869, 520, 120)  # Set exact position like Homepage (position at bottom)

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

        # Set the layout to this widget
        self.setLayout(main_layout)