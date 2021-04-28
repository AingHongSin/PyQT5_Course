import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackLayout")

        self.lbxLanguage = QListWidget()
        self.lbxLanguage.addItems(
            ["C", "C++", "C#", "JavaScrip", "Python", "PHP", "Java", "COBOL", "FORTRAN", "Ruby", "Visual Basic",
             "Rust", "Julia", "Go"])
        self.lbxLanguage.sortItems()
        self.lbxLanguage.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lbxLanguage.itemSelectionChanged.connect(self.evt_lbxLanguage_selection)

        self.lbxLanguageIKnow = QListWidget()
        self.lbxLanguageIKnow.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lbxLanguageIKnow.itemSelectionChanged.connect(self.evt_lbxLanguageIKnow_selection)

        self.btnAddLanguage = QPushButton("-->")
        self.btnAddLanguage.clicked.connect(self.evt_btnAdd_clicked)

        self.btnRemoveLanguage = QPushButton("<--")
        self.btnRemoveLanguage.clicked.connect(self.evt_btnRemove_clicked)

        self.btnDoSomeThing = QPushButton("Do Something")
        self.btnDoSomeThing.clicked.connect(self.evt_btnDoSomething_clicked)

        self.setupLayout()

    def setupLayout(self):
        self.lytMain = QVBoxLayout()
        self.lytList = QHBoxLayout()
        self.lytButtons = QVBoxLayout()

        #### Add widget to lytList
        self.lytList.addWidget(self.lbxLanguage)
        self.lytList.addLayout(self.lytButtons)
        self.lytList.addWidget(self.lbxLanguageIKnow)

        #### Add widget  to lytMain
        self.lytMain.addLayout(self.lytList)
        self.lytMain.addWidget(self.btnDoSomeThing)

        #### Add widget to lytButton
        self.lytButtons.addStretch()
        self.lytButtons.addWidget(self.btnAddLanguage)
        self.lytButtons.addWidget(self.btnRemoveLanguage)
        self.lytButtons.addStretch()


        self.setLayout(self.lytMain)

    def evt_btnAdd_clicked(self):
        lstItem = self.lbxLanguage.selectedItems()
        for item in lstItem:
            QLWI = self.lbxLanguage.takeItem(self.lbxLanguage.row(item))
            self.lbxLanguageIKnow.addItem(QLWI)
            print(item)
        self.lbxLanguageIKnow.sortItems()
        self.btnDoSomeThing.setDefault(True)
        self.repaint()
        self.lbxLanguageIKnow.repaint()

    def evt_btnRemove_clicked(self):
        lstrmItems = self.lbxLanguageIKnow.selectedItems()
        for itm  in lstrmItems:
            QLWI = self.lbxLanguageIKnow.takeItem(self.lbxLanguageIKnow.row(itm))
            self.lbxLanguage.addItem(QLWI)
        self.lbxLanguage.sortItems()
        self.btnDoSomeThing.setDefault(True)


    def evt_lbxLanguage_selection(self):
        self.btnAddLanguage.setDefault(True)
        self.repaint()

    def evt_lbxLanguageIKnow_selection(self):
        self.btnRemoveLanguage.setDefault(True)
        self.repaint()

    def evt_btnDoSomething_clicked(self):
        if self.lbxLanguageIKnow.count() == 0:
            QMessageBox.information(self, "Languages", "WOW You don't know any Languages!!!")
        else:
            sLanguage = ""
            for row in range(self.lbxLanguageIKnow.count()):
                print(self.lbxLanguageIKnow.item(row).text())
                sLanguage += self.lbxLanguageIKnow.item(row).text() + "\n"
            QMessageBox.information(self, "Languages", "WOW Your know {} Languages\n\n{}".format(self.lbxLanguageIKnow.count(), sLanguage))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())