from UIfiles.BSA_MainGui import Ui_MainWindow
#from batchSolarCellAnalyzer import MainWindow
from PyQt5 import QtWidgets, QtGui

class ModButton(QtWidgets.QPushButton):
    def __init__(self):
        super(ModButton, self).__init__()
        self.clicked.connect(self.AnalyzeFunction)
        pass

    def AnalyzeFunction(self):
        print("Analyze FN")
        pass





def SetupUI(selfui):
    #Title
    selfui.setWindowTitle("Simple Solar Cell Analyzer")
    selfui.ui.tableWithFiles.setHorizontalHeaderLabels(["PLOT?", "ANALYZE?", "File name", "Area", "jsc", "Uoc", "FF", "Eff", "Compare?", "Full Path"])
    pass

def FillFiles(ui:Ui_MainWindow, file_url:None):
    if file_url is not None:
        print("File url is not None")
        rCount = ui.tableWithFiles.rowCount()
        if rCount is not None:
            print("Count is not None")
            ui.tableWithFiles.setRowCount(rCount+1)
            ui.tableWithFiles.setCellWidget(rCount+1, 1, QtWidgets.QPushButton())
            cell = QtWidgets.QTableWidgetItem()
            cell.setText(str(file_url.path()))
            ui.tableWithFiles.setItem(rCount+1, 10, cell)
            ui.tableWithFiles.selectRow(rCount+1)
            ui.tableWithFiles.update()
            pass
        else:
            print("Count is None")
            ui.tableWithFiles.setRowCount(1)
            # Fill all additional info:
            ui.tableWithFiles.setCellWidget( 1, 1, QtWidgets.QPushButton())
            cell = QtWidgets.QTableWidgetItem()
            cell.setText(str(file_url.path()))
            ui.tableWithFiles.setItem( 1, 10, cell)
            ui.tableWithFiles.selectRow(1)
            ui.tableWithFiles.update()
            pass
        # Continue
        pass
    else:
        pass
    pass