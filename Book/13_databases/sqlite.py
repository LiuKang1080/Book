
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QGridLayout
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex


SELECT_1 = 'Select * From genres'
WHERE_1 = ''
SELECT_2 = 'Select Name, Composer From tracks '
WHERE_2 = ' Where GenreId = {}'


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUi()        
        self.show()
       
        
    def initUi(self):
        
        layout = QGridLayout()
        
        view_genres = QTableView()
        view_tracks = QTableView()
        
        model = TableModel(SELECT_1, WHERE_1)
        
        view_genres.setModel(model)
        view_genres.clicked.connect(
                lambda: self.show_tracks(view_genres, view_tracks))
         
        layout.addWidget(view_genres, 0, 0)
        layout.addWidget(view_tracks, 0, 1)
        
        self.setLayout(layout)


    def show_tracks(self, view_genres, view_tracks):

        selected_index = view_genres.selectedIndexes()[0]
        row = selected_index.row()
        
        genre_id = view_genres.model().table[row][0]
        model = TableModel(SELECT_2, WHERE_2.format(genre_id))
        
        view_tracks.setModel(model)



class TableModel(QAbstractTableModel):
    
    def __init__(self, select_clause, where_clause):
        
        QAbstractTableModel.__init__(self)
        
        select_clause = select_clause
        where_clause = where_clause
        
        self.table = self.get_table(
                select_clause, where_clause)
        
        
    def get_table(self, select_clause, where_clause):
        
        connection = sqlite3.connect('chinook.db')
        
        cursor = connection.cursor()
        cursor.execute(select_clause + where_clause)
                
        rows = cursor.fetchall()
        
        return rows
        
        
    def rowCount(self, parent):
        
        return len(self.table)
        
        
    def columnCount(self, parent):
        
        return len(self.table[0])
        
        
    def data(self, index, role=Qt.DisplayRole):
        
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        
        return self.table[index.row()][index.column()]



def main(args):
    
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main(sys.argv)
