from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication, QMovie, QPainter, QLinearGradient, QColor, QFont, QBrush, QPainterPath
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Slot, QTimer, QTime, QDate
import os


class Homepage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 612, 1000)
        app_icon = QtGui.QIcon(os.path.abspath('C:/Moondrift/assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)

        # Disable fullscreen and resizing
        self.setFixedSize(612, 1000)

        # Create a QTimer that updates the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        self.current_time = QTime.currentTime().toString("hh:mm")
        self.update()  # Trigger an initial paint event

        # Add additional text below the time label (not in paintEvent)
        self.additional_text_label = QtWidgets.QLabel("This is additional text", self)
        self.additional_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.additional_text_label.setStyleSheet("font: bold 24pt Arial; color: white;")
        layout.addWidget(self.additional_text_label)

    def update_time(self):
        """Updates the time and triggers repaint"""
        self.current_time = QTime.currentTime().toString("hh:mm")
        self.update()  # Force repaint to trigger paintEvent

    def paintEvent(self, event):
        """Custom paint event to draw text with gradient"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Set font properties
        font = QFont("Arial", 74, QFont.Bold)
        painter.setFont(font)

        # Get text size and position it in the center
        text = self.current_time
        font_metrics = painter.fontMetrics()
        text_width = font_metrics.horizontalAdvance(text)
        text_height = font_metrics.height()
        x = (self.width() - text_width) // 2
        y = (self.height() + text_height) // 2 - 200

        # Create a path for the text
        path = QPainterPath()
        path.addText(x, y, font, text)

        # Set up gradient (match text width)
        gradient = QLinearGradient(x, 0, x + text_width, 0)
        gradient.setColorAt(0, QColor("#16635B"))
        gradient.setColorAt(1, QColor("#113953"))

        # Apply gradient brush
        brush = QBrush(gradient)
        painter.setBrush(brush)
        painter.setPen(QtCore.Qt.PenStyle.NoPen)  # No outline

        # Draw the text
        painter.drawPath(path)