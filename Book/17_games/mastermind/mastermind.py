
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()
        
        self.show()
       
        
    def initUi(self):

        layout = QGridLayout()

        table_guesses = QTableView()
        layout.addWidget(table_guesses, 2, 1)
        
        table_results = QTableView()
        layout.addWidget(table_results, 2, 2)

        table_selection = QTableWidget()
        table_selection.setFixedSize(66, 514)
        table_selection.horizontalHeader().hide()
        table_selection.verticalHeader().hide()
        
        table_selection.setRowCount(8)
        table_selection.setColumnCount(1)

        table_selection.setColumnWidth(0, 64)

        for i in range(8):
            table_selection.setRowHeight(i, 64)

        table_selection.cellClicked.connect(
                lambda: self.on_table_selection_cell_clicked(table_selection))

        widget_1 = QWidget()
        label_1 = QLabel()
        label_1.setFixedSize(64, 64)
        label_1.setAlignment(Qt.AlignCenter)
        pixmap_1 = QPixmap('icons/1.png')
        pixmap_1 = pixmap_1.scaledToHeight(34)
        pixmap_1 = pixmap_1.scaledToWidth(34)
        label_1.setPixmap(pixmap_1)
        hbox_1 = QHBoxLayout(widget_1)
        hbox_1.addWidget(label_1)
        widget_1.setLayout(hbox_1)
        table_selection.setCellWidget(0, 0, label_1)

        widget_2 = QWidget()
        label_2 = QLabel()
        label_2.setFixedSize(64, 64)
        label_2.setAlignment(Qt.AlignCenter)        
        pixmap_2 = QPixmap('icons/2.png')
        pixmap_2 = pixmap_2.scaledToHeight(34)
        pixmap_2 = pixmap_2.scaledToWidth(34)
        label_2.setPixmap(pixmap_2)
        hbox_2 = QHBoxLayout(widget_2)
        hbox_2.addWidget(label_2)
        widget_2.setLayout(hbox_2)
        table_selection.setCellWidget(1, 0, label_2)


        widget_3 = QWidget()
        label_3 = QLabel()
        label_3.setFixedSize(64, 64)
        label_3.setAlignment(Qt.AlignCenter)        
        pixmap_3 = QPixmap('icons/3.png')
        pixmap_3 = pixmap_3.scaledToHeight(34)
        pixmap_3 = pixmap_3.scaledToWidth(34)
        label_3.setPixmap(pixmap_3)
        hbox_3 = QHBoxLayout(widget_3)
        hbox_3.addWidget(label_3)
        widget_3.setLayout(hbox_3)
        table_selection.setCellWidget(2, 0, label_3)

        widget_4 = QWidget()
        label_4 = QLabel()
        label_4.setFixedSize(64, 64)
        label_4.setAlignment(Qt.AlignCenter)        
        pixmap_4 = QPixmap('icons/4.png')
        pixmap_4 = pixmap_4.scaledToHeight(34)
        pixmap_4 = pixmap_4.scaledToWidth(34)
        label_4.setPixmap(pixmap_4)
        hbox_4 = QHBoxLayout(widget_4)
        hbox_4.addWidget(label_4)
        widget_4.setLayout(hbox_4)
        table_selection.setCellWidget(3, 0, label_4)

        widget_5 = QWidget()
        label_5 = QLabel()
        label_5.setFixedSize(64, 64)
        label_5.setAlignment(Qt.AlignCenter)        
        pixmap_5 = QPixmap('icons/5.png')
        pixmap_5 = pixmap_5.scaledToHeight(34)
        pixmap_5 = pixmap_5.scaledToWidth(34)
        label_5.setPixmap(pixmap_5)
        hbox_5 = QHBoxLayout(widget_5)
        hbox_5.addWidget(label_5)
        widget_5.setLayout(hbox_5)
        table_selection.setCellWidget(4, 0, label_5)

        widget_6 = QWidget()
        label_6 = QLabel()
        label_6.setFixedSize(64, 64)
        label_6.setAlignment(Qt.AlignCenter)        
        pixmap_6 = QPixmap('icons/6.png')
        pixmap_6 = pixmap_6.scaledToHeight(34)
        pixmap_6 = pixmap_6.scaledToWidth(34)
        label_6.setPixmap(pixmap_6)
        hbox_6 = QHBoxLayout(widget_6)
        hbox_6.addWidget(label_6)
        widget_6.setLayout(hbox_6)
        table_selection.setCellWidget(5, 0, label_6)

        widget_7 = QWidget()
        label_7 = QLabel()
        label_7.setFixedSize(64, 64)
        label_7.setAlignment(Qt.AlignCenter)        
        pixmap_7 = QPixmap('icons/7.png')
        pixmap_7 = pixmap_7.scaledToHeight(34)
        pixmap_7 = pixmap_7.scaledToWidth(34)
        label_7.setPixmap(pixmap_7)
        hbox_7 = QHBoxLayout(widget_7)
        hbox_7.addWidget(label_7)
        widget_7.setLayout(hbox_7)
        table_selection.setCellWidget(6, 0, label_7)

        widget_8 = QWidget()
        label_8 = QLabel()
        label_8.setFixedSize(64, 64)
        label_8.setAlignment(Qt.AlignCenter)        
        pixmap_8 = QPixmap('icons/8.png')
        pixmap_8 = pixmap_8.scaledToHeight(34)
        pixmap_8 = pixmap_8.scaledToWidth(34)
        label_8.setPixmap(pixmap_8)
        hbox_8 = QHBoxLayout(widget_8)
        hbox_8.addWidget(label_8)
        widget_8.setLayout(hbox_8)
        table_selection.setCellWidget(7, 0, label_8)                        
        
        layout.addWidget(table_selection, 2, 3)

        self.setLayout(layout)


    def on_table_selection_cell_clicked(self, sender):
        print(sender.currentRow())


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
