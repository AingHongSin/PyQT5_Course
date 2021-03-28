import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.resize(200,200)

        self.btn = QPushButton("Open File", self )
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.MessageBox_Showing)


    def MessageBox_Showing(self):
        # res = QFileDialog.getOpenFileName(self, "Open File", "/Users/ainghongsin/Desktop/", "PNG File (*.png);; PDF Files (*.pdf)")
        # res = QFileDialog.getSaveFileName(self, "Open File", "/Users/ainghongsin/Desktop/", "PNG File (*.png);; PDF Files (*.pdf)")
        res = QFileDialog.getOpenFileNames(self, "Open File", "/Users/ainghongsin/Desktop/", "PNG File (*.png);; PDF Files (*.pdf)")

        print(res)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())