
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QToolBox, QPushButton, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()

        tool_box = QToolBox()
        
        linux_button = QPushButton('Linux')
        tool_box.addItem(linux_button, 'Linux')

        windows_button = QPushButton('Windows')
        tool_box.addItem(windows_button, 'Windows')

        mac_button = QPushButton('Mac')
        tool_box.addItem(mac_button, 'Mac')

        android_button = QPushButton('Android')
        tool_box.addItem(android_button, 'Android')        

        layout.addWidget(tool_box, 0, 0)
           
        self.setLayout(layout)



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
