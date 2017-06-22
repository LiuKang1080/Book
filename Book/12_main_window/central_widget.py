import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit 


class MainWindow(QMainWindow):
    
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.initUi()
        
        
    def initUi(self):
        
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)

        self.show()



def main(args):
    
    app = QApplication(args)
    main_window = MainWindow()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
