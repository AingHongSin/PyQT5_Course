import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Choose Font", self )
        self.btn.move(40, 40)
        self.btn.resize(120, 40)
        font = QFont("Montserrat", 20, 75, True)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.MessageBox_Showing)


    def MessageBox_Showing(self):
        font, bOK = QFontDialog.getFont()

        if bOK:
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())

            self.btn.setFont(font)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())