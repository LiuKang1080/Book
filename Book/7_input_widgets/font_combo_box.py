
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QFontComboBox, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()        
        label = QLabel()
        combo_box = QFontComboBox()

        combo_box.currentFontChanged.connect(
                lambda: self.on_current_font_changed(
                        combo_box, label))
                
        layout.addWidget(combo_box, 0, 0)
        layout.addWidget(label, 1, 0)
        self.setLayout(layout)


    def on_current_font_changed(self, sender, label):

        font = sender.currentFont()
        font_name = font.toString()
        label.setFont(font)
        label.setText(font_name)
        


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
