
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDial, QLabel, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()
        label = QLabel()
               
        spinbox = QSpinBox()
        spinbox.setRange(0, 100)
        spinbox.setSingleStep(5)

        dial = QDial()
        dial.setRange(0, 100)
        
        spinbox.valueChanged.connect(
                lambda: self.on_value_changed(
                        spinbox, dial, label))

        dial.valueChanged.connect(
                lambda: self.on_value_changed(
                        dial, spinbox, label))


        layout.addWidget(spinbox, 0, 0)
        layout.addWidget(dial, 0, 4)
        layout.addWidget(label, 1, 0)
        self.setLayout(layout)


    def on_value_changed(self, sender, target, label):

        value = sender.value()
        target.setValue(value)
        label.setText(str(value))



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
