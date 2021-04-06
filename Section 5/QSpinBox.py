import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)


        self.SpbInt = QSpinBox(self)
        self.SpbInt.move(50, 50)
        self.SpbInt.setWrapping(True)
        self.SpbInt.setRange(0, 10000)
        self.SpbInt.setSingleStep(200)
        self.SpbInt.setValue(1000)
        self.SpbInt.valueChanged.connect(self.evt_spbInt_valueChanged)
        self.SpbInt.editingFinished.connect(self.evt_spbInt_editingFinished)

        self.spbDub = QDoubleSpinBox(self)
        self.spbDub.move(50, 70)
        self.spbDub.setDecimals(5)
        self.spbDub.setSingleStep(0.01)
        self.spbDub.setPrefix("Latitude: ")
        self.spbDub.setSuffix(chr(176))
        self.spbDub.setRange(-90, 90)
        self.spbDub.valueChanged.connect(self.evt_spbDub_valueChanged)

    def evt_spbInt_editingFinished(self):
        res = QMessageBox.critical(self, "Invalid Number", "Invalid value entered \n\nMust be divisible 200")

    def evt_spbDub_valueChanged(self, val):
        print(self.spbDub.text())
        print(self.spbDub.value())


    def evt_spbInt_valueChanged(self, val):
        if (val % 200):
            print(val % 200)
            self.SpbInt.setStyleSheet("color:red;")
        else:
            print(val % 200)
            self.SpbInt.setStyleSheet("color:black;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())