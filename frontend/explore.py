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
        self.setFixedSize(612, 1000)

        # Set window icon (ensure the path to the icon is correct)
        app_icon = QtGui.QIcon(os.path.abspath('../assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)

        # Set up the layout
        layout = QtWidgets.QVBoxLayout()

        # **Label for Stats Page**
        label = QtWidgets.QLabel("Welcome to Explore!")
        label.setObjectName("moondrift_h1")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center align text
        layout.addWidget(label)

        # Add some space before footer (ensure footer is at the bottom)
        layout.addStretch(1)

        # **Page**
        #nature
        sound_nature_frame = QtWidgets.QFrame(self)
        sound_nature_frame.setGeometry(170, 137, 400, 150)
        sound_nature_frame.setObjectName('explore_sound_frame')

        self.nature_label = QtWidgets.QLabel(sound_nature_frame)
        self.nature_label.setGeometry(250, 0, 150, 150)
        self.nature_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        pixmap_nature = QtGui.QPixmap("..\\assets\\explore\\sound_nature.png")
        self.nature_label.setPixmap(pixmap_nature)
        self.nature_label.setScaledContents(True)

        #animals
        sound_animals_frame = QtWidgets.QFrame(self)
        sound_animals_frame.setGeometry(42, 300, 400, 150)
        sound_animals_frame.setObjectName('explore_sound_frame')

        self.animals_label = QtWidgets.QLabel(sound_animals_frame)
        self.animals_label.setGeometry(0, 0, 150, 150)
        self.animals_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        pixmap_animals = QtGui.QPixmap("..\\assets\\explore\\sound_animal.png")
        self.animals_label.setPixmap(pixmap_animals)
        self.animals_label.setScaledContents(True)

        #asmr
        sound_asmr_frame = QtWidgets.QFrame(self)
        sound_asmr_frame.setGeometry(170, 463, 400, 150)
        sound_asmr_frame.setObjectName('explore_sound_frame')

        self.asmr_label = QtWidgets.QLabel(sound_asmr_frame)
        self.asmr_label.setGeometry(250, 0, 150, 150)
        self.asmr_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        pixmap_asmr = QtGui.QPixmap("..\\assets\\explore\\sound_asmr.png")
        self.asmr_label.setPixmap(pixmap_asmr)
        self.asmr_label.setScaledContents(True)

        #weather
        sound_weather_frame = QtWidgets.QFrame(self)
        sound_weather_frame.setGeometry(42, 626, 400, 150)
        sound_weather_frame.setObjectName('explore_sound_frame')


        self.weather_label = QtWidgets.QLabel(sound_weather_frame)
        self.weather_label.setGeometry(0, 0, 150, 150)
        self.weather_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        pixmap_weather = QtGui.QPixmap("..\\assets\\explore\\sound_weather.png")
        self.weather_label.setPixmap(pixmap_weather)
        self.weather_label.setScaledContents(True)

        # **Footer**
        self.bottom_frame = QtWidgets.QFrame(self)
        self.bottom_frame.setFixedSize(519, 103)  # Fixed size for bottom frame
        # self.bottom_frame.setStyleSheet("background-color: transparent;")
        self.bottom_frame.setStyleSheet("""
            QFrame {
                background-image: url("../assets/footer_explore.png");
                background-repeat: no-repeat;
                background-position: center;
                background-color: transparent;
            }
        """)
        self.bottom_frame.setGeometry(46, 869, 520, 120)  # Set exact position like Homepage (position at bottom)
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



        # Set the layout to this widget
        self.setLayout(layout)