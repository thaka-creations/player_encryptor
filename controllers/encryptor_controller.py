from PyQt5.QtWidgets import QFileDialog

from encryptor_ui import Ui_Encryptor


class EncryptorController(Ui_Encryptor):
    def setupUi(self, Encryptor):
        super().setupUi(Encryptor)
        self.outputDirectoryButton.clicked.connect(self.output_directory_dialog)

    # set the output directory
    def output_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory()
        self.outputDirectoryLabel.setText(f"Output Directory: {directory}")

