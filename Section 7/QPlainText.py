import sys
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainText")

        self.ted = QPlainTextEdit("THis nest was surveyed for consecutive year without any fledgelings")

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.ted)

        self.setLayout(self.lytMain)













if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())