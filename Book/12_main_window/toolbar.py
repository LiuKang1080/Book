import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QMenu, QAction, QToolBar, QMessageBox, qApp

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.initUi()
        
        
    def initUi(self):
        
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)
        
        self.create_actions()
        self.create_status_bar()
        self.create_menus()
        self.create_toolbar()
                
        self.show()


    def create_actions(self):
 
        self.exit_action = QAction(self.menuBar())
        self.exit_action.setText('Exit')
        self.exit_action.setIcon(QIcon('exit.png'))
        
        self.about_action = QAction(self.menuBar())
        self.about_action.setText('About')  
        self.about_action.setIcon(QIcon('about.png'))    
        
    

    def create_menus(self):
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        
        file_menu.addAction(self.exit_action)
        self.exit_action.triggered.connect(qApp.quit)        
        help_menu = menu_bar.addMenu('Help')
        
        self.about_action.triggered.connect(
                self.display_msgbox)
        
        help_menu.addAction(self.about_action)
        

    def create_status_bar(self):

        label = QLabel()
        self.statusBar().addWidget(label)
        
        self.centralWidget().textChanged.connect(
                lambda: self.on_text_changed(
                        self.centralWidget(), label))        

    def create_toolbar(self):
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.exit_action)
        file_toolbar.addAction(self.about_action)
        file_toolbar.setToolButtonStyle(
                Qt.ToolButtonTextBesideIcon)


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
