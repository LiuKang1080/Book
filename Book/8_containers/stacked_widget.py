
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QLabel, QShortcut, QGridLayout
from PyQt5.QtGui import QKeySequence

class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()

        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(QLabel('Linux'))
        stacked_widget.addWidget(QLabel('Windows'))
        stacked_widget.addWidget(QLabel('Mac'))
        stacked_widget.addWidget(QLabel('Android'))

        layout.addWidget(stacked_widget, 0, 0)
           
        self.setLayout(layout)

        left_shortcut = QShortcut(self)
        left_shortcut.setKey('Ctrl+L')
        right_shortcut = QShortcut(self)
        right_shortcut.setKey('Ctrl+R')

        left_shortcut.activated.connect(
                lambda: self.on_shortcut_activated(
                        left_shortcut, stacked_widget))

        right_shortcut.activated.connect(
                lambda: self.on_shortcut_activated(
                        right_shortcut, stacked_widget))                        


    def on_shortcut_activated(self, shortcut, target):

        index = target.currentIndex()
        
        if shortcut.key() == 'Ctrl+R':
            if index < target.count():
                target.setCurrentIndex(index + 1)
        elif shortcut.key() == 'Ctrl+L':
            if index > 0:
                target.setCurrentIndex(index - 1)


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
