from FirstTest import *
import qpageview
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtNetwork
import os

PDFJS = f"file://{os.path.abspath('./web/viewer.html')}"
# PDFJS = 'file:///usr/share/pdf.js/web/viewer.html'
PDF = 'file:///C:/Users/crist/Documents/Coding/PrintVending/Job1.PDF'

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        self.showMaximized()



        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")




class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
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
    window2 = Window()
    window2.setGeometry(600, 50, 800, 600)
    window2.show()
    app.exec_()
