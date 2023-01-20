from PyQt5.QtWidgets import QFileDialog
from home_widget import Ui_homeForm


class HomeController(Ui_homeForm):
    def setupUi(self, homeForm):
        super().setupUi(homeForm)
        self.selectFileButton.clicked.connect(self.open_file_dialog)
        self.selectFolderButton.clicked.connect(self.open_file_dialog)

    # @staticmethod
    # def clear_files(layouts):
    #     for layout in layouts:
    #         while layout.count():
    #             child = layout.takeAt(0)
    #             if child.widget():
    #                 child.widget().deleteLater()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setWindowTitle("Select Video File")
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mkv)")

        if file_dialog.exec_():
            # get the selected file
            file = file_dialog.selectedFiles()[0]
            # extract the file name
            file_name = file.split("/")[-1]
            self.fileFolderListWidget.addItem(file_name)
            self.fileFolderListWidget.addItem(file)


