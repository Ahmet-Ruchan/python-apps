from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class guiApp2 (QDialog):
    def __init__(self, parent = None):
        super(guiApp2, self).__init__(parent)
        self.font = 3
        self.text = '<center><font color = "blue" size = "+%d"> Visual Programming </font></center>'
        self.tag = QLabel(self.text % self.font)
        buttonShrink = QPushButton("Zoom Out")
        buttonShrink.clicked.connect(self.zoomOut)
        buttonZoom = QPushButton("Zoom In")
        buttonZoom.clicked.connect(self.zoomIn)
        grid = QGridLayout()
        grid.addWidget(self.tag, 0,0,1,2)
        grid.addWidget(buttonShrink, 1,0,1,1)
        grid.addWidget(buttonZoom, 1,1,1,1)
        self.setLayout(grid)
        self.setWindowTitle('PyQt Grid')
        self.resize(500, 100)
    
    def zoomIn (self):
        if self.font <= 5:
            self.font = self.font + 1
            self.tag.setText(self.text % self.font) 
            print (self.font)
            
    def zoomOut(self):
        if self.font >= 1:
            self.font = self.font - 1
            self.tag.setText(self.text % self.font) 
            print (self.font)
                
app = QApplication([])     
window = guiApp2()
window.show()
app.exec_()
