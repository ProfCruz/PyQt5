from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Quiz')
#main_win.resize(600,400)

#main_win.setLayout()

main_win.show()
#main_win.hide()
app.exec_()