
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()
        label = QLabel()        
        plain_text_edit = QPlainTextEdit()
        plain_text_edit.textChanged.connect(
                lambda: self.on_text_changed(
                        plain_text_edit, label))


        layout.addWidget(plain_text_edit, 0, 0)
        layout.addWidget(label, 1, 0)
        self.setLayout(layout)


    def on_text_changed(self, sender, label):

        size = sender.document().characterCount()
        label.setText(str(size))


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
