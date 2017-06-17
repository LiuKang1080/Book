
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()
        
        label = QLabel()

        combo_box = QComboBox()
        combo_box.addItem('Linux')
        combo_box.addItem('Windows')
        combo_box.addItem('Mac')
        combo_box.addItem('Android')

        combo_box.currentTextChanged.connect(
                lambda: self.on_current_text_changed(
                        combo_box, label))
                
        layout.addWidget(combo_box, 0, 0)
        layout.addWidget(label, 1, 0)
        self.setLayout(layout)


    def on_current_text_changed(self, sender, label):

        text = sender.currentText()
        label.setText(text)
        


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
