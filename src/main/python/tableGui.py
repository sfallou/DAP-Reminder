from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen

import actionButtons as actBtn
from Functions import *

class TableGUI(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent=parent)
        self.setObjectName("tableWidget")
        self.setColumnCount(10)
        self.setHorizontalHeaderLabels(['PN', 'CMM','REV CMM', 'DAP', 'REV DAP', 'DATE CREATION', 'DEADLINE','ECHEANCE','COMMENTS', ''])
        self.verticalHeader().hide()
        style = "::section {""background-color: lightblue; }"
        self.horizontalHeader().setStyleSheet(style)
        #self.tableWidget.setShowGrid(False) 
        self.content_table()

    def content_table(self):
        datas = show_dap()
        i = -1
        for row in datas:
            i += 1
            self.insertRow(i)
            self.setItem(i , 0, QtWidgets.QTableWidgetItem(row[1]))
            self.setItem(i , 1, QtWidgets.QTableWidgetItem(row[2]))
            self.setItem(i , 2, QtWidgets.QTableWidgetItem(row[3]))
            self.setItem(i , 3, QtWidgets.QTableWidgetItem(row[4]))
            self.setItem(i , 4, QtWidgets.QTableWidgetItem(row[5]))
            self.setItem(i , 5, QtWidgets.QTableWidgetItem(row[6]))
            self.setItem(i , 6, QtWidgets.QTableWidgetItem(row[7]))
            echeance, color = deadline(row[7])
            echeance = str(echeance)
            self.setItem(i , 7, QtWidgets.QTableWidgetItem(echeance))
            self.item(i, 7).setBackground(QColor(color[0],color[1],color[2]))
            self.setItem(i , 8, QtWidgets.QTableWidgetItem(row[8]))
            self.setCellWidget(i,9, actBtn.ActionButton(i))
           
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = TableGUI()
    win.show()
    sys.exit(app.exec_())

