
# The QWidget class is the base class
# of all user interface objects.
# http://doc.qt.io/qt-5/qwidget.html#details

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class HelloWidget(QWidget):


    def __init__(self):
        
        super().__init__()

        self.left = 500
        self.top = 250

        self.width = 600
        self.height = 400
        
        self.setupUi()


    def setupUi(self):

        self.setGeometry(
                self.left, self.top,
                self.width, self.height)
        self.setWindowTitle('Hello, PyQt5')

        label_hello = QLabel('Hello, PyQt5', self)
        label_hello.move(260, 160)
        


def main(args):

    app = QApplication(args)
    hello_window = HelloWidget()
    hello_window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
