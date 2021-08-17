from FirstTest import *
from DialogMail import *
from PrintWindow import *
import qpageview
from PyQt5 import QtWebEngineWidgets, QtCore, QtWidgets
from PyQt5 import QtNetwork
import os, sys
import MailManager

PDFJS = 'file://pdf.js/web/viewer.html'
PDF = 'file://'
INITIALFOLDER = '/'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # self.label.setText("Haz clic en el botón")
        # self.pushButton.setText("Presióname")
        #self.showMaximized()



        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.onMailClick)
        self.pushButton_2.clicked.connect(self.onUsbClick)

    def onMailClick(self):
        dlg = DialogMail(self)
        dlg.exec()

    def onUsbClick(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Selecciona un archivo", INITIALFOLDER)[0]
        print(filename)

class DialogMail(QtWidgets.QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.onClickOk)

    #def onInputBoxClick(self):

    def onClickOk(self):
        printFile = MailManager.Download_Attach(self.ui.lineEdit.text())
        prt = Window(self, printFile)
        prt.show()
        sys.exit(prt.exec_())


class PrintWindow(QtWidgets.QMainWindow, Ui_PrintWindow ):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.widget.AllPagesView
        self.widget.paintRequested.connect(self.handlePaintRequest)

    def handlePaintRequest(self, printer):
        self.view.render(QtGui.QPainter(printer))


class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, printFile):
        global PDF
        super(Window, self).__init__()
        PDF = PDF + printFile
        self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))

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
