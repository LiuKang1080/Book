#### 2. Hello, PyQt5! 



Most PyQt5 scripts in this tutorial will have the same basic structure. I will use a simple script that displays a [QLabel](http://doc.qt.io/qt-5/qlabel.html) inside a [QWidget](http://doc.qt.io/qt-5/qwidget.html) to demonstrate this structure.

```python

# The QWidget class is the base class
# of all user interface objects.
# http://doc.qt.io/qt-5/qwidget.html#details

import sys

from PyQt5.QtWidgets import (
        QApplication, QWidget, QLabel)



class HelloWidget(QWidget):


    def __init__(self):
        
        super().__init__()

        self.left = 500
        self.top = 250

        self.width = 600
        self.height = 400
        
        self.setupUi()


    def setupUi(self):
        
        # set the window size and title
        self.setGeometry(
                self.left, self.top,
                self.width, self.height)
        self.setWindowTitle('Hello, PyQt5!')

        label_hello = QLabel('Hello, PyQt5!', self)
        # use absolute positioning for the label
        label_hello.move(260, 160)
        


def main(args):

    app = QApplication(args)
    hello_window = HelloWidget()
    hello_window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)

```

QWidget is the base class for all Qt5 widgets. You can also use it as a top level widget - a window inside which you will display your user interface. Let's walk through the Hello, PyQt5! script.

- Import the necessary Python modules. You need the `sys` module for two things: If your program needs to accept command line arguments you need to use `sys.argv` to make them available to the application and you use `sys.exit` to accept the PyQt5 script exit code, which will be zero if the script executed correctly.

- Import the PyQt5 classes you will use in your script. For this simple script I use only three classes: QApplication, QWidget and QLabel.

- Create a subclass of QWidget. This class is displayed as a top level window - a container that holds all UI widgets. Later in the tutorial you will see that there are other PyQt5 classes you can use as top level containers, but QWidget is the simplest. In the Hello, World! script I named the QWidget subclass `HelloWidget`.

- Inside the `HelloWidget` class you first need to initialize the `QWidget` class itself - this is what `super().__init__()` does. The rest of the `__init__()` method is straightforward - you just set four attributes -  `left`, `top`, `width` and `height`, that are used to define the `HelloWidget` position and size.

- The last statement in `__init__()` is a the call to the `HelloWidget` `setupUi()` method. `setupUi()` contains widget initialization logic. You could put all the initialization logic into `__init__()` but it is better to separate it from the rest of your class initialization.

- Initialize all your widgets in `setupUi()`. The first thing to do is to set `HelloWidget` size and position on the display. I also set the window title to `'Hello, PyQt5!'` - you don't have to do this, but the title is also displayed in the panel taskbar and if your application has a meaningful title it is easier for users to recognize it when the window is minimized.

- Create an instance of the `QLabel` class. The second argument to `QLabel` constructor is `self` which means that `HelloWidget` is `hello_label`'s parent widget. The last `setupUi()` statement positions `hello_label` inside `HelloWidget`. In this script I use absolute positioning - the top left pixel of the `HelloWidget` content area has coordinates `(0, 0)` and I set the `hello_label`'s top left corner to `(260, 160)`, approximately at the center of `HelloWidget`. You will  later see that there are more flexible ways to position widgets then using absolute coordinates.

- The last thing to do is to actually display `HelloWidget` on the screen. I used the recommended [`if __name__ == '__main__'`idiom](https://docs.python.org/3/library/__main__.html) for this to invoke the `main()` function.

- In `main()` , you first create an instance of the [`QApplication` class](http://doc.qt.io/qt-5/qapplication.html). `QApplication` manages the application control flow and main settings and you need precisely one `QApplication` instance for your application.

- Next, you create a `HelloWidget` instance and invoke its `show()` method to display it on the screen. The `QApplication` `exec_()` method starts the main event loop i.e. the application is ready to respond to user actions. When you close the application window an exit code is returned to `sys.exit()` and the program halts.

There are a few things to notice about the Hello, PyQt5! script: PyQt5 doesn't follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) recommendation to use snake case for attribute names - it uses camel case notation instead. Also, I link to the original Qt5 documentation. Qt5 is a GUI toolkit written in C++ and the documentation assumes that you are creating a C++ Qt application. Nevertheless, the Qt5 documentation is very good and you should use it when you need help writing PyQt5 scripts.
