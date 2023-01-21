import utils
from PyQt5.QtWidgets import QFileDialog, QWidget, QVBoxLayout
from PyQt5.QtCore import QDir
from home_widget import Ui_homeForm
from product_widget import Ui_Form


class HomeController(Ui_homeForm):
    def __init__(self):
        self.productWidget = None

    def setupUi(self, homeForm):
        super().setupUi(homeForm)
        self.selectFileButton.clicked.connect(self.open_file_dialog)
        self.selectFolderButton.clicked.connect(self.open_folder_dialog)
        self.clearFilesButton.clicked.connect(self.clear_files)
        self.createSelectButton.clicked.connect(self.create_select_product)

    def clear_files(self):
        self.fileFolderListWidget.clear()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setWindowTitle("Select Video File")
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mkv)")

        if file_dialog.exec_():
            # clear list widget
            self.clear_files()

            # get the selected file
            file = file_dialog.selectedFiles()[0]
            # extract the file name
            file_name = file.split("/")[-1]
            self.fileFolderListWidget.addItem(file_name)
            self.fileFolderListWidget.addItem(file)

            # write file
            utils.write_file(file)

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

            # clear the list widget
            self.clear_files()

            if files:
                for file in files:
                    self.fileFolderListWidget.addItem(file)
                    self.fileFolderListWidget.addItem(folder)

                # write file line by line
                utils.write_lines_to_file([f"{folder}/{file}" for file in files])
            else:
                self.fileFolderListWidget.addItem("No video files found in the selected folder")

    def create_select_product(self):
        # check if products are available
        status, response = utils.list_products()

        # remove layout from widget
        widget = QWidget()
        self.productWidget = Ui_Form()
        self.productWidget.setupUi(widget)
        layout = QVBoxLayout()
        layout.addWidget(widget)
        self.homeWidget.close()
        self.altMainWidget.setLayout(layout)





