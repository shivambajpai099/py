import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class sinterest(QtGui.QWidget):
    def __init__(self):
        super(sinterest,self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(300,100)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)

        self.lab1 = QtGui.QLabel("Principal :")
        self.lab2 = QtGui.QLabel("Rate :")
        self.lab3 = QtGui.QLabel("Years :")
        self.lab4 = QtGui.QLabel("Amount :")
        self.lab5 = QtGui.QLabel("")
        self.principle = QtGui.QDoubleSpinBox()
        self.rate = QtGui.QDoubleSpinBox()
        self.years = QtGui.QSpinBox()
        
        self.principle.setRange(0.01,100000.00)
        self.principle.setValue(1.00)
        self.principle.setSingleStep(1.00)
        self.principle.setPrefix('$ ')

        self.rate.setRange(1.00,100)
        self.rate.setValue(1)
        self.rate.setSingleStep(0.25)
        self.rate.setSuffix(' %')

        self.years.setRange(1,30)
        self.years.setValue(2)
        self.years.setSuffix(' years')
        
        self.grid.addWidget(self.lab1,0,0)
        self.grid.addWidget(self.principle,0,1)
        self.grid.addWidget(self.lab2,1,0)
        self.grid.addWidget(self.rate,1,1)
        self.grid.addWidget(self.lab3,2,0)
        self.grid.addWidget(self.years,2,1)
        self.grid.addWidget(self.lab4,3,0)
        self.grid.addWidget(self.lab5,3,1)
        
        self.connect(self.principle, QtCore.SIGNAL("valueChanged(double)"), self.evaluate)
        self.connect(self.rate, QtCore.SIGNAL("valueChanged(double)"), self.evaluate)
        self.connect(self.years, QtCore.SIGNAL("valueChanged(int)"), self.evaluate)

        self.setWindowTitle('Simple Interest Calculator')
        
        self.show()
        
    def evaluate(self):
        prin = float(self.principle.value())
        rat = float(self.rate.value())
        year = float(self.years.value())
        amount = (prin * rat * year) / 100
        self.lab5.setText(str(amount))
        
        



app = QtGui.QApplication(sys.argv)
ex = sinterest()

sys.exit(app.exec_())
        
        

        
