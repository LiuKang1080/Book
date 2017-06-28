import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QColorDialog, QFileDialog, QFontDialog, QInputDialog, QLineEdit, QGridLayout

from PyQt5.QtGui import QFont


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()        
        self.show()
              
        
    def initUi(self):
            
        layout = QGridLayout()
        
        button_color = QPushButton('Show color dialog')
        button_file = QPushButton('Show file dialog')
        button_font = QPushButton('Show font dialog')
        button_input = QPushButton('Show input dialog')
        
        label_color = QLabel('Color label')
        label_file = QLabel('File label')
        label_font = QLabel('Font label')
        label_input = QLabel('Input label')
               
        layout.addWidget(button_color, 0, 0)
        layout.addWidget(button_file, 1, 0)
        layout.addWidget(button_font, 2, 0)
        layout.addWidget(button_input, 3, 0)
        
        layout.addWidget(label_color, 0, 1)
        layout.addWidget(label_file, 1, 1)
        layout.addWidget(label_font, 2, 1)
        layout.addWidget(label_input, 3, 1)
        
        button_color.clicked.connect(
            lambda: self.on_button_color_clicked(label_color))
            
        button_file.clicked.connect(
            lambda: self.on_button_file_clicked(label_file))
            
        button_font.clicked.connect(
            lambda: self.on_button_font_clicked(label_font))
            
        button_input.clicked.connect(
            lambda: self.on_button_input_clicked(label_input))                                            
        
        self.setLayout(layout)
        
        
    def on_button_color_clicked(self, label):
        
         color = QColorDialog.getColor()
         style_sheet = 'QLabel {background-color: ' + color.name() + '}'
         label.setStyleSheet(style_sheet)
        
        
    def on_button_file_clicked(self, label):
        
        file_name = QFileDialog.getOpenFileName()
        label.setText(file_name[0])
        
        
    def on_button_font_clicked(self, label):
        
        font = QFontDialog.getFont()
        label.setFont(font[0])
        
        
    def on_button_input_clicked(self, label):
        
        text = QInputDialog.getText(
                self, 'Enter text', 'Some text')
        label.setText(text[0])
        


def main(args):
       
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
