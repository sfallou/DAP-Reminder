from fbs_runtime.application_context.PyQt5 import ApplicationContext 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen

import actionButtons as actBtn
from Functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.setGeometry(300, 100, 1030, 400)
        self.setMinimumSize(630, 400)
        self.menu()
        self.init_table()
        self.mainWindow()
        self.show_dap()
    
    def menu(self):
        ### horizontal box with the buttons
        self.groupBox = QtWidgets.QHBoxLayout()
        
        self.createButton = QtWidgets.QPushButton()
        #self.createButton.setFixedWidth(90)
        self.createButton.setObjectName("createButton")
        self.createButton.setText("Créer une DAP")

        self.exportButton = QtWidgets.QPushButton()
        #self.exportButton.setFixedWidth(90)
        self.exportButton.setObjectName("exportButton")
        self.exportButton.setText("Exporter")

        self.importButton = QtWidgets.QPushButton()
        #self.importButton.setFixedWidth(90)
        self.importButton.setObjectName("importButton")
        self.importButton.setText("Importer")
  
        self.aboutButton = QtWidgets.QPushButton()
        #self.aboutButton.setFixedWidth(90)
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.setText("A propos")
        
        self.groupBox.addWidget(self.createButton, 0, QtCore.Qt.AlignLeft)
        self.groupBox.addWidget(self.exportButton, 1, QtCore.Qt.AlignLeft)
        self.groupBox.addWidget(self.importButton, 2, QtCore.Qt.AlignLeft)
        self.groupBox.addWidget(self.aboutButton, 3, QtCore.Qt.AlignRight)
    
    def init_table(self):
        ##########################################
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['PN', 'CMM','REV CMM', 'DAP', 'REV DAP', 'DATE CREATION', 'DEADLINE','ECHEANCE','COMMENTS', ''])
        self.tableWidget.verticalHeader().hide()
        style = "::section {""background-color: lightblue; }"
        self.tableWidget.horizontalHeader().setStyleSheet(style)
        #self.tableWidget.setShowGrid(False) 

    def show_dap(self):
    	datas = show_dap()
    	i = -1
    	for row in datas:
    		i += 1
    		self.tableWidget.insertRow(i)
    		self.tableWidget.setItem(i , 0, QtWidgets.QTableWidgetItem(row[1]))
    		self.tableWidget.setItem(i , 1, QtWidgets.QTableWidgetItem(row[2]))
    		self.tableWidget.setItem(i , 2, QtWidgets.QTableWidgetItem(row[3]))
    		self.tableWidget.setItem(i , 3, QtWidgets.QTableWidgetItem(row[4]))
    		self.tableWidget.setItem(i , 4, QtWidgets.QTableWidgetItem(row[5]))
    		self.tableWidget.setItem(i , 5, QtWidgets.QTableWidgetItem(row[6]))
    		self.tableWidget.setItem(i , 6, QtWidgets.QTableWidgetItem(row[7]))
    		echeance, color = deadline(row[7])
    		echeance = str(echeance)
    		self.tableWidget.setItem(i , 7, QtWidgets.QTableWidgetItem(echeance))
    		self.tableWidget.item(i, 7).setBackground(QColor(color[0],color[1],color[2]))
    		self.tableWidget.setItem(i , 8, QtWidgets.QTableWidgetItem(row[8]))
    		self.tableWidget.setCellWidget(i,9, actBtn.ActionButton(i))

			

    def mainWindow(self):
        #### Main Window Layout
        self.vertWidget = QtWidgets.QVBoxLayout()
        self.vertWidget.setSpacing(10)
 
        self.vertWidget.addLayout(self.groupBox)
        #self.vertWidget.addLayout(self.lblgroup)
        #self.vertWidget.addLayout(self.combogroup)
 
        self.vertWidget.setStretch(0, 1)
        self.vertWidget.setStretch(1, 0)
 
        self.vertWidget.addWidget(self.tableWidget)
 
        self.mainWidget = QtWidgets.QWidget()
 
        self.mainWidget.setLayout(self.vertWidget)
 
        self.setCentralWidget(self.mainWidget)
  
        QtCore.QMetaObject.connectSlotsByName(self)
  
        self.setWindowTitle("Utilitaire de rappel pour DAP")
        self.statusBar().showMessage("Version 1.0")
        
   
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

