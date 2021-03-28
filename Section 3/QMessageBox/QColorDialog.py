import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Choose Color", self )
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.MessageBox_Showing)


    def MessageBox_Showing(self):
        color = QColorDialog.getColor(QColor("#FF0000"), self, "Choose Color")
        print(color)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())