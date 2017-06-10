
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            
        self.button_blue = QRadioButton('Change background to color blue')
        self.button_blue.setObjectName('blue')
        self.button_green = QRadioButton('Change background to color green')
        self.button_green.setObjectName('green')
        self.button_red = QRadioButton('Change background to color blue')
        self.button_red.setObjectName('red')
        
        self.label = QLabel('Colored label')
        
        self.layout = QGridLayout()
                
        self.layout.addWidget(self.button_blue, 0, 0)
        self.layout.addWidget(self.button_green, 1, 0)
        self.layout.addWidget(self.button_red, 2, 0)                
        self.layout.addWidget(self.label, 0, 1, 3, 1)
        
        self.button_blue.clicked.connect(
                lambda: self.on_button_clicked(self.button_blue))
        self.button_green.clicked.connect(
                lambda: self.on_button_clicked(self.button_green))
        self.button_red.clicked.connect(
                lambda: self.on_button_clicked(self.button_red))                                
        
        self.setLayout(self.layout)
        
        
    def on_button_clicked(self, sender):
        
        if sender.objectName() == 'blue':
            self.label.setStyleSheet(
                    'background-color:blue;')
        elif sender.objectName() == 'green':
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
