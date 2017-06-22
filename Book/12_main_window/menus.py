import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QMenu, QAction, QMessageBox, qApp


class MainWindow(QMainWindow):
    
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.initUi()
        
        
    def initUi(self):
        
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)
        
        self.create_status_bar()
        self.create_menus()
                
        self.show()


    def create_menus(self):
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        
        exit_action = QAction(menu_bar)
        exit_action.setText('&Exit')
        exit_action.triggered.connect(qApp.quit)
        
        file_menu.addAction(exit_action)
        
        help_menu = menu_bar.addMenu('&Help')
        
        about_action = QAction(menu_bar)
        about_action.setText('&About')
        
        about_action.triggered.connect(
                self.display_msgbox)
        
        help_menu.addAction(about_action)
        

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
    
    
    def display_msgbox(self):
        
        message_box = QMessageBox()
        message_box.setText('PyQt5 Menu example.')
        message_box.exec()


def main(args):
    
    app = QApplication(args)
    main_window = MainWindow()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
