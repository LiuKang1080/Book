import sys


from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QGroupBox, QSlider, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt



class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            

        layout = QGridLayout()
        
        vertical_splitter = QSplitter(Qt.Vertical)
        
        left_vertical_group = QGroupBox()
        
        horizontal_slider = QSlider(Qt.Horizontal)
        horizontal_slider.setMinimum(1)
        horizontal_slider.setMaximum(100)
        horizontal_slider.setValue(50)
        
        vertical_slider = QSlider(Qt.Vertical)
        vertical_slider.setMinimum(1)
        vertical_slider.setMaximum(100)
        vertical_slider.setValue(50)
        
        left_vertical_layout = QVBoxLayout()
        
        left_vertical_layout.addWidget(horizontal_slider)
        left_vertical_layout.addWidget(vertical_slider)
        
        left_vertical_group.setLayout(left_vertical_layout)
        
        right_vertical_group = QGroupBox()
        
        label_1 = QLabel()
        label_2 = QLabel()
        
        right_vertical_layout = QVBoxLayout()
        
        right_vertical_layout.addWidget(label_1)
        right_vertical_layout.addWidget(label_2)
        
        right_vertical_group.setLayout(right_vertical_layout)
        
        vertical_splitter.addWidget(left_vertical_group)
        vertical_splitter.addWidget(right_vertical_group)
        
        vertical_splitter.addWidget(left_vertical_group)
        vertical_splitter.addWidget(right_vertical_group)
        layout.addWidget(vertical_splitter)
        
        horizontal_slider.valueChanged.connect(
                lambda: self.on_value_changed(horizontal_slider, label_1))
                
        vertical_slider.valueChanged.connect(
                lambda: self.on_value_changed(
                vertical_slider, label_2))                       
        
        self.setLayout(layout)        
        
        
    def on_value_changed(self, sender, label):
        
        value = str(sender.value())
        label.setText(value)
        


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
