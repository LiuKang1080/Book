
import sys
import os
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QGridLayout
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()
        
        table_view = QTableView()
        
        model = QTableModel()
        table_view.setModel(model)

        layout.addWidget(table_view, 0, 0)
        self.setLayout(layout)
        


class QTableModel(QAbstractTableModel):


    def __init__(self):
        
        super(QTableModel, self).__init__()

        self.row_count = 5
        self.column_count = 5

        self.table = [[randint(0, 100) for _ in range(5)] for _ in range(5)]


    def rowCount(self, parent=QModelIndex()):
        return self.row_count


    def columnCount(self, parent=QModelIndex()):
        return self.column_count


    def data(self, index, role=Qt.DisplayRole):

        if role == Qt.DisplayRole:

            i = index.row()
            j = index.column()

            return self.table[i][j]
            

        



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
