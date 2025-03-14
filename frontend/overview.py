import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui


class text_overview(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moondrift")
        self.setGeometry(0, 0, 412, 917)
        self.setStyleSheet("background-color: #092139;")
        app_icon = QtGui.QIcon(os.path.abspath('/assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)
        layout = QtWidgets.QVBoxLayout()

        # Header
        self.header = QtWidgets.QLabel("This is the Header", alignment=QtCore.Qt.AlignLeft)
        self.header.setObjectName("moondrift_header")
        layout.addWidget(self.header)

        # H1
        self.h1 = QtWidgets.QLabel("This is h1", alignment=QtCore.Qt.AlignLeft)
        self.h1.setObjectName("moondrift_h1")
        layout.addWidget(self.h1)

        # Home Button
        self.home_button = QtWidgets.QLabel("This is Home Button Text", alignment=QtCore.Qt.AlignLeft)
        self.home_button.setObjectName("home_buttons")
        layout.addWidget(self.home_button)

        # Stats Diagram Text Stats
        self.diagram_stats = QtWidgets.QLabel("This is Stats Diagram", alignment=QtCore.Qt.AlignLeft)
        self.diagram_stats.setObjectName("stats_diagram_text_stats")
        layout.addWidget(self.diagram_stats)

        # Stats Diagram Text Date
        self.diagram_date = QtWidgets.QLabel("This is Stats Diagram", alignment=QtCore.Qt.AlignLeft)
        self.diagram_date.setObjectName("stats_diagram_text_date")
        layout.addWidget(self.diagram_date)

        # Explore Sound Text
        self.sound_text = QtWidgets.QLabel("This is Explore Sound Text", alignment=QtCore.Qt.AlignLeft)
        self.sound_text.setObjectName("explore_sound_text")
        layout.addWidget(self.sound_text)

        # Explore Artist Text
        self.artist_text = QtWidgets.QLabel("This is Explore Artist Text", alignment=QtCore.Qt.AlignLeft)
        self.artist_text.setObjectName("explore_artist_text")
        layout.addWidget(self.artist_text)

        # Profile Text Description
        self.description_text = QtWidgets.QLabel("This is Profile Text Description", alignment=QtCore.Qt.AlignLeft)
        self.description_text.setObjectName("profile_text_description")
        layout.addWidget(self.description_text)

        # Settings Header
        self.settings_header = QtWidgets.QLabel("This is Settings Header", alignment=QtCore.Qt.AlignLeft)
        self.settings_header.setObjectName("settings_header")
        layout.addWidget(self.settings_header)

        # Settings h1
        self.settings_h1 = QtWidgets.QLabel("This is settings_h1", alignment=QtCore.Qt.AlignLeft)
        self.settings_h1.setObjectName("settings_h1")
        layout.addWidget(self.settings_h1)

        # Settings text
        self.settings_text = QtWidgets.QLabel("This is settings_text", alignment=QtCore.Qt.AlignLeft)
        self.settings_text.setObjectName("settings_text")
        layout.addWidget(self.settings_text)

        # settings_fillout_text
        self.settings_fillout_text = QtWidgets.QLabel("This is settings_fillout_text", alignment=QtCore.Qt.AlignLeft)
        self.settings_fillout_text.setObjectName("settings_fillout_text")
        layout.addWidget(self.settings_fillout_text)

        # settings_button_text
        self.settings_button_text = QtWidgets.QLabel("This is settings_button_text", alignment=QtCore.Qt.AlignLeft)
        self.settings_button_text.setObjectName("settings_button_text")
        layout.addWidget(self.settings_button_text)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Stylesheet aus einer Datei laden
    with open("style.css", "r", encoding="utf-8") as f:
        stylesheet = f.read()
        app.setStyleSheet(stylesheet)  # Das Stylesheet anwenden

    window = text_overview()
    window.show()
    sys.exit(app.exec())