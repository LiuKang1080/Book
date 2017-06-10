
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QGridLayout

from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
        
        self.layout = QGridLayout()
        
        self.tree_widget = QTreeWidget()
        self.tree_widget.currentItemChanged.connect(
                self.on_current_item_changed)
        
        self.top_level_item = QTreeWidgetItem()
        self.top_level_item.setText(0, 'Apes')
        self.top_level_item.setData(
                0, Qt.UserRole, 'Hominoidea')

        self.item_gibbon = QTreeWidgetItem(
                self.top_level_item)
        self.item_gibbon.setText(0, 'Gibbons')
        self.item_gibbon.setData(
                0, Qt.UserRole, 'Hylobatidae')

        self.item_hominidae = QTreeWidgetItem(
                self.top_level_item)
        self.item_hominidae.setText(0, 'Hominidae')
        self.item_hominidae.setData(
                0, Qt.UserRole, 'Hominidae')

        self.item_ponginae = QTreeWidgetItem(
                self.item_hominidae)
        self.item_ponginae.setText(0, 'Orangutans')
        self.item_ponginae.setData(
                0, Qt.UserRole, 'Ponginae')

        self.item_homininae = QTreeWidgetItem(
                self.item_hominidae)
        self.item_homininae.setText(0, 'Homininae')
        self.item_homininae.setData(
                0, Qt.UserRole, 'Homininae')

        self.item_gorillinae = QTreeWidgetItem(
                self.item_homininae)
        self.item_gorillinae.setText(0, 'Gorillas')
        self.item_gorillinae.setData(
                0, Qt.UserRole, 'Gorillinae')

        self.item_hominini = QTreeWidgetItem(
                self.item_homininae)
        self.item_hominini.setText(0, 'Hominini')
        self.item_hominini.setData(
                0, Qt.UserRole, 'Hominini')

        self.item_panina = QTreeWidgetItem(
                self.item_hominini)
        self.item_panina.setText(0, 'Chimpanzees')
        self.item_panina.setData(
                0, Qt.UserRole, 'Panina')

        self.item_hominina = QTreeWidgetItem(
                self.item_hominini)
        self.item_hominina.setText(0, 'Hominina')
        self.item_hominina.setData(
                0, Qt.UserRole, 'Homo\n(including us)')
        
        self.tree_widget.addTopLevelItem(self.top_level_item)
        
        self.label = QLabel()
        self.label.setFixedWidth(100)
        
        self.layout.addWidget(self.tree_widget, 0, 0)
        self.layout.addWidget(self.label, 0, 1)
        
        self.setLayout(self.layout)
        
        
    def on_current_item_changed(self):
        
        current_item = self.tree_widget.currentItem()
        role = current_item.data(0, Qt.UserRole)

        self.label.setText(role)

        

def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
