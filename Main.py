import sys
from PyQt5 import QtWidgets
from UI.UI_Main import UiApp


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UiApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
