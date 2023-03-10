import utils
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QLabel, QPushButton, QListWidget, QDialog, QMessageBox
from main_ui import Ui_MainWindow
from controllers import encryptor_controller, login_controller


class MainWindowController(Ui_MainWindow):
    def __init__(self):
        self.productListWidget = QListWidget()

        if not utils.is_authenticated():
            dialog = QDialog()
            login_dialog = login_controller.LoginController()
            login_dialog.setupUi(dialog)
            dialog.exec()

    def setupUi(self, MainWindow):
        if not utils.is_authenticated():
            sys.exit(0)
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

            # write file
            utils.write_file(file)
            print("testing writing single file")

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

                # write file line by line
                print("Writing files to file", [f"{folder}/{file}" for file in files])
                utils.write_lines_to_file([f"{folder}/{file}" for file in files])

            else:
                errorLabel = QLabel()
                errorLabel.setText("No video files found in the selected folder")
                self.altWidgetLayout.addWidget(errorLabel)
                self.altWidgetLayout.addWidget(errorLabel)

    def display_message(self, status_code, message):
        message_box = QMessageBox()
        message_box.setWindowTitle(status_code)
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.Ok)

        if status_code == "Success":
            message_box.setIcon(QMessageBox.Information)
        else:
            message_box.setIcon(QMessageBox.Warning)

        message_box.exec_()

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
                self.display_message("Error", response)
                return
        else:
            selectedProduct = self.productListWidget.currentItem().text()
            self.homeVerticalLayout.removeWidget(self.homeMainWidget)
            self.homeMainWidget.deleteLater()
            ui_encryptor = encryptor_controller.EncryptorController()
            ui_encryptor.setupUi(ui_encryptor)
            self.homeVerticalLayout.addWidget(ui_encryptor)

            # change labels
            ui_encryptor.productLabel.setText(f"Product: {selectedProduct}")

            # read line by line
            file_content = utils.get_file_contents()
            for line in file_content:
                ui_encryptor.encryptorListWidget.addItem(line)







