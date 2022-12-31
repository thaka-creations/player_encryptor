from PyQt5.QtWidgets import QFileDialog, QMessageBox
from cryptography.fernet import Fernet
import utils
from encryptor_ui import Ui_Encryptor


class EncryptorController(Ui_Encryptor):
    def setupUi(self, Encryptor):
        super().setupUi(Encryptor)
        self.outputDirectoryButton.clicked.connect(self.output_directory_dialog)
        self.startEncryptionButton.clicked.connect(self.encrypt_files)

    # set the output directory
    def output_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory()
        self.outputDirectoryLabel.setText(f"Output Directory: {directory}")

    def encrypt_files(self):
        status, key = utils.retrieve_product(self.productLabel.text().split(": ")[1])
        if not status:
            self.display_message("Error", "Product not found")
            return
        fernet = Fernet(key)
        output_directory = self.outputDirectoryLabel.text().split(":")[-1].strip()
        if not output_directory:
            self.display_message("Error", "Please select an output directory")
            return
        read_paths = utils.get_file_contents()

        for path in read_paths:
            # encrypt the file
            with open(path, "rb") as file:
                original = file.read()

            encrypted = fernet.encrypt(original)

            # output the encrypted file
            with open(f"{output_directory}/{path.split('/')[-1]}", "wb") as f:
                f.write(encrypted)

        self.display_message("Success", "Encryption Completed Successfully")
        return

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

