
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            
        self.layout = QFormLayout()
            
        self.edit_1 = QLineEdit()
        self.edit_2 = QLineEdit()
        self.edit_3 = QLineEdit()
        self.edit_4 = QLineEdit()
        
        self.layout.addRow('Edit 1', self.edit_1)
        self.layout.addRow('Edit 2', self.edit_2)
        self.layout.addRow('Edit 3', self.edit_3)
        self.layout.addRow('Edit 4', self.edit_4)
        
        self.edit_1.textChanged.connect(
                lambda: self.on_text_changed(self.edit_1))
        self.edit_2.textChanged.connect(
                lambda: self.on_text_changed(self.edit_2))
        self.edit_3.textChanged.connect(
                lambda: self.on_text_changed(self.edit_3))
        self.edit_4.textChanged.connect(
                lambda: self.on_text_changed(self.edit_4))                                    
        
        self.setLayout(self.layout)
        
        
    def on_text_changed(self, sender):
        print(sender.text())


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
