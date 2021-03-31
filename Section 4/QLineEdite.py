import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.ledText = QLineEdit("My GUI", self)
        self.ledText.move(45,50)

        self.btnUpdate = QPushButton("Update Title", self)
        self.btnUpdate.move(35, 80)
        self.btnUpdate.clicked.connect(self.evt_btnUpdate_clicked)

    def evt_btnUpdate_clicked(self):
         self.setWindowTitle(self.ledText.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())