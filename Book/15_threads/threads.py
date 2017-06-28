

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout

from PyQt5.QtCore import QThread, QObject, pyqtSignal


class Window(QWidget):


    def __init__(self):

        super().__init__()
        self.initUi()
        self.show()


    def initUi(self):

        self.button_start = QPushButton(
                'Start long running task')
        self.button_start.clicked.connect(self.run_task)
        
        self.button_stop = QPushButton(
                'Stop long running task')
        self.button_stop.clicked.connect(self.end_task)
        
        self.label = QLabel()

        self.layout = QGridLayout()        
        self.layout.addWidget(self.button_start, 0, 0)
        self.layout.addWidget(self.button_stop, 1, 0)
        self.layout.addWidget(self.label, 2, 0)
        self.setLayout(self.layout)
        
        
    def run_task(self):
        
        self.thread = QThread()
        
        self.worker = Worker(self.thread)
        self.worker.moveToThread(self.thread)
        self.worker.incremented.connect(
                self.set_label_value)        
        
        self.thread.started.connect(
                self.worker.do_work)
        self.thread.finished.connect(
                self.thread.deleteLater)        
        
        if not self.thread.isRunning():
            self.thread.start()
            
            
    def end_task(self):
        
        self.worker.stop()
        if self.thread.isRunning():
            self.thread.quit()
            self.label.setText('')
            
            
    def set_label_value(self, value):        
        self.label.setText(value)


class Worker(QObject):
    
    incremented = pyqtSignal(str)
    
    
    def __init__(self, thread, parent=None):

        QObject.__init__(self, parent=parent)
        self.thread = thread
        self.stopped = False


    def do_work(self):
        
        for i in range(30):
            
            if not self.stopped:
                print('running . . .')
                self.incremented.emit(str(i))            
                QThread.sleep(1)
        
    
    def stop(self):
        self.stopped = True



def main(args):

    app = QApplication(args)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
