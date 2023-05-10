from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class fuelCalculator (QDialog):

    def __init__(self, parent = None):
        super(fuelCalculator, self).__init__(parent)

        # make a grid
        grid = QGridLayout()
        # add widgets
        grid.addWidget(QLabel('The Way You Will Go (KM):'), 0,0,1,1)
        self.wayTaken = QLineEdit() # QlineEdit make a text box
        self.wayTaken.setInputMask('0000000000') # text input format
        grid.addWidget(self.wayTaken, 0,1,1,1)
        
        grid.addWidget(QLabel('Liter Price of Fuel:'), 1,0,1,1)
        self.fuelPrice = QLineEdit() # QlineEdit make a text box can editable
        self.fuelPrice.setInputMask('00.00') # text input format
        grid.addWidget(self.fuelPrice, 1,1,1,1)
        
        grid.addWidget(QLabel("Fuel Consumed per 100 km:"), 2,0,1,1)
        self.fuelConsumption = QLineEdit() # QlineEdit make a text box can editable
        self.fuelConsumption.setInputMask('0.0') # text input format
        grid.addWidget(self.fuelConsumption, 2,1,1,1)
        
        grid.addWidget(QLabel("Total Amount ($):"), 3,0,1,1)
        self.amount = (QLabel('<i> Enter KM </i>')) 
        grid.addWidget(self.amount, 3,1,1,1)
        
        self.button = QPushButton("Calcualte")
        self.button.clicked.connect(self.calculator)
        grid.addWidget(self.button, 4,0,1,2)
        
        self.setLayout(grid)
        self.setWindowTitle('Fuel Calculator')

    def calculator(self):

        way = 0
        try: way = int(self.wayTaken.text())
        except: pass
    
        price = 0
        try: price = float(self.fuelPrice.text())
        except: pass
    
        consumption = 0
        try: consumption = float(self.fuelConsumption.text())
        except: pass
    
        if not way :
            self.amount.setText('<font color ="red"><i> Enter KM </i></font>')
            self.wayTaken.setFocus()    
        elif not price:
            self.amount.setText('<font color ="red"><i> Enter The Price </i></font>')
            self.fuelPrice.setFocus()
        elif not consumption:
            self.amount.setText('<font color ="red"><i> Enter the Consumption </i></font>')
            self.fuelConsumption.setFocus()   
        else: 
            amount = price*((way * consumption) / 100)
            self.amount.setText('<font color = "black"><b> %0.2f </b></font>' % amount)
               
app = QApplication([]) 
window = fuelCalculator()   
window.show()
app.exec_()
