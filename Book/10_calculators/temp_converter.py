import sys

'''
T(°F) = T(°C) × 1.8 + 32
T(°C) = (T(°F) - 32) / 1.8
'''



from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLineEdit, QLabel, QGridLayout

from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):            

        
        layout = QGridLayout()
        
        radio_celsius = QRadioButton(
                'Temperature in Celsius scale')
        radio_celsius.setObjectName('c')
        radio_celsius.setChecked(True)        
        
        radio_fahrenheit = QRadioButton(
                'Temperature in Fahrenheit scale')
        radio_fahrenheit.setObjectName('f')

        
        line_temp = QLineEdit()
        line_temp.setText('0')
        
        label_temp = QLabel()
        
        radio_celsius.toggled.connect(
                lambda: self.on_toggled_changed(
                    radio_celsius, line_temp, label_temp)) 
                    
        radio_fahrenheit.toggled.connect(
                lambda: self.on_toggled_changed(
                    radio_fahrenheit, line_temp, label_temp))                     
                
        layout.addWidget(radio_celsius, 0, 0)
        layout.addWidget(radio_fahrenheit, 1, 0)
        layout.addWidget(line_temp, 2, 0)
        layout.addWidget(label_temp, 3, 0)
        
        self.setLayout(layout)
        
        
    def on_toggled_changed(self, sender, line_temp, label_temp):
        
        temperature = float(line_temp.text())
        
        if sender.objectName() == 'c':
            converted_temp = (temperature - 32) / 1.8
        elif sender.objectName() == 'f':
            converted_temp = temperature * 1.8 + 32
            
        label_temp.setText(str(round(converted_temp, 2)))
        

        

def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
