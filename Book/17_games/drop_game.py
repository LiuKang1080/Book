

import sys, random

from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QEvent
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import qApp

class Window(QWidget):
       
    WIDTH = 860
    HEIGHT = 540
    SPEED = 1000

    def __init__(self):
        
        super().__init__()
               
        self.isStarted = False
        self.isPaused = False

        timer = QTimer()
        timer.setInterval(Window.SPEED)

        self.installEventFilter(qApp)
        self.initUi(timer)
    
        self.show()
          
        
    def initUi(self, timer):

        self.resize(Window.WIDTH, Window.HEIGHT)        
        
        layout = QGridLayout()
        
        button_start = QPushButton('Start')
        button_pause = QPushButton('Pause / Resume')
        
        button_start.clicked.connect(
                lambda: self.start(timer))
        button_pause.clicked.connect(
                lambda: self.pause(timer))
        
        scene = GraphicsScene()
        view = GraphicsView(scene, timer)
       
        layout.addWidget(button_start, 0, 0)
        layout.addWidget(button_pause, 0, 1)
        layout.addWidget(view, 1, 0, 4, 4)
        
        self.setLayout(layout)
        

    def start(self, timer):
        
        if not self.isPaused:
            self.isStarted = True
            timer.start(Window.SPEED)


    def pause(self, timer):
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            timer.stop()            
        else:
            timer.start(Window.SPEED)

        self.update()
        
    
    def eventFilter(self, source, event):
        
        if event.type() == QEvent.KeyPress:
            keyEvent = event
            print(event.key())
            
        #return super(Window, self.eventFilter(source, event))
        return False
        
    
    def keyPressEvent(self, event):
        if event.key() == 0x01000014:
            print('right')



class GraphicsView(QGraphicsView):
    
    
    def __init__(self, scene, timer):
        
        super(GraphicsView, self).__init__()
        
        self.setFixedSize(820, 500)
        
        self.timer = timer
        self.scene = scene   
        self.setScene(self.scene)
        
        self.timer.timeout.connect(self.paint_scene)
        
            
    def paintEvent(self, event):
        
        print('paint event')
        QGraphicsView.paintEvent(self, event)        
           
            
    def paint_scene(self):
        self.scene.add_shapes()
        print('view paint event')        
        
        


class GraphicsScene(QGraphicsScene):
    
    
    def __init__(self):
        
        super(GraphicsScene, self).__init__()
        
        self.sprite_speed = 200
        self.bucket_created = False
        

    def add_bucket(self):
        
        pixmap = QPixmap('images/bucket.png')
        
        self.bucket_item = QGraphicsPixmapItem(pixmap)
        self.bucket_item.setPos(368, 416)
        self.addItem(self.bucket_item)

        self.bucket_created = True


    def add_shapes(self):
        
        self.setSceneRect(0, 0, 800, 480)
        
        if not self.bucket_created:
            self.add_bucket()
        
        print('add shapes')        
        


if __name__ == '__main__':
    
    app = QApplication([])
    window = Window()    
    sys.exit(app.exec_())

