import pandas as pd
import sys
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication

### A simple graphic interface for converting a JSON file to CSV. 
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.openFileNameDialog()

    def openFileNameDialog(self):
            fileName,_ = QFileDialog.getOpenFileName()
            Temp_json=pd.read_json(fileName)
            Filename = fileName[:-4]
            Temp_json.to_csv(Filename+'csv')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())