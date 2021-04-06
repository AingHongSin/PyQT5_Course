import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200, 200)

        self.btn = QPushButton("Disable Label", self)
        self.btn.move(40, 40)
        self.btn.setFlat(True)
        self.btn.setIcon(QIcon("Resource/search.png"))
        self.btn.clicked.connect(self.btn_Processing)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(50, 80)
        self.lbl.resize(100, 100)
        font = QFont("Times New Roman", 20, 75, True, )
        self.lbl.setFont(font)

    def btn_Processing(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.lbl.repaint()
            self.btn.setText("Enable Label")
            self.btn.repaint()
        else:
            self.lbl.setEnabled(True)
            self.lbl.repaint()
            self.btn.setText("Disable Label")
            self.btn.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())