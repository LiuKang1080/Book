
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QGridLayout



class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()

        tab_widget = QTabWidget()
        tab_widget.insertTab(0, QLabel('Linux'), 'Linux')
        tab_widget.insertTab(1, QLabel('Windows'), 'Windows')
        tab_widget.insertTab(2, QLabel('Mac'), 'Mac')
        tab_widget.insertTab(3, QLabel('Android'), 'Android')

        label = QLabel()

        tab_widget.currentChanged.connect(
                lambda: self.on_current_changed(
                        tab_widget, label))

        layout.addWidget(tab_widget, 0, 0)
        layout.addWidget(label, 1, 0)
           
        self.setLayout(layout)


    def on_current_changed(self, sender, label):

        text = sender.currentWidget().text()
        label.setText(text)
        



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
