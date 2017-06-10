
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            
        self.button_1 = QPushButton('Button 1')
        self.button_2 = QPushButton('Button 2')
        self.button_3 = QPushButton('Button 3')
        self.button_4 = QPushButton('Button 4')
        self.button_5 = QPushButton('Button 5')
        
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.button_1)
        self.layout.addWidget(self.button_2)
        self.layout.addWidget(self.button_3)
        self.layout.addWidget(self.button_4)
        self.layout.addWidget(self.button_5)
        
        self.button_1.clicked.connect(
                lambda: self.on_button_clicked(self.button_1))
        self.button_2.clicked.connect(
                lambda: self.on_button_clicked(self.button_2))
        self.button_3.clicked.connect(
                lambda: self.on_button_clicked(self.button_3))
        self.button_4.clicked.connect(
                lambda: self.on_button_clicked(self.button_4))
        self.button_5.clicked.connect(
                lambda: self.on_button_clicked(self.button_5))
        
        self.setLayout(self.layout)
        
        
    def on_button_clicked(self, sender):
        
        print(sender.text())


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
