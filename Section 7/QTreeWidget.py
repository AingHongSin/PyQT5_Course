import sys
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackLayout")

        #### Create Widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(3)
        self.trwQt.setHeaderLabels(["QT Class", "Methods", "Signals"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQt_DubleClicked)

        self.populateTree()
        self.trwQt.sortItems(0, Qt.AscendingOrder)
        self.trwQt.setColumnWidth(0, 200)
        self.trwQt.expandItem(self.twiQWidget)

        #### Setup Layout
        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.trwQt)

        self.setLayout(self.lytMain)


    def populateTree(self):

        #### Create topLevel Item

        self.twiQWidget = QTreeWidgetItem(self.trwQt, ["QWidget Module"])
        self.twiGUI = QTreeWidgetItem(self.trwQt, ["QGui Module"])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ["QCore Module"])

        #### Add SubItem to QTWidget Module
        lstQtWidget = ["QDialog", "QLabel", "QLineEdit", "QGroupBox", "QFrame"]
        for cls in lstQtWidget:
            self.twiQWidget.addChild((QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))])))

        #### Add SubItem to QTWidget Module
        lstQtGUI = ["QBitmap", "QColor", "QIcon", "QImage"]
        for cls in lstQtGUI:
            self.twiGUI.addChild((QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))])))

        #### Add SubItem to QTWidget Module
        lstQtCore = ["QThread", "QPixmap", "QUrl", "QFile", "QFrame"]
        for cls in lstQtCore:
            self.twiQCore.addChild((QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))])))

        #### Add Subitem to QDailog Without Variable
        twi = self.trwQt.findItems("QDialog", Qt.MatchRecursive)[0]
        lstQtWidget = ["QFIleDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for cls in lstQtWidget:
            twi.addChild((QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))])))

        #### Add Subitem to QFrame Without Variable
        twi = self.trwQt.findItems("QFrame", Qt.MatchRecursive)[0]
        lstQtWidget = ["QLabel", "QLCDNumber", "QStackedWidget", "QToolBox"]
        for cls in lstQtWidget:
            twi.addChild((QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))])))

        ####
    def evt_trwQt_DubleClicked(self, twi, col):
        QMessageBox.information(self, "QClasses", "You Choose {} Class".format(twi.text(0)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())