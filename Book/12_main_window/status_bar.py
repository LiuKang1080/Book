import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel


class MainWindow(QMainWindow):
    
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.initUi()
        
        
    def initUi(self):
        
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)
        
        self.create_status_bar()
                
        self.show()


    def create_status_bar(self):

        label = QLabel()
        self.statusBar().addWidget(label)
        
        self.centralWidget().textChanged.connect(
                lambda: self.on_text_changed(
                        self.centralWidget(), label))        

    def on_text_changed(self, sender, label):
        
        cursor = sender.textCursor()
        
        size = len(sender.toPlainText())
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        
        label.setText('text size: {}, x: {}, y: {}'.format(size, x, y))
          


def main(args):
    
    app = QApplication(args)
    main_window = MainWindow()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
