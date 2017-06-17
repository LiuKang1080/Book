
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QPlainTextEdit, QGridLayout
from PyQt5.QtGui import QTextOption


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()

        plain_text_edit = QPlainTextEdit()
        plain_text_edit.setWordWrapMode(QTextOption.NoWrap)

        scroll_area = QScrollArea()
        scroll_area.setWidget(plain_text_edit)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(200)

        layout.addWidget(scroll_area, 0, 0)
        self.setLayout(layout)



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
