import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200, 200)

        self.Ckb = QCheckBox("Enable", self)
        self.Ckb.move(30, 40)
        self.Ckb.setChecked(True)
        self.Ckb.toggled.connect(self.evt_chkEnable_toggled)

        self.chbThree = QCheckBox("Enable", self)
        self.chbThree.move(30, 70)
        self.chbThree.setTristate(True)
        self.chbThree.stateChanged.connect(self.evt_ckThree_toggled)

        self.lbl = QLabel("Old Text", self)
        self.lbl.move(50, 80)
        self.lbl.resize(100, 100)
        font = QFont("Times New Roman", 20, 75, True, )
        self.lbl.setFont(font)

    def evt_ckThree_toggled(self, state):
        print(state)

    def evt_chkEnable_toggled(self, check):

        if check:
            self.lbl.setDisabled(False)
        else:
            self.lbl.setDisabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())