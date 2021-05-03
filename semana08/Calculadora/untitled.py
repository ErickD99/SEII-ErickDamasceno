# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(326, 298)
        MainWindow.setMinimumSize(QSize(326, 298))
        MainWindow.setMaximumSize(QSize(326, 298))
        icon = QIcon()
        icon.addFile(u":/newPrefix/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(203, 203, 203);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 80, 328, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.p8 = QPushButton(self.gridLayoutWidget)
        self.p8.setObjectName(u"p8")

        self.gridLayout_2.addWidget(self.p8, 1, 1, 1, 1)

        self.p3 = QPushButton(self.gridLayoutWidget)
        self.p3.setObjectName(u"p3")

        self.gridLayout_2.addWidget(self.p3, 3, 2, 1, 1)

        self.p0 = QPushButton(self.gridLayoutWidget)
        self.p0.setObjectName(u"p0")

        self.gridLayout_2.addWidget(self.p0, 4, 1, 1, 1)

        self.p2 = QPushButton(self.gridLayoutWidget)
        self.p2.setObjectName(u"p2")

        self.gridLayout_2.addWidget(self.p2, 3, 1, 1, 1)

        self.ponto = QPushButton(self.gridLayoutWidget)
        self.ponto.setObjectName(u"ponto")

        self.gridLayout_2.addWidget(self.ponto, 4, 0, 1, 1)

        self.soma = QPushButton(self.gridLayoutWidget)
        self.soma.setObjectName(u"soma")

        self.gridLayout_2.addWidget(self.soma, 4, 3, 1, 1)

        self.p7 = QPushButton(self.gridLayoutWidget)
        self.p7.setObjectName(u"p7")

        self.gridLayout_2.addWidget(self.p7, 1, 0, 1, 1)

        self.igual = QPushButton(self.gridLayoutWidget)
        self.igual.setObjectName(u"igual")

        self.gridLayout_2.addWidget(self.igual, 4, 2, 1, 1)

        self.p5 = QPushButton(self.gridLayoutWidget)
        self.p5.setObjectName(u"p5")

        self.gridLayout_2.addWidget(self.p5, 2, 1, 1, 1)

        self.p1 = QPushButton(self.gridLayoutWidget)
        self.p1.setObjectName(u"p1")

        self.gridLayout_2.addWidget(self.p1, 3, 0, 1, 1)

        self.sub = QPushButton(self.gridLayoutWidget)
        self.sub.setObjectName(u"sub")

        self.gridLayout_2.addWidget(self.sub, 3, 3, 1, 1)

        self.p4 = QPushButton(self.gridLayoutWidget)
        self.p4.setObjectName(u"p4")

        self.gridLayout_2.addWidget(self.p4, 2, 0, 1, 1)

        self.p9 = QPushButton(self.gridLayoutWidget)
        self.p9.setObjectName(u"p9")

        self.gridLayout_2.addWidget(self.p9, 1, 2, 1, 1)

        self.p6 = QPushButton(self.gridLayoutWidget)
        self.p6.setObjectName(u"p6")

        self.gridLayout_2.addWidget(self.p6, 2, 2, 1, 1)

        self.div = QPushButton(self.gridLayoutWidget)
        self.div.setObjectName(u"div")

        self.gridLayout_2.addWidget(self.div, 1, 3, 1, 1)

        self.mult = QPushButton(self.gridLayoutWidget)
        self.mult.setObjectName(u"mult")

        self.gridLayout_2.addWidget(self.mult, 2, 3, 1, 1)

        self.on = QPushButton(self.gridLayoutWidget)
        self.on.setObjectName(u"on")

        self.gridLayout_2.addWidget(self.on, 0, 0, 1, 2)

        self.off = QPushButton(self.gridLayoutWidget)
        self.off.setObjectName(u"off")

        self.gridLayout_2.addWidget(self.off, 0, 2, 1, 2)

        self.visor = QLCDNumber(self.frame)
        self.visor.setObjectName(u"visor")
        self.visor.setGeometry(QRect(3, 10, 321, 61))
        self.visor.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.p8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.p3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.p0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.p2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.ponto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.soma.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.p7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.p5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.p1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.p4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.p9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.p6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.on.setText(QCoreApplication.translate("MainWindow", u"CE/On", None))
        self.off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
    # retranslateUi

