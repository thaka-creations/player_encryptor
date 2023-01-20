# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeForm(object):
    def setupUi(self, homeForm):
        homeForm.setObjectName("homeForm")
        homeForm.resize(1440, 872)
        self.altMainWidget = QtWidgets.QWidget(homeForm)
        self.altMainWidget.setGeometry(QtCore.QRect(5, 0, 16777215, 730))
        self.altMainWidget.setMaximumSize(QtCore.QSize(16777215, 769))
        self.altMainWidget.setStyleSheet("")
        self.altMainWidget.setObjectName("altMainWidget")
        self.widget = QtWidgets.QWidget(self.altMainWidget)
        self.widget.setGeometry(QtCore.QRect(-28, 1, 1461, 721))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectFileButton = QtWidgets.QPushButton(self.widget1)
        self.selectFileButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.selectFileButton.setFont(font)
        self.selectFileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectFileButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectFileButton.setStyleSheet("color: white;\n"
"background: #5968B0;")
        self.selectFileButton.setFlat(False)
        self.selectFileButton.setObjectName("selectFileButton")
        self.horizontalLayout.addWidget(self.selectFileButton)
        self.selectFolderButton = QtWidgets.QPushButton(self.widget1)
        self.selectFolderButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.selectFolderButton.setFont(font)
        self.selectFolderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectFolderButton.setStyleSheet("color:white;\n"
"background: #5968B0;")
        self.selectFolderButton.setAutoDefault(False)
        self.selectFolderButton.setFlat(False)
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.horizontalLayout.addWidget(self.selectFolderButton)
        self.clearFilesButton = QtWidgets.QPushButton(self.widget1)
        self.clearFilesButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.clearFilesButton.setFont(font)
        self.clearFilesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearFilesButton.setStyleSheet("color: white;\n"
"background: #5968B0;")
        self.clearFilesButton.setFlat(False)
        self.clearFilesButton.setObjectName("clearFilesButton")
        self.horizontalLayout.addWidget(self.clearFilesButton)
        self.verticalLayout.addWidget(self.widget1)
        self.fileFolderListWidget = QtWidgets.QListWidget(self.widget)
        self.fileFolderListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fileFolderListWidget.setObjectName("fileFolderListWidget")
        self.verticalLayout.addWidget(self.fileFolderListWidget)
        self.createSelectButton = QtWidgets.QPushButton(self.widget)
        self.createSelectButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.createSelectButton.setFont(font)
        self.createSelectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createSelectButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.createSelectButton.setObjectName("createSelectButton")
        self.verticalLayout.addWidget(self.createSelectButton)

        self.retranslateUi(homeForm)
        QtCore.QMetaObject.connectSlotsByName(homeForm)

    def retranslateUi(self, homeForm):
        _translate = QtCore.QCoreApplication.translate
        homeForm.setWindowTitle(_translate("homeForm", "Form"))
        self.selectFileButton.setText(_translate("homeForm", "Select Files"))
        self.selectFolderButton.setText(_translate("homeForm", "Select Folder"))
        self.clearFilesButton.setText(_translate("homeForm", "Clear Files"))
        self.createSelectButton.setText(_translate("homeForm", "Create or Select Product"))
