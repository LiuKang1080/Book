
import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            
        self.check_windows = QCheckBox('Windows')
        self.check_windows.setObjectName('windows')
        
        self.check_linux = QCheckBox('Linux')
        self.check_linux.setObjectName('linux')
        
        self.check_mac = QCheckBox('Mac')
        self.check_mac.setObjectName('mac')
        
        self.label = QLabel()
        
        self.layout = QGridLayout()
                
        self.layout.addWidget(self.check_windows, 0, 0)
        self.layout.addWidget(self.check_linux, 1, 0)
        self.layout.addWidget(self.check_mac, 2, 0)                
        self.layout.addWidget(self.label, 0, 1, 3, 1)
        
        self.check_windows.stateChanged.connect(
                self.on_state_changed)
        self.check_linux.stateChanged.connect(
                self.on_state_changed)
        self.check_mac.clicked.connect(
                self.on_state_changed)                                
        
        self.setLayout(self.layout)
        
        
    def on_state_changed(self):
        
        self.label.setText('')
        label_text = ''
        
        if self.check_windows.isChecked():
            label_text += 'Windows\n'
        
        if self.check_linux.isChecked():
            label_text += 'Linux\n'
            
        if self.check_mac.isChecked():
            label_text += 'Mac'
        
        self.label.setText(label_text)


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
