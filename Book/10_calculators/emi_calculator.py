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

        label_loan = QLabel('Principal loan amount')
        label_interest = QLabel('Yearly interest (%)')
        label_period = QLabel('Period in months')
        label_payment = QLabel('Monthly payment: ')
        
        edit_loan = QLineEdit()
        edit_interest = QLineEdit()
        edit_period = QLineEdit()
        
        button_calculate = QPushButton('Calculate')
        button_calculate.clicked.connect(
                lambda: self.on_button_calculate_click(
                        edit_loan, edit_interest, edit_period, label_payment))
        
        layout.addWidget(label_loan, 0, 0)
        layout.addWidget(label_interest, 1, 0)
        layout.addWidget(label_period, 2, 0)
        
        layout.addWidget(edit_loan, 0, 1)
        layout.addWidget(edit_interest, 1, 1)
        layout.addWidget(edit_period, 2, 1)
        
        layout.addWidget(button_calculate, 3, 0)
        layout.addWidget(label_payment, 3, 1)

        self.setLayout(layout)
        
        
    def on_button_calculate_click(self, edit_loan, edit_interest, edit_period, label_payment):
        
        loan = float(edit_loan.text())
        interest = float(edit_interest.text())
        interest_per_month = interest / (12 * 100)
        period = float(edit_period.text())

        EMI = (loan * interest_per_month * (1 + interest_per_month)**period) / ((1 + interest_per_month)**period - 1)
        
        text = label_payment.text()
        label_payment.setText(text + str(EMI))
        
        
        

        

def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
