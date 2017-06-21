import sys


from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QGroupBox, QDateEdit, QLineEdit, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt



class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            

        layout = QGridLayout()
        
        horizontal_splitter = QSplitter(Qt.Horizontal)
        
        left_vertical_group = QGroupBox()
        
        date_edit = QDateEdit()
        line_edit = QLineEdit()
        
        left_vertical_layout = QVBoxLayout()
        
        left_vertical_layout.addWidget(date_edit)
        left_vertical_layout.addWidget(line_edit)
        
        left_vertical_group.setLayout(left_vertical_layout)
        
        right_vertical_group = QGroupBox()
        
        label_date = QLabel()
        label_text = QLabel()
        
        right_vertical_layout = QVBoxLayout()
        
        right_vertical_layout.addWidget(label_date)
        right_vertical_layout.addWidget(label_text)
        
        right_vertical_group.setLayout(right_vertical_layout)
        
        horizontal_splitter.addWidget(left_vertical_group)
        horizontal_splitter.addWidget(right_vertical_group)
        
        horizontal_splitter.addWidget(left_vertical_group)
        horizontal_splitter.addWidget(right_vertical_group)
        layout.addWidget(horizontal_splitter)
        
        date_edit.dateChanged.connect(
                lambda: self.on_date_changed(date_edit, label_date))
                
        line_edit.textChanged.connect(
                lambda: self.on_text_changed(line_edit, label_text))                       
        
        self.setLayout(layout)        
        
        
    def on_date_changed(self, sender, label):
        
        date = sender.date().toString()
        label.setText(date)
        
        
    def on_text_changed(self, sender, label):
        
        text = sender.text()
        label.setText(text)
        


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
