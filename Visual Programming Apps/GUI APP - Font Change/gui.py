from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class FontType(QDialog):
    
    def __init__(self, parent = None):
        super(FontType, self).__init__(parent)
        
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Font:"), 0,0,1,1)
        self.fontList = QComboBox()
        self.fontList.addItems(('Arial', 'Times New Roman', 'Verdana', 'Comic San MS'))
        self.fontList.setCurrentIndex(0) #default open with Arial
        grid.addWidget(self.fontList, 0,1,1,1)
        
        acceptButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        
        buttonBox = QHBoxLayout()
        buttonBox.addWidget(acceptButton)
        buttonBox.addWidget(cancelButton)
        
        grid.addLayout(buttonBox, 1,0,1,2)
        
        acceptButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)
        
        self.setLayout(grid)
        self.resize(300, 100)
        self.setWindowTitle("Font Settings")
        self.setWindowIcon(QIcon("icons8-font-size-50"))
        
class MainApp(QDialog):
    
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        
        self.fontType = 'Arial'
        self.text = '<font color = "black" size = "+3" face = "%s"> Hello World!</font>'
        self.tag = QLabel(self.text % self.fontType)

        box = QVBoxLayout()
        box.addWidget(self.tag)
        
        fontBox = QPushButton("Change Font")
        fontBox.clicked.connect(self.changeFont)
        box.addWidget(fontBox)
        self.setLayout(box)

        self.setWindowTitle("Main App")
        self.setWindowIcon(QIcon("icons8-spyder-ide-5-48"))

    def changeFont(self):
        
        dialog = FontType()
        
        if dialog.exec_():
            self.fontType = dialog.fontList.currentText()
            self.tag.setText(self.text % self.fontType)
            
app = QApplication([])
window = MainApp()
window.show()
app.exec_()
