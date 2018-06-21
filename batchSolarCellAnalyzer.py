#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from UIfiles.BSA_MainGui import Ui_MainWindow
from UIfiles.SetupUI import SetupUI
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        SetupUI(self)
        # SLOTS:
        self.ui.closeAppButton.clicked.connect(self.closeFunction)
        self.ui.actionClose.triggered.connect(self.closeFunction)
        self.ui.addFilesButton.clicked.connect(self.addFilesFunction)
        self.ui.clearTableButton.clicked.connect(self.clearTableFunction)

    def ConsoleOutput(self, text=None):
        if text is not None:
            self.ui.consoleOutput.appendPlainText(str(text))
        else:
            pass

    def clearTableFunction(self):
        self.ConsoleOutput("Table will be cleared")
        pass


    def closeFunction(self):
        print("Exiting ... ")
        sys.exit(10)
        pass

    def addFilesFunction(self):
        self.ConsoleOutput("FILES WILL BE ADDED")
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
