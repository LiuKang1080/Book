
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QGridLayout

from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            

        
        self.layout = QGridLayout()
        
        self.list_widget = QListWidget()
        self.list_widget.currentItemChanged.connect(
                self.on_current_item_changed)
        
        self.item_blue = QListWidgetItem()
        self.item_blue.setData(Qt.DisplayRole, 'blue')
        
        self.item_green = QListWidgetItem()
        self.item_green.setData(Qt.DisplayRole, 'green')
        
        self.item_red = QListWidgetItem()
        self.item_red.setData(Qt.DisplayRole, 'red')
        
        self.list_widget.addItem(self.item_blue)
        self.list_widget.addItem(self.item_green)
        self.list_widget.addItem(self.item_red)
        
        self.label = QLabel()
        self.label.setFixedWidth(100)
        
        self.layout.addWidget(self.list_widget, 0, 0)
        self.layout.addWidget(self.label, 0, 1)
        
        self.setLayout(self.layout)
        
        
    def on_current_item_changed(self):
        
        current_item = self.list_widget.currentItem()
        color = current_item.data(Qt.DisplayRole)
        
        if color == 'blue':
            self.label.setStyleSheet(
                    'background-color:blue;')
        elif color == 'green':
            self.label.setStyleSheet(
                    'background-color:green;')
        else:
            self.label.setStyleSheet(
                    'background-color:red;')
        

def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
