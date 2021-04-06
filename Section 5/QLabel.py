import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Choose Color", self )
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.btn_Processing)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(50, 80)
        self.lbl.resize(100, 100)
        font = QFont("Times New Roman", 20, 75, True,)
        self.lbl.setFont(font)

    def btn_Processing(self):
        # self.lbl.setText("New Text")
        # self.repaint()

        # str = """
        # <h1>Header</h1>
        # <ul>
        #     <li>Red</li>
        #     <li>Blue</li>
        #     <li><Lime/li>
        # </ul>
        # """
        # self.lbl.setText(str)

        pxm = QPixmap('Resource/LovelyHusky.jpg').scaled(100, 100)

        self.lbl.setPixmap(pxm)
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())