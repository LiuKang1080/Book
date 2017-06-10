
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            

        
        self.layout = QGridLayout()
        
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(3)
        self.table_widget.setColumnWidth(0, 80)
        self.table_widget.setColumnWidth(1, 80)
        self.table_widget.setColumnWidth(2, 80)

        self.table_widget.setItem(0, 0,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(0, 1,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(0, 2,
                QTableWidgetItem(str(randint(1, 100))))                
        
        self.table_widget.currentItemChanged.connect(
                self.on_current_item_changed)

        self.table_widget.setItem(1, 0,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(1, 1,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(1, 2,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(2, 0,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(2, 1,
                QTableWidgetItem(str(randint(1, 100))))

        self.table_widget.setItem(2, 2,
                QTableWidgetItem(str(randint(1, 100))))                

        
        self.label = QLabel()
        self.label.setFixedWidth(100)
        
        self.layout.addWidget(self.table_widget, 0, 0)
        self.layout.addWidget(self.label, 0, 1)
        
        self.setLayout(self.layout)
        
        
    def on_current_item_changed(self):
        
        current_item = self.table_widget.currentItem()
        self.label.setText(current_item.text())

        

def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
