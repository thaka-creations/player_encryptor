import concurrent.futures
import pickle
import threading

import key_utils
import utils
import sys
import user_utils
from cryptography.fernet import Fernet
from PyQt5.QtCore import QDir, QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog
from main_window import Ui_TafaEncryptor
from controllers import login_controller


class Worker(QObject):
    start_encryption = pyqtSignal()
    finished = pyqtSignal()

    def run(self):
        # Start the event loop for the thread
        self.exec_()


class MainWindowController(Ui_TafaEncryptor):
    emit_display = pyqtSignal(str, str)

    def __init__(self):
        self.should_cancel = False
        self.MainWindow = None
        if not utils.is_authenticated():
            dialog = QDialog()
            login_dialog = login_controller.LoginController()
            login_dialog.setupUi(dialog)
            self.homeWidget = None
            dialog.exec()
        self.thread = QThread()
        self.worker = Worker()

    def setupUi(self, MainWindow):
        if not utils.is_authenticated():
            sys.exit(0)
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # home first view
        self.selectFilesButton.clicked.connect(self.open_file_dialog)
        self.selectFolderButton.clicked.connect(self.open_folder_dialog)
        self.clearFilesButton.clicked.connect(self.clear_files)
        self.createSelectButton.clicked.connect(self.create_select_product)

        # select product view
        self.selectProductButton.clicked.connect(self.select_product)
        self.backButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # threading
        self.worker.moveToThread(self.thread)
        self.worker.start_encryption.connect(self.encrypt_files)
        self.emit_display.connect(self.display_message)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)

        # encryptor view
        self.outputDirectoryButton.clicked.connect(self.output_directory_dialog)
        self.startEncryptionButton.clicked.connect(self.worker.start_encryption.emit)
        self.backButton2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.changeContentButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # navigator
        self.homeButton.clicked.connect(self.navigate_to_home)
        self.homeButton_2.clicked.connect(self.navigate_to_home)
        self.homeButton_3.clicked.connect(self.navigate_to_home)
        self.profileButton.clicked.connect(self.navigate_to_profile)
        self.profileButton_2.clicked.connect(self.navigate_to_profile)
        self.profileButton_3.clicked.connect(self.navigate_to_profile)
        self.aboutButton.clicked.connect(self.navigate_to_about)
        self.aboutButton_2.clicked.connect(self.navigate_to_about)
        self.aboutButton_3.clicked.connect(self.navigate_to_about)

        # logout
        self.logoutButton.clicked.connect(self.logout)

        # new product
        self.newProductButton.clicked.connect(self.navigate_to_new_product)
        self.addProductButton.clicked.connect(self.add_product)
        self.backButton3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def resizeEvent(self, event):
        # get resized window dimensions
        self.stackedWidget_2.setFixedSize(event.size().width(), event.size().height())
        # self.stackedWidget.setFixedHeight(event.size().height() - 10)
        return self.resizeEvent(event)

    def redirect_to_login(self):
        # close main window
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.MainWindow.close()

        # del headers
        utils.delete_headers()

        # open login dialog
        dialog = QDialog()
        login_dialog = login_controller.LoginController(self.MainWindow)
        login_dialog.setupUi(dialog)
        self.homeWidget = None
        dialog.exec()

    def navigate_to_home(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def navigate_to_profile(self):
        # retrieve logged in user details
        status_code, message = user_utils.user_details()
        if not status_code:
            if message == "403":
                self.redirect_to_login()
            else:
                self.display_message("Error", message)
        else:
            self.nameProfileLabel.setText(f'NAME: {message["name"]}')
            self.emailProfileLabel.setText(f'EMAIL: {message["username"]}')
            self.phoneProfileLabel.setText(f'PHONE: {message["phone"]}')
            self.stackedWidget_2.setCurrentIndex(1)

    def navigate_to_about(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def navigate_to_new_product(self):
        self.stackedWidget.setCurrentIndex(3)

    def add_product(self):
        # add product
        payload = {
            "name": self.nameEdit.text(),
            "title": self.titleEdit.text(),
            "short_description": self.shortDescriptionEdit.text(),
            "long_description": self.longDescriptionEdit.toPlainText()
        }
        status_code, message = utils.add_product(payload)
        if status_code:
            self.display_message("Success", message)
            self.nameEdit.clear()
            self.titleEdit.clear()
            self.shortDescriptionEdit.clear()
            self.longDescriptionEdit.clear()
        else:
            if message == "403":
                self.redirect_to_login()
            else:
                self.display_message("Error", message)

    def logout(self):
        status_code, message = user_utils.logout()
        if status_code:
            self.display_message("Success", message)
            self.redirect_to_login()
        else:
            self.display_message("Error", message)

    def open_file_dialog(self):
        # select multiple files
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setWindowTitle("Select Video File")
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mkv)")

        if file_dialog.exec_():
            # get the selected file
            files = file_dialog.selectedFiles()
            for file in files:
                # extract the file name
                file_name = file.split("/")[-1]
                self.fileFolderListWidget.addItem(file_name)
                self.fileFolderListWidget.addItem(file)

            # write file
            utils.write_lines_to_file([file for file in files])

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

            if files:
                for file in files:
                    self.fileFolderListWidget.addItem(file)
                    self.fileFolderListWidget.addItem(folder)

                # write file line by line
                utils.write_lines_to_file([f"{folder}/{file}" for file in files])
            else:
                self.display_message("Error", "No video files found in the selected folder")

    def clear_files(self):
        self.fileFolderListWidget.clear()

    def create_select_product(self):
        # check if widget is blank
        if self.fileFolderListWidget.count() == 0:
            self.display_message("Error", "Please select video files or folders")
            return
        # check if products are available
        status, response = utils.list_products()
        if status:
            self.productListWidget.clear()
            for i in response:
                self.productListWidget.addItem(f"{i['id']} {i['name']}")
        self.stackedWidget.setCurrentIndex(1)

    # select product view
    def select_product(self):
        selectedProduct = self.productListWidget.currentItem()
        if not selectedProduct:
            self.display_message("Error", "Please select a product")
            return
        self.productLabel.setText(f"Product: {selectedProduct.text()}")

        # clear the list widget
        self.encryptorListWidget.clear()
        # read line by line
        file_content = utils.get_file_contents()
        for line in file_content:
            self.encryptorListWidget.addItem(line)
        self.stackedWidget.setCurrentIndex(2)

    # set the output directory
    def output_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory()
        self.outputDirectoryLabel.setText(f"Output Directory: {directory}")

    # encrypt the files
    def encryptor(self, response, output_directory, key):
        try:
            for i in response:
                # read file in chunks
                file_name = i['name']
                file_id = i['video_id'].encode()
                new_file_name = f"{file_name.split('.')[0]}.tafa"
                output_file = f"{output_directory}/{new_file_name}"
                obj = key_utils.EncryptionTool(i['file_path'], key, file_id, output_file)
                for percentage in obj.encrypt():
                    if self.should_cancel:
                        break
                    percentage = "{0:.2f}%".format(percentage)
                    print(percentage)
                self.emit_display.emit("Success", "Encryption Completed Successfully")

                if self.should_cancel:
                    obj.abort()
                    self.emit_display.emit("Error", "Encryption Aborted")
                    return
        except Exception as e:
            print(e)
            self.emit_display.emit("Error", "Encryption Failed")

    def encrypt_files(self):
        request_id = self.productLabel.text().split(": ")[1]
        status, key = utils.retrieve_product(request_id)
        if not status:
            self.display_message("Error", "Product not found")
            return
        # fernet = Fernet(key)
        output_directory = self.outputDirectoryLabel.text().split(":")[-1].strip()
        if not output_directory:
            self.display_message("Error", "Please select an output directory")
            return

        # send file to server
        status_code, response = utils.send_encrypted_files(request_id)

        if not status_code:
            self.display_message("Error", response)
            return
        threading.Thread(target=self.encryptor, args=(response, output_directory, key), daemon=False).start()

    @staticmethod
    def display_message(status_code, message):
        message_box = QMessageBox()
        message_box.setWindowTitle(status_code)
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.Ok)

        if status_code == "Success":
            message_box.setIcon(QMessageBox.Information)
        else:
            message_box.setIcon(QMessageBox.Warning)

        message_box.exec_()
