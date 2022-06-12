import sys
from PyQt5 import QtWidgets
import pandas as pd
from PyQt5.QtWidgets import QDialog

from DB import unpivot, users_email_subs
from UI import main_ui
from UI.UI_Plots import PlotFilmViewsCanvas, PlotFilmRatingCanvas, PlotBoxCanvas, PlotFilmRatingScatterCanvas, \
    PlotAvgMarksCanvas
from UI.add_dialog import Ui_AddDialog


# Класс основного окна
class UiApp(QtWidgets.QMainWindow, main_ui.Ui_FilmsDb):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1100, 900)

        db = pd.read_excel('DB.xlsx', sheet_name='First normal form')
        self.loadData(db.to_dict(orient='record'))
        self.loadFilmViewsData(db)
        self.loadFilmRatingsData(db)
        self.loadRejRatingsData(db)
        self.loadSubStatsData(db)

        self.dbTableWidget.setColumnWidth(0, 150)
        self.dbTableWidget.setColumnWidth(1, 150)
        self.dbTableWidget.setColumnWidth(2, 150)
        self.dbTableWidget.setColumnWidth(3, 150)
        self.dbTableWidget.setColumnWidth(4, 150)
        self.dbTableWidget.setColumnWidth(5, 150)
        self.dbTableWidget.setColumnWidth(6, 150)
        self.dbTableWidget.setColumnWidth(7, 150)
        self.dbTableWidget.setColumnWidth(8, 150)
        self.dbTableWidget.setColumnWidth(9, 150)
        self.dbTableWidget.setColumnWidth(10, 150)

        self.dbTableFilmViewsWidget.setColumnWidth(0, 400)
        self.dbTableFilmViewsWidget.setColumnWidth(1, 400)

        self.dbTableFilmRatingsWidget.setColumnWidth(0, 400)
        self.dbTableFilmRatingsWidget.setColumnWidth(1, 400)

        self.dbTableRejRatingsWidget.setColumnWidth(0, 400)
        self.dbTableRejRatingsWidget.setColumnWidth(1, 400)

        self.dbTableSubscribeStatsWidget.setColumnWidth(0, 300)
        self.dbTableSubscribeStatsWidget.setColumnWidth(1, 300)
        self.dbTableSubscribeStatsWidget.setColumnWidth(2, 300)

        self.tableSaveButton.clicked.connect(self.exportData)
        self.tableAddButton.clicked.connect(self.onAddBtnClicked)

        sc = PlotFilmViewsCanvas(self, db)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.tab_6.setLayout(layout)

        sc = PlotAvgMarksCanvas(self, db)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.tab_7.setLayout(layout)

        sc = PlotFilmRatingCanvas(self, db)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.tab_8.setLayout(layout)

        sc = PlotFilmRatingScatterCanvas(self, db)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.tab_9.setLayout(layout)

        sc = PlotBoxCanvas(self, db)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.tab_10.setLayout(layout)

        self.deleteButton.clicked.connect(self.deleteCurrentRowData)

    def exportData(self):
        columnHeaders = []

        for j in range(self.dbTableWidget.model().columnCount()):
            columnHeaders.append(self.dbTableWidget.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        for row in range(self.dbTableWidget.model().rowCount()):
            for col in range(self.dbTableWidget.model().columnCount()):
                df.at[row, columnHeaders[col]] = self.dbTableWidget.item(row, col).text()

        df.to_excel('DB.xlsx', index=False, sheet_name='First normal form')

    def loadData(self, database):
        row = 0

        self.dbTableWidget.setRowCount(len(database))
        self.dbTableWidget.setSortingEnabled(True)
        for data in database:
            self.dbTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data['ID пользователя'])))
            self.dbTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data['Имя пользователя']))
            self.dbTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data['E-mail пользователя']))
            self.dbTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['Наличие Подписки']))
            self.dbTableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data['ID фильма'])))
            self.dbTableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['Название Фильма']))
            self.dbTableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data['ID режиссера'])))
            self.dbTableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(data['Режиссер']))
            self.dbTableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(data['Жанр']))
            self.dbTableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(data['Оценка'])))
            self.dbTableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(data['Время Просмотра'])))
            row += 1

    def loadFilmViewsData(self, database):
        row = 0

        self.dbTableFilmViewsWidget.setRowCount(len(database['Название Фильма'].value_counts()))
        self.dbTableFilmViewsWidget.setSortingEnabled(True)

        for data in database['Название Фильма'].value_counts().to_dict():
            self.dbTableFilmViewsWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data)))
            row += 1
        row = 0
        for data in database['Название Фильма'].value_counts():
            self.dbTableFilmViewsWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data)))
            row += 1

    def loadFilmRatingsData(self, database):
        row = 0

        pivot = pd.pivot_table(database, values='Оценка', index='Название Фильма')

        self.dbTableFilmRatingsWidget.setRowCount(len(pivot))
        self.dbTableFilmRatingsWidget.setSortingEnabled(True)

        for data in pivot.index:
            self.dbTableFilmRatingsWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data)))
            row += 1

        row = 0
        for data in unpivot(pivot)['value']:
            self.dbTableFilmRatingsWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data)))
            row += 1

    def addData(self, database):
        row = self.dbTableWidget.rowCount()
        row += 1
        for data in database:
            self.dbTableWidget.setRowCount(row)
            self.dbTableWidget.setItem(row - 1, 0, QtWidgets.QTableWidgetItem(str(data['ID пользователя'])))
            self.dbTableWidget.setItem(row - 1, 1, QtWidgets.QTableWidgetItem(data['Имя пользователя']))
            self.dbTableWidget.setItem(row - 1, 2, QtWidgets.QTableWidgetItem(data['E-mail пользователя']))
            self.dbTableWidget.setItem(row - 1, 3, QtWidgets.QTableWidgetItem(data['Наличие Подписки']))
            self.dbTableWidget.setItem(row - 1, 4, QtWidgets.QTableWidgetItem(str(data['ID фильма'])))
            self.dbTableWidget.setItem(row - 1, 5, QtWidgets.QTableWidgetItem(data['Название Фильма']))
            self.dbTableWidget.setItem(row - 1, 6, QtWidgets.QTableWidgetItem(str(data['ID режиссера'])))
            self.dbTableWidget.setItem(row - 1, 7, QtWidgets.QTableWidgetItem(data['Режиссер']))
            self.dbTableWidget.setItem(row - 1, 8, QtWidgets.QTableWidgetItem(data['Жанр']))
            self.dbTableWidget.setItem(row - 1, 9, QtWidgets.QTableWidgetItem(str(data['Оценка'])))
            self.dbTableWidget.setItem(row - 1, 10, QtWidgets.QTableWidgetItem(str(data['Время Просмотра'])))
            row += 1

    def loadRejRatingsData(self, database):
        row = 0

        pivot = pd.pivot_table(database, values='Оценка', index='Режиссер')

        self.dbTableRejRatingsWidget.setRowCount(len(pivot))
        self.dbTableRejRatingsWidget.setSortingEnabled(True)

        for data in pivot.index:
            self.dbTableRejRatingsWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data)))
            row += 1

        row = 0
        for data in unpivot(pivot)['value']:
            self.dbTableRejRatingsWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data)))
            row += 1

    def loadSubStatsData(self, database):
        row = 0

        self.dbTableSubscribeStatsWidget.setRowCount(len(users_email_subs(database)))
        self.dbTableSubscribeStatsWidget.setSortingEnabled(True)

        for data in users_email_subs(database)['Имя пользователя']:
            self.dbTableSubscribeStatsWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data)))
            row += 1
        row = 0
        for data in users_email_subs(database)['E-mail пользователя']:
            self.dbTableSubscribeStatsWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data)))
            row += 1
        row = 0
        for data in users_email_subs(database)['Наличие Подписки']:
            self.dbTableSubscribeStatsWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data)))
            row += 1

    def onAddBtnClicked(self):
        dlg = AddDlg(self)
        dlg.exec()
        if dlg.isOk:
            self.addData(dlg.addNewDataToDb().to_dict(orient='record'))
            self.exportData()
            db = pd.read_excel('DB.xlsx', sheet_name='First normal form')
            self.loadData(db.to_dict(orient='record'))
            self.loadFilmViewsData(db)
            self.loadFilmRatingsData(db)
            self.loadRejRatingsData(db)
            self.loadSubStatsData(db)

    def deleteCurrentRowData(self):
        r = self.dbTableWidget.currentRow()
        self.dbTableWidget.removeRow(r)

        self.exportData()
        db = pd.read_excel('DB.xlsx', sheet_name='First normal form')
        self.loadData(db.to_dict(orient='record'))
        self.loadFilmViewsData(db)
        self.loadFilmRatingsData(db)
        self.loadRejRatingsData(db)
        self.loadSubStatsData(db)


##Класс диалога добавления
class AddDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_AddDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.addNewData()

        self.isOk = False

        self.ui.addRowButton.clicked.connect(self.addNewData)
        self.ui.addToDbTable.setColumnWidth(0, 150)
        self.ui.addToDbTable.setColumnWidth(1, 150)
        self.ui.addToDbTable.setColumnWidth(2, 150)
        self.ui.addToDbTable.setColumnWidth(3, 150)
        self.ui.addToDbTable.setColumnWidth(4, 150)
        self.ui.addToDbTable.setColumnWidth(5, 150)
        self.ui.addToDbTable.setColumnWidth(6, 150)
        self.ui.addToDbTable.setColumnWidth(7, 150)
        self.ui.addToDbTable.setColumnWidth(8, 150)
        self.ui.addToDbTable.setColumnWidth(9, 150)
        self.ui.addToDbTable.setColumnWidth(10, 150)

        self.ui.buttonBox.accepted.connect(self.addNewDataToDb)

    def addNewDataToDb(self):
        columnHeaders = []
        self.isOk = True
        for j in range(self.ui.addToDbTable.model().columnCount()):
            columnHeaders.append(self.ui.addToDbTable.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        for row in range(self.ui.addToDbTable.model().rowCount()):
            for col in range(self.ui.addToDbTable.model().columnCount()):
                df.at[row, columnHeaders[col]] = self.ui.addToDbTable.item(row, col).text()

        print(df)

        return df

    def addNewData(self):
        rowPosition = self.ui.addToDbTable.rowCount()

        self.ui.addToDbTable.setRowCount(rowPosition + 1)

        self.ui.addToDbTable.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem("Василий"))
        self.ui.addToDbTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem("Vasiliy@miem.hse.ru"))
        self.ui.addToDbTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem("Нет"))
        self.ui.addToDbTable.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 8, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 9, QtWidgets.QTableWidgetItem("1"))
        self.ui.addToDbTable.setItem(rowPosition, 10, QtWidgets.QTableWidgetItem("1"))
