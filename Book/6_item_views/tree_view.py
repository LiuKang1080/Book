
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QGridLayout, QFileSystemModel
from PyQt5.QtCore import QDir


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()
        tree_view = QTreeView()
        
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        tree_view.setModel(model)
        
        layout.addWidget(tree_view, 0, 0)
        self.setLayout(layout)
        



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
