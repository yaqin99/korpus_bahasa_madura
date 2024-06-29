# from PyQt5 import QtGui , QtCore , QtWidgets 

# from PyQt5.QtGui import * 
# from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication , QPushButton , QLabel, QWidget

app = QApplication([])
window = QWidget()
label = QLabel(window) #maksudnya masukin kedalam window
label.setText("ini adalah label bro")
label.move(200 , 0)

button = QPushButton(window) #ini maksudanya masukan kedalam button bro
button.setText("ini adalah button bro")
window.show()

app.exec()