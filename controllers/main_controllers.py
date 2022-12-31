from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QLabel, QPushButton, QListWidget, QWidget

import utils
from main_ui import Ui_MainWindow
from controllers import encryptor_controller


class MainWindowController(Ui_MainWindow):
    def __init__(self):
        self.productListWidget = QListWidget()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.selectFilesButton.clicked.connect(self.open_file_dialog)
        self.selectFolderButton.clicked.connect(self.open_folder_dialog)
        self.clearFilesButton.clicked.connect(self.clear_files)
        self.createSelectProductButton.clicked.connect(self.create_select_product)

    # clear all widgets from the layouts
    @staticmethod
    def clear_files(layouts):
        for layout in layouts:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setWindowTitle("Select Video File")
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mkv)")

        if file_dialog.exec_():
            # get the selected file
            file = file_dialog.selectedFiles()[0]
            self.clear_files([self.altWidgetLayout])
            # extract the file name
            file_name = file.split("/")[-1]
            fileLabel = QLabel()
            fileLabel.setText(file_name)
            locationLabel = QLabel()
            locationLabel.setText(file)

            self.altWidgetLayout.addWidget(fileLabel)
            self.altWidgetLayout.addWidget(locationLabel)

    def open_folder_dialog(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setWindowTitle("Select Video Folder")

        if folder_dialog.exec_():
            # get the selected folder
            folder = folder_dialog.selectedFiles()[0]
            directory = QDir(folder)
            directory.setNameFilters(["*.mp4", "*.avi", "*.mkv"])
            directory.setFilter(QDir.Files)  # set filter to only show files

            files = directory.entryList()  # list of files in the selected folder
            self.clear_files([self.altWidgetLayout])

            if files:
                for file in files:
                    fileLabel = QLabel()
                    fileLabel.setText(file)
                    locationLabel = QLabel()
                    locationLabel.setText(folder)

                    self.altWidgetLayout.addWidget(fileLabel)
                    self.altWidgetLayout.addWidget(locationLabel)
            else:
                errorLabel = QLabel()
                errorLabel.setText("No video files found in the selected folder")
                self.altWidgetLayout.addWidget(errorLabel)
                self.altWidgetLayout.addWidget(errorLabel)

    def create_select_product(self):
        if self.createSelectProductButton.text() == "Create or Select Product":
            layouts = [self.homeHorizontalLayout, self.altWidgetLayout]
            self.clear_files(layouts)
            newProductButton = QPushButton()
            newProductButton.setText("New Product")

            # check if products are available
            status, response = utils.list_products()

            if status:
                for product in response:
                    self.productListWidget.addItem(f"{product['id']}  {product['name'].title()}")
                self.altWidgetLayout.addWidget(self.productListWidget)

            self.createSelectProductButton.setText("Select Product")
            self.homeHorizontalLayout.addWidget(newProductButton)
        else:
            selectedProduct = self.productListWidget.currentItem().text()
            self.homeVerticalLayout.removeWidget(self.homeMainWidget)
            self.homeMainWidget.deleteLater()
            ui_encryptor = encryptor_controller.EncryptorController()
            ui_encryptor.setupUi(ui_encryptor)
            self.homeVerticalLayout.addWidget(ui_encryptor)

            # change labels
            ui_encryptor.productLabel.setText(f"Product: {selectedProduct}")





