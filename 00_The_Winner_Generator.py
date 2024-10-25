'''Basics of PyQt5
Dev: Renee Cruz'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()

#main_win.hide()

main_win.setWindowTitle('Winner identifier')
#main_win.move(900, 70)
main_win.resize(400, 200)

but = QPushButton('Generate')
text = QLabel('Click to find out the winner')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    x = randint(1,100)
    winner.setText(str(x))
    text.setText('Winner:')

but.clicked.connect(show_winner)
main_win.show()
app.exec_()

