
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.low = 0
        self.high = 100
        
        self.show()
       
        
    def initUi(self):
            
        self.button = QPushButton('Generate random integer')
        self.label = QLabel()
        
        self.layout = QGridLayout()        
        self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.label, 1, 0)
        
        self.button.clicked.connect(self.on_button_clicked)
        
        self.setLayout(self.layout)
        
        
    def on_button_clicked(self):
        
        value = str(randint(self.low, self.high))
        self.label.setText(value)


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
