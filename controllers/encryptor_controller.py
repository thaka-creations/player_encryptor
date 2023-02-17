import pickle
import struct
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

    # encrypt files
    def encrypt_files(self):
        request_id = self.productLabel.text().split(": ")[1]
        status, key = utils.retrieve_product(request_id)
        if not status:
            self.display_message("Error", "Product not found")
            return
        fernet = Fernet(key)
        output_directory = self.outputDirectoryLabel.text().split(":")[-1].strip()
        if not output_directory:
            self.display_message("Error", "Please select an output directory")
            return

        # send file to server
        status_code, response = utils.send_encrypted_files(request_id)

        if not status_code:
            self.display_message("Error", response)
            return

        chunk_size = 1024
        for i in response:
            # read file in chunks
            with open(i['file_path'], "rb") as file:
                while True:
                    chunk = file.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    # encrypt the chunk
                    encrypted_chunk = fernet.encrypt(chunk)

                    # write the encrypted chunk
                    with open(f"{output_directory}/{i['name']}", "ab") as f:
                        f.write(encrypted_chunk)

            # # encrypt the file
            # with open(i['file_path'], "rb") as file:
            #     original = file.read()
            #
            # file_name = i['name']
            # file_id = i['video_id'].encode()
            # encrypted = fernet.encrypt(original)
            #
            # # pack the tag and encrypted data into a single binary string
            # packed_data = pickle.dumps((file_id, encrypted))
            #
            # # output the encrypted file
            # with open(f"{output_directory}/{file_name}", "wb") as f:
            #     f.write(packed_data)

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
