# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 1441, 871))
        self.stackedWidget_2.setStyleSheet("background: white;")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.page_4)
        self.frame_2.setStyleSheet("background: #5968B0;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.homeButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeButton.setFont(font)
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setStyleSheet("background: white;\n"
"color: black;")
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_2.addWidget(self.homeButton)
        self.profileButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.profileButton.setFont(font)
        self.profileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileButton.setStyleSheet("background: white;\n"
"color: black;")
        self.profileButton.setObjectName("profileButton")
        self.horizontalLayout_2.addWidget(self.profileButton)
        self.aboutButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aboutButton.setFont(font)
        self.aboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutButton.setStyleSheet("background: white;\n"
"color: black;")
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout_2.addWidget(self.aboutButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectFilesButton = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.selectFilesButton.setFont(font)
        self.selectFilesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectFilesButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.selectFilesButton.setObjectName("selectFilesButton")
        self.horizontalLayout.addWidget(self.selectFilesButton)
        self.selectFolderButton = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.selectFolderButton.setFont(font)
        self.selectFolderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectFolderButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.horizontalLayout.addWidget(self.selectFolderButton)
        self.clearFilesButton = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clearFilesButton.setFont(font)
        self.clearFilesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearFilesButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.clearFilesButton.setObjectName("clearFilesButton")
        self.horizontalLayout.addWidget(self.clearFilesButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fileFolderListWidget = QtWidgets.QListWidget(self.page)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.fileFolderListWidget.setFont(font)
        self.fileFolderListWidget.setStyleSheet("color: black;")
        self.fileFolderListWidget.setObjectName("fileFolderListWidget")
        self.verticalLayout.addWidget(self.fileFolderListWidget)
        self.createSelectButton = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.createSelectButton.setFont(font)
        self.createSelectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createSelectButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.createSelectButton.setObjectName("createSelectButton")
        self.verticalLayout.addWidget(self.createSelectButton)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backButton = QtWidgets.QPushButton(self.page_2)
        self.backButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.backButton.setObjectName("backButton")
        self.verticalLayout_2.addWidget(self.backButton)
        self.newProductButton = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.newProductButton.setFont(font)
        self.newProductButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newProductButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.newProductButton.setObjectName("newProductButton")
        self.verticalLayout_2.addWidget(self.newProductButton)
        self.productListWidget = QtWidgets.QListWidget(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.productListWidget.setFont(font)
        self.productListWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.productListWidget.setStyleSheet("color: black;")
        self.productListWidget.setObjectName("productListWidget")
        self.verticalLayout_2.addWidget(self.productListWidget)
        self.selectProductButton = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.selectProductButton.setFont(font)
        self.selectProductButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectProductButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.selectProductButton.setObjectName("selectProductButton")
        self.verticalLayout_2.addWidget(self.selectProductButton)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.backButton2 = QtWidgets.QPushButton(self.page_3)
        self.backButton2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backButton2.setFont(font)
        self.backButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton2.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.backButton2.setObjectName("backButton2")
        self.verticalLayout_4.addWidget(self.backButton2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem2)
        self.productLabel = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.productLabel.setFont(font)
        self.productLabel.setStyleSheet("color: black;")
        self.productLabel.setObjectName("productLabel")
        self.verticalLayout_4.addWidget(self.productLabel)
        self.encryptorListWidget = QtWidgets.QListWidget(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.encryptorListWidget.setFont(font)
        self.encryptorListWidget.setStyleSheet("color: black;")
        self.encryptorListWidget.setObjectName("encryptorListWidget")
        self.verticalLayout_4.addWidget(self.encryptorListWidget)
        self.frame = QtWidgets.QFrame(self.page_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.changeContentButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.changeContentButton.setFont(font)
        self.changeContentButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeContentButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.changeContentButton.setObjectName("changeContentButton")
        self.verticalLayout_3.addWidget(self.changeContentButton)
        self.outputDirectoryButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.outputDirectoryButton.setFont(font)
        self.outputDirectoryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outputDirectoryButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.outputDirectoryButton.setObjectName("outputDirectoryButton")
        self.verticalLayout_3.addWidget(self.outputDirectoryButton)
        self.outputDirectoryLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outputDirectoryLabel.setFont(font)
        self.outputDirectoryLabel.setStyleSheet("color: black;")
        self.outputDirectoryLabel.setObjectName("outputDirectoryLabel")
        self.verticalLayout_3.addWidget(self.outputDirectoryLabel)
        self.startEncryptionButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.startEncryptionButton.setFont(font)
        self.startEncryptionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startEncryptionButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.startEncryptionButton.setObjectName("startEncryptionButton")
        self.verticalLayout_3.addWidget(self.startEncryptionButton)
        self.verticalLayout_4.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_3)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.backButton3 = QtWidgets.QPushButton(self.page_6)
        self.backButton3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backButton3.setFont(font)
        self.backButton3.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.backButton3.setObjectName("backButton3")
        self.verticalLayout_6.addWidget(self.backButton3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.frame_5 = QtWidgets.QFrame(self.page_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: black;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.nameEdit = QtWidgets.QLineEdit(self.frame_5)
        self.nameEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet("border: 1px solid grey;\n"
"color: black;")
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout_5.addWidget(self.nameEdit)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: black;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.titleEdit = QtWidgets.QLineEdit(self.frame_5)
        self.titleEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.titleEdit.setFont(font)
        self.titleEdit.setStyleSheet("border: 1px solid grey;\n"
"color: black;")
        self.titleEdit.setText("")
        self.titleEdit.setObjectName("titleEdit")
        self.verticalLayout_5.addWidget(self.titleEdit)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: black;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.shortDescriptionEdit = QtWidgets.QLineEdit(self.frame_5)
        self.shortDescriptionEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.shortDescriptionEdit.setFont(font)
        self.shortDescriptionEdit.setStyleSheet("border: 1px solid grey;\n"
"color: black;")
        self.shortDescriptionEdit.setText("")
        self.shortDescriptionEdit.setObjectName("shortDescriptionEdit")
        self.verticalLayout_5.addWidget(self.shortDescriptionEdit)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.longDescriptionEdit = QtWidgets.QTextEdit(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.longDescriptionEdit.setFont(font)
        self.longDescriptionEdit.setStyleSheet("border: 1px solid grey;\n"
"color: black;")
        self.longDescriptionEdit.setObjectName("longDescriptionEdit")
        self.verticalLayout_5.addWidget(self.longDescriptionEdit)
        self.addProductButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.addProductButton.setFont(font)
        self.addProductButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addProductButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.addProductButton.setObjectName("addProductButton")
        self.verticalLayout_5.addWidget(self.addProductButton)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.page_6)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.page_7)
        self.frame_3.setStyleSheet("background: #5968B0;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.homeButton_2 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeButton_2.setFont(font)
        self.homeButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton_2.setStyleSheet("background: white;\n"
"color: black;")
        self.homeButton_2.setObjectName("homeButton_2")
        self.horizontalLayout_3.addWidget(self.homeButton_2)
        self.profileButton_2 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.profileButton_2.setFont(font)
        self.profileButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileButton_2.setStyleSheet("background: white;\n"
"color: black;")
        self.profileButton_2.setObjectName("profileButton_2")
        self.horizontalLayout_3.addWidget(self.profileButton_2)
        self.aboutButton_2 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aboutButton_2.setFont(font)
        self.aboutButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutButton_2.setStyleSheet("background: white;\n"
"color: black;")
        self.aboutButton_2.setObjectName("aboutButton_2")
        self.horizontalLayout_3.addWidget(self.aboutButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.label_9 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: black;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.frame_6 = QtWidgets.QFrame(self.page_7)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.nameProfileLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nameProfileLabel.setFont(font)
        self.nameProfileLabel.setStyleSheet("color: black;")
        self.nameProfileLabel.setObjectName("nameProfileLabel")
        self.verticalLayout_7.addWidget(self.nameProfileLabel)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem6)
        self.emailProfileLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.emailProfileLabel.setFont(font)
        self.emailProfileLabel.setStyleSheet("color: black;")
        self.emailProfileLabel.setObjectName("emailProfileLabel")
        self.verticalLayout_7.addWidget(self.emailProfileLabel)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem7)
        self.phoneProfileLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.phoneProfileLabel.setFont(font)
        self.phoneProfileLabel.setStyleSheet("color: black;")
        self.phoneProfileLabel.setObjectName("phoneProfileLabel")
        self.verticalLayout_7.addWidget(self.phoneProfileLabel)
        self.logoutButton = QtWidgets.QPushButton(self.frame_6)
        self.logoutButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logoutButton.setFont(font)
        self.logoutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet("background: grey;\n"
"color: white;")
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout_7.addWidget(self.logoutButton)
        self.verticalLayout_9.addWidget(self.frame_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_4 = QtWidgets.QFrame(self.page_5)
        self.frame_4.setStyleSheet("background: #5968B0;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.homeButton_3 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeButton_3.setFont(font)
        self.homeButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton_3.setStyleSheet("background: white;\n"
"color: black;")
        self.homeButton_3.setObjectName("homeButton_3")
        self.horizontalLayout_4.addWidget(self.homeButton_3)
        self.profileButton_3 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.profileButton_3.setFont(font)
        self.profileButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileButton_3.setStyleSheet("background: white;\n"
"color: black;")
        self.profileButton_3.setObjectName("profileButton_3")
        self.horizontalLayout_4.addWidget(self.profileButton_3)
        self.aboutButton_3 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aboutButton_3.setFont(font)
        self.aboutButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutButton_3.setStyleSheet("background: white;\n"
"color: black;")
        self.aboutButton_3.setObjectName("aboutButton_3")
        self.horizontalLayout_4.addWidget(self.aboutButton_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.label_10 = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: black;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.aboutUsBrowser = QtWidgets.QTextBrowser(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.aboutUsBrowser.setFont(font)
        self.aboutUsBrowser.setStyleSheet("color: black;")
        self.aboutUsBrowser.setObjectName("aboutUsBrowser")
        self.verticalLayout_10.addWidget(self.aboutUsBrowser)
        self.stackedWidget_2.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.profileButton.setText(_translate("MainWindow", "PROFILE"))
        self.aboutButton.setText(_translate("MainWindow", "ABOUT"))
        self.selectFilesButton.setText(_translate("MainWindow", "Select Files"))
        self.selectFolderButton.setText(_translate("MainWindow", "Select Folder"))
        self.clearFilesButton.setText(_translate("MainWindow", "Clear Files"))
        self.createSelectButton.setText(_translate("MainWindow", "Create or Select Product"))
        self.backButton.setText(_translate("MainWindow", "BACK"))
        self.newProductButton.setText(_translate("MainWindow", "New Product"))
        self.selectProductButton.setText(_translate("MainWindow", "Select Product"))
        self.backButton2.setText(_translate("MainWindow", "BACK"))
        self.productLabel.setText(_translate("MainWindow", "Header"))
        self.changeContentButton.setText(_translate("MainWindow", "CHANGE CONTENT"))
        self.outputDirectoryButton.setText(_translate("MainWindow", "OUTPUT DIRECTORY"))
        self.outputDirectoryLabel.setText(_translate("MainWindow", "Output Directory:"))
        self.startEncryptionButton.setText(_translate("MainWindow", "START ENCRYPTION"))
        self.backButton3.setText(_translate("MainWindow", "BACK"))
        self.label.setText(_translate("MainWindow", "Create Product"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Title"))
        self.label_3.setText(_translate("MainWindow", "Short description"))
        self.label_2.setText(_translate("MainWindow", "Long description"))
        self.longDescriptionEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>"))
        self.addProductButton.setText(_translate("MainWindow", "Add Product"))
        self.homeButton_2.setText(_translate("MainWindow", "HOME"))
        self.profileButton_2.setText(_translate("MainWindow", "PROFILE"))
        self.aboutButton_2.setText(_translate("MainWindow", "ABOUT"))
        self.label_9.setText(_translate("MainWindow", "PROFILE"))
        self.nameProfileLabel.setText(_translate("MainWindow", "NAME:"))
        self.emailProfileLabel.setText(_translate("MainWindow", "EMAIL:"))
        self.phoneProfileLabel.setText(_translate("MainWindow", "PHONE:"))
        self.logoutButton.setText(_translate("MainWindow", "LOGOUT"))
        self.homeButton_3.setText(_translate("MainWindow", "HOME"))
        self.profileButton_3.setText(_translate("MainWindow", "PROFILE"))
        self.aboutButton_3.setText(_translate("MainWindow", "ABOUT"))
        self.label_10.setText(_translate("MainWindow", "ABOUT"))
        self.aboutUsBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>"))
