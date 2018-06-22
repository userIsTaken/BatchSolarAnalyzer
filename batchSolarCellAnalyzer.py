#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from UIfiles.BSA_MainGui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Simple Solar Cell Analyzer")
        self.ui.tableWithFiles.setHorizontalHeaderLabels(["PLOT?", "ANALYZE?", "File name", "Area", "jsc", "Uoc", "FF", "Eff", "Compare?", "Full Path"])
        # SLOTS:
        self.ui.closeAppButton.clicked.connect(self.closeFunction)
        self.ui.actionClose.triggered.connect(self.closeFunction)
        self.ui.clearTableButton.clicked.connect(self.clearTableFunction)
        #LOAD files:
        self.ui.addFilesButton.clicked.connect(self.loadFilesFunction)

    def FillFiles(self, file_url=None):
        if file_url is not None:
            print("File url is not None")
            rCount = self.ui.tableWithFiles.rowCount()
            if rCount is not None:
                print("Count is not None")
                self.ui.tableWithFiles.setRowCount(rCount + 1)
                self.ui.tableWithFiles.setCellWidget(rCount + 1, 1, QtWidgets.QPushButton())
                cell = QtWidgets.QTableWidgetItem()
                cell.setText(str(file_url.path()))
                self.ui.tableWithFiles.setItem(rCount + 1, 10, cell)
                self.ui.tableWithFiles.selectRow(rCount + 1)
                self.ui.tableWithFiles.update()
                pass
            else:
                print("Count is None")
                self.ui.tableWithFiles.setRowCount(1)
                # Fill all additional info:
                self.ui.tableWithFiles.setCellWidget(1, 1, QtWidgets.QPushButton())
                cell = QtWidgets.QTableWidgetItem()
                cell.setText(str(file_url.path()))
                self.ui.tableWithFiles.setItem(1, 10, cell)
                self.ui.tableWithFiles.selectRow(1)
                self.ui.tableWithFiles.update()
                pass
            # Continue
            pass
        else:
            pass
        pass

    def loadFilesFunction(self):
        self.ConsoleOutput("File(s) will be add")
        filter = "TXT (*.txt);;CSV (*.csv);;DAT (*.dat);; ANY file (*.*)"
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        names = file_name.getOpenFileUrls(self, "Open files", "/home/", filter)
        for i in names[0]:
            self.ConsoleOutput(str(i.path()))
        # MAIN LOADER:
        for i in names[0]:
            file_path = i
            self.FillFiles( file_path)
        pass

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
