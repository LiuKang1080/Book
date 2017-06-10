

from PyQt5.QtWidgets import QWidget


def main():

    print('QWidget base classes\n')
    for base_class in QWidget.__bases__:
        print(base_class.__name__)

    print('\nQWidget subclasses\n')
    for subclass in QWidget.__subclasses__():
        print(subclass.__name__)


if __name__ == '__main__':
    main()
