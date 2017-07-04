

import sys, random

from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor 


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):    

        layout = QGridLayout()

        display = Display(self)
        display.start()
        
        layout.addWidget(display, 1, 1)
        
        self.show()
                


class Display(QWidget):
       
    WIDTH = 800
    HEIGHT = 480
    SPEED = 300

    def __init__(self, parent):
        
        super().__init__(parent)
        self.initDisplay()
        
        
    def initDisplay(self):     

        self.resize(Display.WIDTH, Display.HEIGHT)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.isStarted = False
        self.isPaused = False
        

    def start(self):
        
        if self.isPaused:
            return

        self.isStarted = True
        self.timer.start(Display.SPEED)

        
    def pause(self):
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()            
        else:
            self.timer.start(Board.Speed)

        self.update()

        
    def paintEvent(self, event):
        
        #painter = QPainter(self)
        print('paint event ...')


    def timerEvent(self):
        self.repaint()
        print('timer ...')



if __name__ == '__main__':
    
    app = QApplication([])
    window = Window()    
    sys.exit(app.exec_())
