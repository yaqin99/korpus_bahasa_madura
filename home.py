from PyQt5 import QtGui , QtCore , QtWidgets 

from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 

app = QApplication([])
window = QPushButton("My Button")
window.show()

app.exec()