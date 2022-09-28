from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_agregar)

    @Slot()
    def click_agregar(self):
        print("\n\n----------\nDestinoX: ", self.ui.spnnDestinoX.value())
        print("DestinoY: ", self.ui.spnnDestinoY.value())
        print("Velocidad: ", self.ui.txtVelocidad.text())
        print("Rojo: ", self.ui.spnnRed.value())
        print("Azul: ", self.ui.spnnBlue.value())
        print("Verde: ", self.ui.spnnGreen.value())
