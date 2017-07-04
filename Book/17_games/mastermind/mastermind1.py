
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QGroupBox, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from game_logic import Game


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()

        self.current_row = 0
        
        self.show()
       
        
    def initUi(self):


        self.game = Game()

        layout = QGridLayout()

        table_results = QTableWidget()
        layout.addWidget(table_results, 2, 1)
        
        table_guesses = QTableWidget()
        layout.addWidget(table_guesses, 2, 2)

        table_selection = QTableWidget()

        self.setup_table_results(table_results)
        self.setup_table_guesses(table_guesses)
        self.setup_table_selection(table_selection, table_guesses, table_results)

        game_buttons = self.setup_game_buttons(table_guesses, table_results)
        layout.addWidget(game_buttons, 1, 1, 1, 4)        
        
        layout.addWidget(table_selection, 2, 3)

        self.setLayout(layout)


    def setup_game_buttons(self, table_guesses, table_results):

        group_box = QGroupBox()

        hbox = QHBoxLayout()
        
        button_newgame = QPushButton('New game')
        button_checkcombo = QPushButton('Check combination')
        button_backspace = QPushButton('Delete symbol')

        button_checkcombo.clicked.connect(
                lambda: self.check_combos(table_guesses, table_results))

        hbox.addWidget(button_newgame)
        hbox.addWidget(button_checkcombo)
        hbox.addWidget(button_backspace)

        group_box.setLayout(hbox)

        return group_box
    

    def setup_table_guesses(self, table_guesses):

        table_guesses.setFixedSize(258, 514)
        table_guesses.horizontalHeader().hide()
        table_guesses.verticalHeader().hide()
        
        table_guesses.setRowCount(8)
        table_guesses.setColumnCount(4)

        for i in range(4):
            table_guesses.setColumnWidth(i, 64)

        for i in range(8):
            table_guesses.setRowHeight(i, 64)


    def setup_table_results(self, table_results):

        table_results.setFixedSize(258, 514)
        table_results.horizontalHeader().hide()
        table_results.verticalHeader().hide()
        
        table_results.setRowCount(8)
        table_results.setColumnCount(4)

        for i in range(4):
            table_results.setColumnWidth(i, 64)

        for i in range(8):
            table_results.setRowHeight(i, 64)        


    def setup_table_selection(self, table_selection, table_guesses, table_results):

        table_selection.setFixedSize(66, 514)
        table_selection.horizontalHeader().hide()
        table_selection.verticalHeader().hide()
        
        table_selection.setRowCount(8)
        table_selection.setColumnCount(1)

        table_selection.setColumnWidth(0, 64)

        for i in range(8):
            table_selection.setRowHeight(i, 64)

        table_selection.cellClicked.connect(
                lambda: self.on_table_selection_cell_clicked(
                        table_selection, table_guesses, table_results))


        for i in range(1, 9):

            label = QLabel()
            label.setFixedSize(64, 64)
            label.setAlignment(Qt.AlignCenter)

            pixmap = QPixmap('icons/{}.png'.format(i))
            pixmap = pixmap.scaledToHeight(34)
            pixmap = pixmap.scaledToWidth(34)

            label.setPixmap(pixmap)

            label.setProperty('element_id', i)

            table_selection.setCellWidget(i - 1, 0, label)


    def set_attempt_combo(self, label, table_guesses):
        print(self.current_row)
        if not hasattr(Window.set_attempt_combo, 'column'):
            Window.set_attempt_combo.column = 0

        if Window.set_attempt_combo.column < 5:    
            if Window.set_attempt_combo.column < 4:
                table_guesses.setCellWidget(
                        self.current_row,
                        Window.set_attempt_combo.column, label)
                Window.set_attempt_combo.column += 1


    def on_table_selection_cell_clicked(self, sender, table_guesses, table_results):

        if not hasattr(Window.set_attempt_combo, 'count'):
            Window.on_table_selection_cell_clicked.count = 0
            
        Window.on_table_selection_cell_clicked.count += 1
        
        if Window.on_table_selection_cell_clicked.count == 5:
            self.current_row += 1
            print(self.current_row)  

        if Window.on_table_selection_cell_clicked.count < 5:
            label = sender.cellWidget(sender.currentRow(), 0)
            
            label_copy = QLabel()
            label_copy.setFixedSize(64, 64)
            label_copy.setAlignment(Qt.AlignCenter)
            
            label_copy.setPixmap(label.pixmap())
            label_copy.setProperty(
                    'element_id', label.property('element_id'))
            self.set_attempt_combo(label_copy, table_guesses)




    def check_combos(self, table_guesses, table_results):

        secret = self.game.secret[:]
        attempt = list()

        for i in range(4):
            label = table_guesses.cellWidget(
                    self.current_row, i)
            attempt.append(label.property('element_id'))
        print(attempt)
        print(secret)

        full, partial = self.game.compare_combos(attempt, secret)
        self.display_results(full, partial, table_results)      


    def display_results(self, full, partial, table_results):

        for i in range(full):
            
            label = QLabel()
            label.setFixedSize(64, 64)
            label.setAlignment(Qt.AlignCenter)

            pixmap = QPixmap('icons/bingo.png')
            pixmap = pixmap.scaledToHeight(34)
            pixmap = pixmap.scaledToWidth(34)

            label.setPixmap(pixmap)

            table_results.setCellWidget(self.current_row, i, label)

        for i in range(partial):
            
            label = QLabel()
            label.setFixedSize(64, 64)
            label.setAlignment(Qt.AlignCenter)

            pixmap = QPixmap('icons/almost.png')
            pixmap = pixmap.scaledToHeight(34)
            pixmap = pixmap.scaledToWidth(34)

            label.setPixmap(pixmap)

            table_results.setCellWidget(self.current_row, i, label)


def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
