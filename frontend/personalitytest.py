from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import os

class personalitytest_popup(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("which personality are you?")
        app_icon = QtGui.QIcon(os.path.abspath('../assets/Logo/Logo.ico'))
        self.setWindowIcon(app_icon)
        self.setGeometry(100, 100, 600, 250)
        self.setStyleSheet("background-color: #092139;")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Persönlichkeitstypen-Score
        self.scores = {
            "Worker": 0,
            "Visionary": 0,
            "Dreamer": 0,
            "Realist": 0,
            "Lover": 0,
            "Sleeper": 0
        }

        ## Questions in German
        # self.questions = [
        #     "Ich verfolge klare Ziele und arbeite konsequent darauf hin.",
        #     "Ich denke oft über die Zukunft und neue Ideen nach.",
        #     "Ich verliere mich gerne in meiner eigenen Fantasie.",
        #     "Ich zeige meine Gefühle offen und spreche gern darüber.",
        #     "Ich halte mich lieber an bewährte Methoden als Neues auszuprobieren.",
        #     "Ich schlafe regelmäßig länger als geplant.",
        #     "Ich glaube, dass harte Arbeit wichtiger ist als Talent.",
        #     "Ich bin schon mal ein Risiko eingegangen, nur weil es sich richtig angefühlt hat.",
        #     "Ich lege viel Wert auf Ordnung und Struktur in meinem Alltag.",
        #     "Ich vertraue meinem Bauchgefühl mehr als harten Fakten.",
        #     "Ich gehe auf die Gefühle anderer ein, selbst wenn ich selbst nicht in Stimmung bin.",
        #     "Ich finde, dass ein Traum auch ohne Realitätsbezug wichtig sein kann.",
        #     "Ich motiviere und inspiriere gerne andere.",
        #     "Ich finde, dass man sich nur verändern sollte, wenn es wirklich notwendig ist.",
        #     "Ich würde mich selbst als empathisch bezeichnen.",
        #     "Ich werde unruhig, wenn ich zu lange nichts Produktives mache.",
        #     "Ich verbringe gerne Zeit allein mit meinen Gedanken.",
        #     "Ich schiebe Aufgaben oft auf und gönne mir lieber noch ein Nickerchen.",
        #     "Ich suche ständig nach neuen Projekten oder Herausforderungen.",
        #     "Ich tue mir schwer mit Veränderungen, selbst wenn ich weiß, dass sie gut wären."
        # ]

        self.questions = [
            "I pursue clear goals and work consistently towards them.",
            "I often think about the future and new ideas",
            "I tend to get lost in my own imagination.",
            "I openly express my feelings and speak about them",
            "I prefer sticking to proven methods rather than trying new things",
            "I regularly sleep longer than I should",
            "I believe hard work is more important than talent.",
            "I have taken a risk just because it felt right.",
            "I place great value on order and structure in my daily life.",
            "I trust my gut feeling more than hard facts.",
            "I am sensitive to others' feelings, even when I am not in the mood myself.",
            "I believe that a dream can be important even without a connection to reality.",
            "I enjoy motivating and inspiring others.",
            "I think change should only happen when it's really necessary.",
            "I would describe myself as empathetic.",
            "I become restless when I haven't done anything productive for a while.",
            "I enjoy spending time alone with my thoughts.",
            "I often procrastinate and prefer taking a nap instead.",
            "I am constantly looking for new projects or challenges.",
            "I find it hard to deal with changes, even when I know they would be beneficial."
        ]
        # Personality for each Question
        self.question_types = [
            ["Worker"],
            ["Visionary"],
            ["Dreamer"],
            ["Lover"],
            ["Realist"],
            ["Sleeper"],
            ["Worker"],
            ["Visionary", "Dreamer"],
            ["Worker", "Realist"],
            ["Dreamer", "Lover"],
            ["Lover"],
            ["Dreamer"],
            ["Visionary"],
            ["Realist"],
            ["Lover"],
            ["Worker"],
            ["Dreamer", "Realist"],
            ["Sleeper"],
            ["Visionary"],
            ["Realist", "Sleeper"]
        ]

        self.current_question = 0

        # GUI-Elemente
        self.question_label = QLabel(self.questions[self.current_question])
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setObjectName("settings_h1")
        self.layout.addWidget(self.question_label)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)  # This centers the buttons horizontally

        self.yes_button = QPushButton("yes")
        self.yes_button.clicked.connect(self.answer_yes)
        self.yes_button.setStyleSheet("background-color: #0F4149;")
        self.yes_button.setObjectName('yes_no_button')
        button_layout.addWidget(self.yes_button)

        self.no_button = QPushButton("no")
        self.no_button.clicked.connect(self.answer_no)
        self.no_button.setStyleSheet("background-color: #0F4149;")
        self.no_button.setObjectName('yes_no_button')
        button_layout.addWidget(self.no_button)

        # Add the button layout to the main layout
        self.layout.addLayout(button_layout)

    def answer_yes(self):
        types = self.question_types[self.current_question]
        for t in types:
            self.scores[t] += 1
        self.next_question()

    def answer_no(self):
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.setText(self.questions[self.current_question])
        else:
            self.show_result()

    def restart_quiz(self):
        # sets back score
        for key in self.scores:
            self.scores[key] = 0

        self.current_question = 0
        self.question_label.setText(self.questions[0])

        self.yes_button.setEnabled(True)
        self.no_button.setEnabled(True)
        self.yes_button.setVisible(True)
        self.no_button.setVisible(True)
        self.restart_button.setVisible(False)

    def show_result(self):
        best_match = max(self.scores, key=self.scores.get)

        descriptions = {
            "Worker": "Ｔｈｅ Ｗｏｒｋｅｒ\n‿̩͙⊱༒︎༻♱༺༒︎⊰‿̩\nWorkers are dedicated and dependable, always striving to meet their goals. They take pride in their effort and believe in the value of discipline and persistence. Practical and focused, they prioritize results and consistency. Workers support change only when it improves efficiency.",
            "Visionary": "𝙏𝙝𝙚 𝙑𝙞𝙨𝙞𝙤𝙣𝙖𝙧𝙮\n‿̩͙⊱༒︎༻♱༺༒︎⊰‿̩\nVisionaries are driven by big ideas and future possibilities. They inspire those around them with their creativity and ambition. They are imaginative and open-minded, always seeking growth and innovation. Visionaries embrace change and take risks, believing in the power of bold dreams.",
            "Dreamer": "𝘛𝘩𝘦 𝘋𝘳𝘦𝘢𝘮𝘦𝘳\n‿̩͙⊱༒︎༻♱༺༒︎⊰‿̩\nDreamers are guided by their inner world and endless imagination. They see beauty and potential everywhere and believe in following their passions. They are idealistic and hopeful, often prioritizing their dreams over practical concerns. Dreamers value creativity and emotional depth.",
            "Realist": "𝐓𝐡𝐞 𝐑𝐞𝐚𝐥𝐢𝐬𝐭\n‿̩͙⊱༒︎༻♱༺༒︎⊰‿̩\nRealists are loyal to the people around them and work hard to keep their promises. They are honest and straightforward with others and expect the same in return. Realists believe in standard procedures and will only support change when there is a demonstrable benefit.",
            "Lover": "𝒯𝒽𝑒 𝐿𝑜𝓋𝑒𝓇\n‿̩͙⊱༒︎༻♱༺༒︎⊰‿̩\nLovers are compassionate and deeply connected to the people around them. They prioritize relationships and express their care through kindness and support. Warm and empathetic, they value harmony and emotional connection. Lovers embrace change when it strengthens bonds.",
            "Sleeper": "TᕼE ᔕᒪEEᑭEᖇ-ᗷᑌIᒪᗪ\n‿̩͙⊱༒︎༻♱༺༒︎⊰‿̩\nYou just too good at sleeping bro, get help."
        }

        result = descriptions.get(best_match, "unknown perosnality...maybe autism?")

        self.question_label.setText(result)
        self.yes_button.setDisabled(True)
        self.no_button.setDisabled(True)
        self.yes_button.setVisible(False)
        self.no_button.setVisible(False)

        self.restart_button = QPushButton("do quiz again?")
        self.restart_button.clicked.connect(self.restart_quiz)
        self.restart_button.setVisible(False)
        self.layout.addWidget(self.restart_button)

        self.restart_button.setVisible(True)
        print(self.scores)

