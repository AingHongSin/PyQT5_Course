import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        # self.resize(200, 200)

        self.cmbState = QComboBox(self)
        self.cmbState.move(50, 50)

        # self.cmbState.addItems(["AL", "AI", "ML", "AR", "MI"])
        self.cmbState.addItem("Phnom Penh", {"ab": "PP", "pop": "5000000"})
        self.cmbState.addItem("Kompong Cham", {"ab": "KPC", "pop": "4000000"})
        self.cmbState.addItem("Kompong Som", {"ab": "KPS", "pop": "3000000"})
        self.cmbState.addItem("MindolKiri", {"ab": "MDK", "pop": "2000000"})
        self.cmbState.addItem("Prey Veng", {"ab": "PV", "pop": "1000000"})
        # self.cmbState.currentTextChanged.connect(self.evt_cmbState_Changed)
        self.cmbState.currentIndexChanged.connect(self.evt_cmbState_Changed)
        self.cmbState.highlighted.connect(self.evt_cmbState_hilight)


        self.lbl = QLabel("Population: 5000000", self)
        self.lbl.move(200, 55)


        self.cmbPlants = QComboBox(self)
        self.cmbPlants.resize(190, 20)
        self.cmbPlants.move(50, 80)
        self.cmbPlants.setEditable(True)
        self.cmbPlants.setDuplicatesEnabled(True)
        self.cmbPlants.addItem("Thalictrum occidentalis", "THOC")
        self.cmbPlants.addItem("Bouteloua gracilis", "BOGER")
        self.cmbPlants.addItem("Bromus tectus","BRTE")
        self.cmbPlants.addItem("Picea englemanii", "PIEN")
        self.cmbPlants.currentIndexChanged.connect(self.evt_cmbPlants_Changed)



    # def evt_cmbState_Changed(self, txt):
    #     QMessageBox.information(self, "ComboBox", "You Selected {}".format(txt))

    def evt_cmbState_Changed(self, idx):
        data = self.cmbState.itemData(idx)
        QMessageBox.information(self, "ComboBox", "You Selected {}\nwhich has a population of: {}".format(data['ab'], data['pop']))

    def evt_cmbState_hilight(self, idx):
        self.lbl.setText("Population: {}".format(self.cmbState.itemData(idx)["pop"]))

    def evt_cmbPlants_Changed(self, idx):
        if not self.cmbPlants.itemData(idx):
            sStr, bOk = QInputDialog.getText(self, "Add Species code", "Add a species code for: {}".format(self.cmbPlants.itemData(idx)))
            if bOk:
                self.cmbPlants.setItemData(idx, sStr)
        QMessageBox.information(self, "You Selected", "You selected {}".format(self.cmbPlants.itemData(idx)))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())