from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()

#main_win.hide()

main_win.setWindowTitle('Winner identifier')
#main_win.move(900, 70)
main_win.resize(400, 200)

question = QLabel('What year was Algorithmics founded in?')

btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)

main_win.show()
app.exec_()