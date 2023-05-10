
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class guiApp (QDialog):
    def __init__(self, parent = None):
        super(guiApp, self).__init__(parent)
        self.tag = QLabel('< font color = "blue", size = "+5" > About PyQt Classes </font>')
        button = QPushButton('Click Here')
        button.clicked.connect(self.textUpdate)
        box = QVBoxLayout()
        box.addWidget(self.tag)
        box.addWidget(button)
        self.setLayout(box)
        self.setWindowTitle("Visual Programming Example")
        self.resize(300, 400)
        self.move(200, 50) 
        
    def textUpdate(self):
        self.tag.setText ('< font color ="red", size = "+3" > Button Clicked </font>')   
          
app = QApplication([])
window = guiApp()
window.show()
app.exec_()
