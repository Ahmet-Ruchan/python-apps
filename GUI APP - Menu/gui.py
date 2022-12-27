from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class guiApp3 (QDialog):
    
    def __init__(self, parent = None):

        super(guiApp3, self).__init__(parent)
        self.height = 2
        self.types = {0:'Arial', 1:'Times New Roman', 2:'Verdana', 3:'Comic Sans MS'}
        self.text_type = self.types[0]
        self.text = '<center><font color = "blue" size = "+%d" face = "%s"> Visual programming, changing font and size. </font></center>'
        self.tag = QLabel(self.text % (self.height, self.text_type))

        grid = QGridLayout()
        grid.addWidget(self.tag, 0, 0, 1, 2)
        grid.addWidget(QLabel('Text Height: '), 1,0,1,1)

        box = QSpinBox()
        box.setRange(1, 4)
        box.setValue(self.height)
        box.valueChanged.connect(self.textChangeSize)

        grid.addWidget(box, 1,1,1,1)
        grid.addWidget(QLabel('Text Font: '), 2,0,1,1)

        openList = QComboBox()
        openList.addItem('Arial')
        openList.addItem('Times New Roman')
        openList.addItem('Verdana')
        openList.addItem('Comic Sans MS')

        listTextIndex = openList.findText(self.text_type)
        openList.setCurrentIndex(listTextIndex)
        openList.activated.connect(self.FontChange)  

        grid.addWidget(openList, 2,1,1,1)

        self.setLayout(grid)
        self.setWindowTitle("Text Format")
        self.resize(500,150)
          
    def textChangeSize (self, height):
        self.height = height 
        self.tag.setText(self.text % (self.height, self.text_type))
                           
    def FontChange (self, var):
        self.text_type = self.types[var]
        self.tag.setText(self.text % (self.height,self.text_type))
                             
app = QApplication([])
window = guiApp3()  
window.show()
app.exec_()     
