
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QListView, QGridLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        self.layout = QGridLayout()
        self.list_view = QListView()
        
        self.model = QStandardItemModel()
        self.populate_model()
        self.list_view.setModel(self.model)
        
        self.layout.addWidget(self.list_view, 0, 0)
        self.setLayout(self.layout)
        

    def populate_model(self):

        files = os.listdir('/')
        
        for f in files:
            item = QStandardItem(f)
            self.model.appendRow(item)



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
