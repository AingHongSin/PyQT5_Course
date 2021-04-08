import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout")
        # self.resize(200,200)

        #### Create Widgets

        self.ledFirstName = QLineEdit("Elon")
        self.ledLastName = QLineEdit("Musk")
        self.dteStart = QDateTimeEdit()
        self.spbAge = QSpinBox()
        self.btnSubmit = QPushButton("Submit")

        #### Setup Layout

        self.mainLayout = QFormLayout()
        self.mainLayout.setLabelAlignment(Qt.AlignLeft)
        self.mainLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.mainLayout.addRow("First Name: ", self.ledFirstName)
        self.mainLayout.addRow("Last Name: ", self.ledLastName)
        self.mainLayout.addRow("Date Started: ", self.dteStart)
        self.mainLayout.addRow("Age: ", self.spbAge)
        self.mainLayout.addRow("", self.btnSubmit)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())