from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

class ActionButton(QWidget):
    def __init__(self, id, parent=None):
        QWidget.__init__(self, parent=parent)
        self.id = id
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(4)
        # add your buttons
        btnEdit = QPushButton('Edit',self)
        #btnEdit.setIcon(QIcon(QPixmap("edit.png")))
        btnEdit.setToolTip('Modifier la ligne')
        btnEdit.clicked.connect(self.edit)

        btnDelete = QPushButton('Delete', self)
        btnDelete.setToolTip('Supprimer la ligne')
        btnDelete.clicked.connect(self.delete)

        layout.addWidget(btnEdit)
        layout.addWidget(btnDelete)

    def edit(self):
        print("edit :", self.id)

    def delete(self):
        print("delete :", self.id)