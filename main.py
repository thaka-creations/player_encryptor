import sys
from PyQt5 import QtWidgets

from controllers import main_controllers


class MainWindow(QtWidgets.QMainWindow, main_controllers.MainWindowController):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
