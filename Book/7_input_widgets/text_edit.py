
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QGridLayout


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()        
        text_edit = QTextEdit()

        html = '''
<div style="color: red;">This line is red</div>
<div style="font-size: 14px;">This line is 14px</div>
<div style="font-weight: bold;">This line is bold</div>
<div style="background-color: LightGray;"></div>
<table border="0.3">
  <tr><th>Month</th><th>Savings</th></tr>
  <tr><td>January</td><td>$100</td></tr>
  <tr><td>February</td><td>$80</td></tr>
</table> 
'''

        text_edit.setHtml(html)

        layout.addWidget(text_edit, 0, 0)
        self.setLayout(layout)



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
