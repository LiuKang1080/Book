import sys


from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QGroupBox, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt



class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            

        layout = QGridLayout()
        
        horizontal_splitter = QSplitter(Qt.Horizontal)
        
        left_groupbox = QGroupBox('left group box')
        right_groupbox = QGroupBox('right group box')
        
        horizontal_splitter.addWidget(left_groupbox)
        horizontal_splitter.addWidget(right_groupbox)
        
        vertical_splitter_1 = QSplitter(Qt.Vertical)
        
        horizontal_layout_left = QHBoxLayout()
        
        left_groupbox_1 = QGroupBox('left top group box')
        left_groupbox_2 = QGroupBox('left bottom group box')
        vertical_splitter_1.addWidget(left_groupbox_1)
        vertical_splitter_1.addWidget(left_groupbox_2)
        
        horizontal_layout_left.addWidget(vertical_splitter_1)
        left_groupbox.setLayout(horizontal_layout_left)
        
        vertical_splitter_2 = QSplitter(Qt.Vertical)
        
        horizontal_layout_right = QHBoxLayout()
        
        right_groupbox_1 = QGroupBox('right top group box')
        right_groupbox_2 = QGroupBox('right bottom group box')
        vertical_splitter_2.addWidget(right_groupbox_1)
        vertical_splitter_2.addWidget(right_groupbox_2) 
        
        horizontal_layout_right.addWidget(vertical_splitter_2)
        right_groupbox.setLayout(horizontal_layout_right)
        
        layout.addWidget(horizontal_splitter)   
        self.setLayout(layout)        
        

        
def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
