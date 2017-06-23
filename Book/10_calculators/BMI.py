import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout

from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):            

        
        layout = QGridLayout()

        label_weight = QLabel('Your weight (kg)')
        label_height = QLabel('Your height  (m)')
        
        edit_weight = QLineEdit()
        edit_height = QLineEdit()
        label_BMI = QLabel()
        
        button_calculate = QPushButton(
                'Calculate your BMI')
        button_calculate.clicked.connect(
                lambda: self.on_button_calculate_click(
                        edit_weight, edit_height, label_BMI))                
        layout.addWidget(label_weight, 0, 0)
        layout.addWidget(label_height, 1, 0)
        
        layout.addWidget(edit_weight, 0, 1)
        layout.addWidget(edit_height, 1, 1)
        
        layout.addWidget(button_calculate, 2, 0)
        layout.addWidget(label_BMI, 2, 1)
        
        self.setLayout(layout)
        
        
    def on_button_calculate_click(self, edit_weight, edit_height, label_BMI):
        
        weight = float(edit_weight.text())
        height = float(edit_height.text())
        
        BMI = round((weight / (height**2)), 2)
        
        label_BMI.setText(str(BMI))
        

        

def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
