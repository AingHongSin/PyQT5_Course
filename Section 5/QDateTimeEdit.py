import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200, 200)

        self.dteDt = QDateTimeEdit(QDate().currentDate(), self)
        self.dteDt.setCalendarPopup(True)
        self.dteDt.move(50, 50)

        self.dtTm = QDateTimeEdit(QTime().currentTime(), self)
        self.dtTm.move(50, 80)

        self.dtDtTm = QDateTimeEdit(QDateTime(QDate.currentDate(), QTime.currentTime()), self)
        self.dtDtTm.move(50, 110)

        self.btn = QPushButton("Elapsed Time", self)
        self.btn.move(50, 150)
        self.btn.clicked.connect(self.evt_btn_Clicked)

    def evt_btn_Clicked(self):
        seconds = QDateTime().currentDateTime().secsTo(self.dtDtTm.dateTime())
        QMessageBox.information(self, "Elapsed Time", "{} seconds have elapsed since {} ".format(seconds, self.dteDt().dateTime().toString()))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())