from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QLabel

from main_ui import Ui_MainWindow


class MainWindowController(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.selectFilesButton.clicked.connect(self.open_file_dialog)
        self.selectFolderButton.clicked.connect(self.open_folder_dialog)

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
            directory.setFilter(QDir.Files) # set filter to only show files

            files = directory.entryList() # list of files in the selected folder

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


