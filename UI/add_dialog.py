# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(1259, 312)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddDialog)
        self.buttonBox.setGeometry(QtCore.QRect(420, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.addToDbTable = QtWidgets.QTableWidget(AddDialog)
        self.addToDbTable.setGeometry(QtCore.QRect(10, 10, 1241, 231))
        self.addToDbTable.setObjectName("addToDbTable")
        self.addToDbTable.setColumnCount(11)
        self.addToDbTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.addToDbTable.setHorizontalHeaderItem(10, item)
        self.addRowButton = QtWidgets.QPushButton(AddDialog)
        self.addRowButton.setGeometry(QtCore.QRect(640, 250, 75, 21))
        self.addRowButton.setObjectName("addRowButton")

        self.retranslateUi(AddDialog)
        self.buttonBox.accepted.connect(AddDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(AddDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDialog.setWindowTitle(_translate("AddDialog", "Add new object to database"))
        item = self.addToDbTable.horizontalHeaderItem(0)
        item.setText(_translate("AddDialog", "ID пользователя"))
        item = self.addToDbTable.horizontalHeaderItem(1)
        item.setText(_translate("AddDialog", "Имя пользователя"))
        item = self.addToDbTable.horizontalHeaderItem(2)
        item.setText(_translate("AddDialog", "E-mail пользователя"))
        item = self.addToDbTable.horizontalHeaderItem(3)
        item.setText(_translate("AddDialog", "Наличие Подписки"))
        item = self.addToDbTable.horizontalHeaderItem(4)
        item.setText(_translate("AddDialog", "ID фильма"))
        item = self.addToDbTable.horizontalHeaderItem(5)
        item.setText(_translate("AddDialog", "Название Фильма"))
        item = self.addToDbTable.horizontalHeaderItem(6)
        item.setText(_translate("AddDialog", "ID режиссера"))
        item = self.addToDbTable.horizontalHeaderItem(7)
        item.setText(_translate("AddDialog", "Режиссер"))
        item = self.addToDbTable.horizontalHeaderItem(8)
        item.setText(_translate("AddDialog", "Жанр"))
        item = self.addToDbTable.horizontalHeaderItem(9)
        item.setText(_translate("AddDialog", "Оценка"))
        item = self.addToDbTable.horizontalHeaderItem(10)
        item.setText(_translate("AddDialog", "Время Просмотра"))
        self.addRowButton.setText(_translate("AddDialog", "Add new row"))
