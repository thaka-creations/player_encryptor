import utils
import sys
from PyQt5.QtWidgets import QFileDialog, QLabel, QPushButton, QWidget, QDialog, QVBoxLayout
from main_window import Ui_MainWindow
from controllers import login_controller, home_controller


class MainWindowController(Ui_MainWindow):
    def __init__(self):
        if not utils.is_authenticated():
            dialog = QDialog()
            login_dialog = login_controller.LoginController()
            login_dialog.setupUi(dialog)
            self.homeWidget = None
            dialog.exec()

    def setupUi(self, MainWindow):
        if not utils.is_authenticated():
            sys.exit(0)
        super().setupUi(MainWindow)
        widget = QWidget()
        self.homeWidget = home_controller.HomeController()
        self.homeWidget.setupUi(widget)
        layout = QVBoxLayout()
        layout.addWidget(widget)
        self.altMainWidget.setLayout(layout)
