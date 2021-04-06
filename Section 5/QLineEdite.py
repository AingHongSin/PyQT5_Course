import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.ledText = QLineEdit("My GUI", self)
        self.ledText.move(45,50)
        self.ledText. ("Enter a new dialog title")
        self.ledText.setReadOnly(False)
        self.ledText.setEchoMode(QLineEdit.Password)
        self.ledText.setAlignment(Qt.AlignCenter)

        self.btnUpdate = QPushButton("Update Title", self)
        self.btnUpdate.move(35, 80)
        self.btnUpdate.clicked.connect(self.evt_btnUpdate_clicked)
        self.ledText.textChanged.connect(self.evt_ledText_TextChange)

    def evt_ledText_TextChange(self, title):
        self.setWindowTitle(title)

    def evt_btnUpdate_clicked(self):
        msgb = QMessageBox.information(self, "Title Changed", "Your Title has change successfully")
        if msgb == QMessageBox.Yes:
            self.setWindowTitle(self.ledText.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())