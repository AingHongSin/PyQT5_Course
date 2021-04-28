import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackLayout")
        # self.resize(200,200)

        #### Create Widget
        self.tabMain = QTabWidget()
        self.tabMain.setTabPosition(QTabWidget.West)
        self.tabMain.setMovable(True)
        self.tabMain.setTabsClosable(True)
        self.tabMain.tabCloseRequested.connect(self.evt_tabClosed)

        self.wdgGeneral = QWidget()
        self.wdgSpecies = QWidget()
        self.wdgLocation = QWidget()
        self.wdgSurveys = QWidget()

        #### General Widget

        self.lblNestID = QLabel("34")

        self.dteFound = QDateTimeEdit(QDate(2016, 5, 13))

        self.dteLast = QDateTimeEdit(QDate(2021, 4, 11))

        self.chkActive = QCheckBox()


        #### Species Widget

        self.cmbSpecies = QComboBox()
        self.cmbSpecies.addItem("Red-Tailes Hawk", 300)
        self.cmbSpecies.addItem("Swainsons Hawk", 400)
        self.cmbSpecies.addItem("Other", 1600)

        self.ledSpecies = QLineEdit()

        self.spbBuffer = QSpinBox()
        self.spbBuffer.setValue(800)


        #### Location Widget

        self.spbLatitude = QDoubleSpinBox()
        self.spbLongitude = QDoubleSpinBox()

        #### Survey Widget

        self.lstSurveys = QListWidget()
        self.lstSurveys.addItem("03/04/2021 - MSM - INACTIVE")
        self.lstSurveys.addItem("03/30/2021 - MSM - INACTIVE")
        self.lstSurveys.addItem("04/07/2021 - MSM - INACTIVE")
        self.lstSurveys.addItem("04/14/2021 - MSM - ACTIVE!!")

        self.btnAddSurvey = QPushButton("Add Survey")


        self.setupLayout()

    def setupLayout(self):

        self.lytMain = QHBoxLayout()
        self.lytLeft = QVBoxLayout()

        self.lytMain.addWidget(self.tabMain)

        #### Add Tabs Widgets to tabWidget
        self.tabMain.addTab(self.wdgGeneral, "General")
        self.tabMain.addTab(self.wdgSpecies, "Species")
        self.tabMain.addTab(self.wdgLocation, "Location")
        self.tabMain.addTab(self.wdgSurveys, "Surveys")

        #### Setup General Widget
        self.lytGeneral = QFormLayout()
        self.lytGeneral.addRow("Nest ID:", self.lblNestID)
        self.lytGeneral.addRow("Date Found:", self.dteFound)
        self.lytGeneral.addRow("Date Lasr Surveyed:", self.dteLast)
        self.lytGeneral.addRow("Currently Acive", self.chkActive)
        self.wdgGeneral.setLayout(self.lytGeneral)

        #### Setup Species Widget
        self.lytSpecies = QFormLayout()
        self.lytSpecies.addRow("Species:", self.cmbSpecies)
        self.lytSpecies.addRow("Species:", self.ledSpecies)
        self.lytSpecies.addRow("Buffer:", self.spbBuffer)
        self.spbBuffer.setSuffix(" m")
        self.wdgSpecies.setLayout(self.lytSpecies)

        #### Setup Loaction Widget
        self.lytLocation = QFormLayout()
        self.lytLocation.addRow("Latitude:", self.spbLatitude)
        self.lytLocation.addRow("Longitude:", self.spbLongitude)
        self.wdgLocation.setLayout(self.lytLocation)

        #### Setup Serveys Widget
        self.lytSurveys = QVBoxLayout()
        self.lytSurveys.addWidget(self.lstSurveys)
        self.lytSurveys.addWidget(self.btnAddSurvey)
        self.wdgSurveys.setLayout(self.lytSurveys)

        self.setLayout(self.lytMain)

    def evt_tabClosed(self, idx):
        mes = QMessageBox.question(self, "Closed", "Are you sur that you want to remove tab {}".format(self.tabMain.tabText(idx)))
        if mes == QMessageBox.Yes:
            self.tabMain.removeTab(idx)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())