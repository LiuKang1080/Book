
import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            
        self.button = QPushButton(
                'Start long running task')
        
        self.layout = QGridLayout()        
        self.layout.addWidget(self.button, 0, 0)

        
        self.button.clicked.connect(
                self.on_button_clicked)
        
        self.setLayout(self.layout)
        
        
    def on_button_clicked(self):
        
        for _ in range(20):
            print('running . . .')
            sleep(2)


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
