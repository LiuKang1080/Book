import sys


from PyQt5.QtWidgets import QApplication, QWidget, QOpenGLWidget, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor



class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):
            
        self.setMinimumSize(500, 500)

        layout = QGridLayout()
        
        opengl_widget = MyOpenGLWidget()
        layout.addWidget(opengl_widget, 0, 0)

        self.setLayout(layout)        
        


class MyOpenGLWidget(QOpenGLWidget):
    
    def __init__(self, version_profile = None, parent = None):
        
        super(MyOpenGLWidget, self).__init__(parent)
        self.version_profile = version_profile
        
        
    def initializeGL(self):
        
        self.gl = self.context().versionFunctions(self.version_profile)
         
        self.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT)       
        
        
    def paintEvent(self, event):
        
        painter = QPainter()
        
        painter.begin(self)
         
        self.draw_ellipse(event, painter)        
        self.draw_rectangle(event, painter)
        
        painter.end()
        
        
    def draw_ellipse(self, event, painter):
        
        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.red)
        brush = QBrush(Qt.Dense3Pattern)
        brush.setColor(Qt.darkGreen)
        
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(200, 200, 100, 100)
        

    def draw_rectangle(self, event, painter):
        
        pen = QPen(Qt.black, 4, Qt.DashDotLine)
        brush = QBrush(Qt.NoBrush)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(50, 50, 100, 100)
        


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
