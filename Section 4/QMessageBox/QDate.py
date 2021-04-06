import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Date", self )
        self.btn.move(40, 40)
        self.btn.resize(120, 40)
        font = QFont("Montserrat", 20, 75, True)
        self.btn.setFont(font)
        self.btn.setStyleSheet('border-radius: 5;'
                               'background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);')
        self.btn.clicked.connect(self.MessageBox_Showing)


    def MessageBox_Showing(self):

        dt = QDate.currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfYear())
        print(dt.dayOfWeek())
        print(dt.addDays(1).toString())

        tm = QTime(14, 30, 20)
        print(tm.toString())

        # tm2 = QTime(20, 14)
        tm2 = tm.addSecs(12)
        print(tm2.toString())
        print(tm.secsTo(tm2))

        dt = QDateTime.currentDateTime()
        print(dt.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())