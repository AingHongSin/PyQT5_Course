import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Show Input", self )
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.MessageBox_Showing)


    def MessageBox_Showing(self):

            ## Text
        # sName, bOK = QInputDialog.getText(self, "Text", "Enter your username")
        # if bOK:
        #     QMessageBox.information(self, "Name", f"Your name is: {sName}")
        # else:
        #     QMessageBox.critical(self, "Canceled", "User Canceled")


            ## Int
        # iAge, bOK = QInputDialog.getInt(self, "Text", "Enter your age", 18, 18, 65, 1)
        # if bOK:
        #     QMessageBox.information(self, "Age", f"Your age is: {str(iAge)}")
        # else:
        #     QMessageBox.critical(self, "Canceled", "User Canceled")


            ## Cost
        # dCost, bOK = QInputDialog.getDouble(self, "Text", "Enter your coffee cost: ", 2.00, 0.1, 10.00, 2)
        # if bOK:
        #     QMessageBox.information(self, "Age", f"Your age is: {str(dCost)}")
        # else:
        #     QMessageBox.critical(self, "Canceled", "User Canceled")


            ## Color
        colorList = ['Red', 'Blue', 'Green', 'Cyan', 'Lime']
        sColor, bOK = QInputDialog.getItem(self, "Text", "Enter your favorite color:", colorList, editable=False)
        if bOK:
            QMessageBox.information(self, "Age", f"Your favorite color is: {sColor}")
        else:
            QMessageBox.critical(self, "Canceled", "User Canceled")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())