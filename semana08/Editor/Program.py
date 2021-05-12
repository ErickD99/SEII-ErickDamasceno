# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from untitled import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def novo():
	global fileName
	fileName = ''
	window.textEdit.clear()

def abrir():
	global fileName
	fileName = QtWidgets.QFileDialog.getOpenFileName()[0]

	with open(fileName, 'r') as f:
		conteudo = f.read()

	window.textEdit.clear()
	window.textEdit.append(conteudo)

def salvar():
	if fileName != '':
		with open(fileName, 'w') as f:
			f.write(window.textEdit.toPlainText())
	else:
		salvar_como()

def salvar_como():
	global fileName
	fileName = QtWidgets.QFileDialog.getSaveFileName()[0]

	with open(fileName, 'w') as f:
		f.write(window.textEdit.toPlainText())

def sair():
	sys.exit(app.exec_())

def main():
	window.actionNovo.triggered.connect(novo)
	window.actionAbrir.triggered.connect(abrir)
	window.actionSalvar.triggered.connect(salvar)
	window.actionSalvarComo.triggered.connect(salvar_como)
	window.actionSair.triggered.connect(sair)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    main()
    fileName = ''
    sys.exit(app.exec_())