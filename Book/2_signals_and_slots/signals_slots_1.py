
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
        
        
    def initUi(self):
        
        self.setGeometry(500, 250, 400, 300)
    
        self.button = QPushButton('Signal test', self)
        self.button.setGeometry(160, 110, 80, 30)
        self.button.clicked.connect(
                lambda: self.on_button_clicked(self.button))
        
        
    def on_button_clicked(self, sender):
        
        print(sender.width())
        print(sender.height())
        print('Button clicked')
            
            


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
