import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200, 200)

        self.lbl = QLabel("My Label", self)
        self.lbl.setStyleSheet("color:red; font-size:15px")
        self.lbl.move(50, 30)

        #### Color Button Group
        self.btgColor = QButtonGroup()

        self.rbtRed = QRadioButton("Red", self)
        self.rbtRed.setChecked(True)
        self.rbtRed.move(50, 60)
        self.rbtRed.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtRed)

        self.rbtBlue = QRadioButton("Blue", self)
        self.rbtBlue.move(50, 80)
        self.rbtBlue.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtBlue)

        self.rbtGreen = QRadioButton("Green", self)
        self.rbtGreen.move(50, 100)
        self.rbtGreen.clicked.connect(self.evt_rbt_clicked)
        self.btgColor.addButton(self.rbtGreen)


        #### Size Button Group
        self.btgSize = QButtonGroup()

        self.rbtSmall = QRadioButton("Small", self)
        self.rbtSmall.move(50, 120)
        self.rbtSmall.clicked.connect(self.evt_rbt_clicked)
        self.btgSize.addButton(self.rbtSmall, 10)

        self.rbtMedium = QRadioButton("Medium", self)
        self.rbtMedium.setChecked(True)
        self.rbtMedium.move(50, 140)
        self.rbtMedium.clicked.connect(self.evt_rbt_clicked)
        self.btgSize.addButton(self.rbtMedium, 15)

        self.rbtLarge= QRadioButton("Large", self)
        self.rbtLarge.move(50, 160)
        self.rbtLarge.clicked.connect(self.evt_rbt_clicked)
        self.btgSize.addButton(self.rbtLarge, 20)



    def evt_rbt_clicked(self):
        clr = self.btgColor.checkedButton()
        size = self.btgSize.checkedId()

        ss = "color:" + clr.text() + ";" + "font-size:" + str(size) + "px"
        print(ss)
        self.lbl.setStyleSheet(ss)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())