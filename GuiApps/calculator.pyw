import sys
import math
import ast
from PyQt4 import QtGui


#GUI CODE
but = []
class Test(QtGui.QWidget):

    def __init__(self):
        super(Test, self).__init__()

        self.initUI()
    
    def initUI(self):
        self.setFixedSize(500,300)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        self.strng = ''
        name = ['CLR','','','+-','SQRT','7','8','9','/','%','4','5','6','*','1\X','1','2','3','-','X2','0','.','e','+','=']
        self.exp = QtGui.QLabel(self.strng)
        self.exp.setStyleSheet('QLabel {background-color: grey; color:black;font-size:25px;padding:5px 0px 5px 0px;overflow:scroll;}')
        self.exp.setWordWrap(True)
        self.exp.resize(200,200)
        self.grid.addWidget(self.exp,0,0,2,0)
        
        position = [ (i,j) for i in range(2,7) for j in range(5)]

        
        
        for i,position, name in zip(range(25),position, name):
            
            button = QtGui.QPushButton(name)
            self.grid.addWidget(button, *position)
            but.append(button)
            
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        
        self.show()
        num = [5,6,7,8,9,10,11,12,13,15,16,17,18,20,21,23]
        for i in num:
            but[i].clicked.connect(self.btn)   
            but[i].setShortcut(but[i].text())
        but[0].clicked.connect(self.clear)
        but[0].setShortcut('esc')
        
        but[3].clicked.connect(self.neg)
        
        but[4].clicked.connect(self.sqroot)
        but[14].clicked.connect(self.onebyx)
        but[19].clicked.connect(self.square)
        but[24].clicked.connect(self.evaluate)
        but[24].setShortcut('return')
        

    def btn(self):
        strn = self.sender().text()
        self.strng = self.strng + strn
        self.exp.setText(self.strng)

    def neg(self):
        self.strng = '-' + self.strng
        self.exp.setText(self.strng)

    def sqroot(self):
        if int(eval(str(self.strng)))>0:
            self.strng = str(math.sqrt(eval(str(self.strng))))
            self.exp.setText(self.strng)
        else:
            self.exp.setText('Input Error')
            self.strng = ''
            
    def onebyx(self):
        if int(eval(str(self.strng)))!= 0:
            num = ((eval(str(self.strng))))
            num = 1/float(num)
            self.strng = str(num)
            self.exp.setText(self.strng)
        else:
            self.exp.setText('Input Error')
            self.strng = ''
            

    def square(self):
        self.strng = str(math.pow(eval(str(self.strng)),2))
        self.exp.setText(self.strng)
        
    def clear(self):
        self.strng = ''
        self.exp.setText(self.strng)
        
    def evaluate(self):
        try :
            self.strng = str(eval(str(self.strng)))
            self.exp.setText(self.strng)
        except :
            self.exp.setText("'%s' expression is Invalid" % self.strng)
            self.strng = ''      

           
            
app = QtGui.QApplication(sys.argv)
ex = Test()

sys.exit(app.exec_())

