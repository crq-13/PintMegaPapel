from FirstTest import *
from DialogMail import *
import qpageview
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtNetwork
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # self.label.setText("Haz clic en el botón")
        # self.pushButton.setText("Presióname")
        #self.showMaximized()



        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.onMailClick)

    def onMailClick(self):
        dlg = DialogMail(self)
        dlg.exec()

class DialogMail(QtWidgets.QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.returnPressed.connect(self.ui.lineEdit.clear)

    #def onInputBoxClick(self):




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Handle high resolution displays:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    app.exec_()
