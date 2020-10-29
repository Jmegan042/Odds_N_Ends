import pandas as pd 
import sys
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication

### A simple graphic interface for converting a CSV file to JSON. 
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.openFileNameDialog()

        def openFileNameDialog(self):
                fileName,_ = QFileDialog.getOpenFileName()
                filename=openFileNameDialog()
                pd.read_csv(filename)
                Filename = filename[:-3]
                pd.to_json(filename+'.json')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())