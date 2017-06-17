
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QLabel, QVBoxLayout, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()

        label_1 = QLabel()
        label_2 = QLabel()

        layout.addWidget(label_1, 0, 1)
        layout.addWidget(label_2, 1, 1)          
        
        groupbox_1 = QGroupBox()
        groupbox_1.setTitle('First group box')

        vertical_layout_1 = QVBoxLayout()

        radiobutton_1 = QRadioButton('First option')
        radiobutton_2 = QRadioButton('Second option')

        radiobutton_1.toggled.connect(
                lambda: self.on_radiobutton_checked(
                        radiobutton_1, label_1))

        radiobutton_2.toggled.connect(
                lambda: self.on_radiobutton_checked(
                        radiobutton_2, label_1))                        
        
        vertical_layout_1.addWidget(radiobutton_1)
        vertical_layout_1.addWidget(radiobutton_2)

        groupbox_1.setLayout(vertical_layout_1)
        
        vertical_layout_2 = QVBoxLayout()

        groupbox_2 = QGroupBox()
        groupbox_2.setTitle('Second group box.')

        radiobutton_3 = QRadioButton('Third option')
        radiobutton_4 = QRadioButton('Fourth option')

        radiobutton_3.toggled.connect(
                lambda: self.on_radiobutton_checked(
                        radiobutton_3, label_2))

        radiobutton_4.toggled.connect(
                lambda: self.on_radiobutton_checked(
                        radiobutton_4, label_2))                         
        
        vertical_layout_2.addWidget(radiobutton_3)
        vertical_layout_2.addWidget(radiobutton_4)

        groupbox_2.setLayout(vertical_layout_2)

        layout.addWidget(groupbox_1, 0, 0)
        layout.addWidget(groupbox_2, 1, 0)
        
        self.setLayout(layout)


    def on_radiobutton_checked(self, sender, label):
        label.setText(sender.text())


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
