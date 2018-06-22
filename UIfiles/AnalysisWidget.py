# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalysisWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 676)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.advancedPlotWidget = QChartView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedPlotWidget.sizePolicy().hasHeightForWidth())
        self.advancedPlotWidget.setSizePolicy(sizePolicy)
        self.advancedPlotWidget.setMinimumSize(QtCore.QSize(500, 400))
        self.advancedPlotWidget.setObjectName("advancedPlotWidget")
        self.gridLayout_2.addWidget(self.advancedPlotWidget, 0, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.shortCircuitCurrentBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.shortCircuitCurrentBox.setObjectName("shortCircuitCurrentBox")
        self.gridLayout.addWidget(self.shortCircuitCurrentBox, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.nonIdealityBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.nonIdealityBox.setObjectName("nonIdealityBox")
        self.gridLayout.addWidget(self.nonIdealityBox, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.openCircuitVoltageBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.openCircuitVoltageBox.setObjectName("openCircuitVoltageBox")
        self.gridLayout.addWidget(self.openCircuitVoltageBox, 1, 1, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.rShuntBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rShuntBox.setObjectName("rShuntBox")
        self.gridLayout.addWidget(self.rShuntBox, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.maxPowerPointBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.maxPowerPointBox.setObjectName("maxPowerPointBox")
        self.gridLayout.addWidget(self.maxPowerPointBox, 3, 1, 1, 1)
        self.rSeriesBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rSeriesBox.setObjectName("rSeriesBox")
        self.gridLayout.addWidget(self.rSeriesBox, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.fillFactorBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.fillFactorBox.setObjectName("fillFactorBox")
        self.gridLayout.addWidget(self.fillFactorBox, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.efficiencyBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.efficiencyBox.setObjectName("efficiencyBox")
        self.gridLayout.addWidget(self.efficiencyBox, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 3)
        self.savePNGButton = QtWidgets.QPushButton(Dialog)
        self.savePNGButton.setObjectName("savePNGButton")
        self.gridLayout_2.addWidget(self.savePNGButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Main Parameters of This Solar Cell"))
        self.label.setText(_translate("Dialog", "jsc [mA/cm]"))
        self.label_6.setText(_translate("Dialog", "Diode non-ideality factor"))
        self.label_2.setText(_translate("Dialog", "Uoc [V]"))
        self.label_7.setText(_translate("Dialog", "Rshunt [Ω]"))
        self.label_8.setText(_translate("Dialog", "Rseries [Ω]"))
        self.label_3.setText(_translate("Dialog", "Max. Power Point"))
        self.label_4.setText(_translate("Dialog", "Fill Factor [%]"))
        self.label_5.setText(_translate("Dialog", "Efficiency [%]"))
        self.savePNGButton.setText(_translate("Dialog", "Save as PNG"))
        self.closeButton.setText(_translate("Dialog", "Close"))

from PyQt5.QtChart import QChartView
