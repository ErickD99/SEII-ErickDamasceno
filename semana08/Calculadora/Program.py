# -*- coding: utf-8 -*- --noconsole

import sys
import re
from PySide2 import QtCore, QtGui, QtWidgets
from untitled import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        lista = []

        class status: status = True

        def cap(arg):
        	if arg == 'Off':
        		self.visor.display('')
        		lista.clear()

        	elif arg == 'CE/On':
        		self.visor.display('0')
        		lista.clear()

        	elif arg in '0123456789.':
        		valor = str(self.visor.intValue())
        		if len(lista) and lista[-1] == '.':
        			valor += '.'
        		if str(self.visor.intValue()) != '0' and status.status == True:
        			self.visor.display(valor + arg)
        		else:
        			self.visor.display(str(arg))
        		lista.append(arg)
        		status.status = True

        	elif arg in '+-*/':
        		self.visor.display('')
        		lista.append(arg)

        	elif arg == '=':
        		junta = ''
        		if len(lista) > 0:
        			while lista[-1] in '+-.*/':
        				lista.remove(lista[-1])
        			for item in lista:
        				junta = junta + f'{item}'
        			resultado = eval(junta)
	        		#print(eval(junta))
	        		self.visor.display(resultado)

	        	
	        	lista.clear()
	        	lista.append(resultado)
	        	junta = ''
	       		#print(lista)

        

        self.p0.clicked.connect(lambda: cap(self.p0.text()))
        self.p1.clicked.connect(lambda: cap(self.p1.text()))
        self.p2.clicked.connect(lambda: cap(self.p2.text()))
        self.p3.clicked.connect(lambda: cap(self.p3.text()))
        self.p4.clicked.connect(lambda: cap(self.p4.text()))
        self.p5.clicked.connect(lambda: cap(self.p5.text()))
        self.p6.clicked.connect(lambda: cap(self.p6.text()))
        self.p7.clicked.connect(lambda: cap(self.p7.text()))
        self.p8.clicked.connect(lambda: cap(self.p8.text()))
        self.p9.clicked.connect(lambda: cap(self.p9.text()))
        self.soma.clicked.connect(lambda: cap(self.soma.text()))
        self.sub.clicked.connect(lambda: cap(self.sub.text()))
        self.mult.clicked.connect(lambda: cap(self.mult.text()))
        self.div.clicked.connect(lambda: cap(self.div.text()))
        self.on.clicked.connect(lambda: cap(self.on.text()))
        self.off.clicked.connect(lambda: cap(self.off.text()))
        self.igual.clicked.connect(lambda: cap(self.igual.text()))
        self.ponto.clicked.connect(lambda: cap(self.ponto.text()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())