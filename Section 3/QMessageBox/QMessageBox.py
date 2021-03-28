import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Show Message", self )
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.MessageBox_Showing)


    def MessageBox_Showing(self):



        # msgBox = QMessageBox.critical(self, "Error", "Your disk drive is almost full")
        # msgBox = QMessageBox.information(self, "Error", "Your disk drive is almost full")
        # msgBox = QMessageBox.warning(self, "Error", "Your disk drive is almost full")
        # msgBox = QMessageBox.about(self, "Error", "Your disk drive is almost full")
        # msgBox = QMessageBox.question(self, "Error", "Your disk drive is almost full")
        #
        # if msgBox == QMessageBox.Yes:
        #     QMessageBox.information(self, "" , "You Clicked Yes")
        # else:
        #     QMessageBox.information(self, "" , "You Clicked No")


        msgBox = QMessageBox()
        msgBox.setWindowTitle("Disk Full")
        msgBox.setText("Your Drive is full")
        msgBox.setDetailedText("Please make some room in your desk")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.exec_()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())