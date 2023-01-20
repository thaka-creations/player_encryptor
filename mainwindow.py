# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 872)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 1441, 831))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        self.stackedWidget.setStyleSheet("background: white;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 1, 1441, 831))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navBarWidget = QtWidgets.QWidget(self.layoutWidget)
        self.navBarWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.navBarWidget.setStyleSheet("background: #5968B0;")
        self.navBarWidget.setObjectName("navBarWidget")
        self.widget = QtWidgets.QWidget(self.navBarWidget)
        self.widget.setGeometry(QtCore.QRect(510, 0, 414, 47))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("color: white;")
        self.homeButton.setFlat(True)
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_2.addWidget(self.homeButton)
        self.profileButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.profileButton.setFont(font)
        self.profileButton.setStyleSheet("color: white;")
        self.profileButton.setFlat(True)
        self.profileButton.setObjectName("profileButton")
        self.horizontalLayout_2.addWidget(self.profileButton)
        self.aboutButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.aboutButton.setFont(font)
        self.aboutButton.setStyleSheet("color: white;")
        self.aboutButton.setFlat(True)
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout_2.addWidget(self.aboutButton)
        self.verticalLayout.addWidget(self.navBarWidget)
        self.altMainWidget = QtWidgets.QWidget(self.layoutWidget)
        self.altMainWidget.setEnabled(True)
        self.altMainWidget.setStyleSheet("")
        self.altMainWidget.setObjectName("altMainWidget")
        self.verticalLayout.addWidget(self.altMainWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget_4 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1441, 831))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.navBarWidget_3 = QtWidgets.QWidget(self.layoutWidget_4)
        self.navBarWidget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.navBarWidget_3.setStyleSheet("background: #5968B0;")
        self.navBarWidget_3.setObjectName("navBarWidget_3")
        self.layoutWidget_5 = QtWidgets.QWidget(self.navBarWidget_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(490, 0, 414, 47))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.homeButton_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.homeButton_3.setFont(font)
        self.homeButton_3.setStyleSheet("color: white;")
        self.homeButton_3.setFlat(True)
        self.homeButton_3.setObjectName("homeButton_3")
        self.horizontalLayout_4.addWidget(self.homeButton_3)
        self.profileButton_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.profileButton_3.setFont(font)
        self.profileButton_3.setStyleSheet("color: white;")
        self.profileButton_3.setFlat(True)
        self.profileButton_3.setObjectName("profileButton_3")
        self.horizontalLayout_4.addWidget(self.profileButton_3)
        self.aboutButton_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.aboutButton_3.setFont(font)
        self.aboutButton_3.setStyleSheet("color: white;")
        self.aboutButton_3.setFlat(True)
        self.aboutButton_3.setObjectName("aboutButton_3")
        self.horizontalLayout_4.addWidget(self.aboutButton_3)
        self.backButton = QtWidgets.QPushButton(self.navBarWidget_3)
        self.backButton.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.backButton.setStyleSheet("color: white;")
        self.backButton.setObjectName("backButton")
        self.verticalLayout_3.addWidget(self.navBarWidget_3)
        self.altMainWidget_3 = QtWidgets.QWidget(self.layoutWidget_4)
        self.altMainWidget_3.setStyleSheet("")
        self.altMainWidget_3.setObjectName("altMainWidget_3")
        self.verticalLayout_3.addWidget(self.altMainWidget_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget_8 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget_8.setGeometry(QtCore.QRect(0, 0, 1441, 831))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.navBarWidget_5 = QtWidgets.QWidget(self.layoutWidget_8)
        self.navBarWidget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.navBarWidget_5.setStyleSheet("background: #5968B0;")
        self.navBarWidget_5.setObjectName("navBarWidget_5")
        self.layoutWidget_9 = QtWidgets.QWidget(self.navBarWidget_5)
        self.layoutWidget_9.setGeometry(QtCore.QRect(490, 0, 414, 47))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.homeButton_5 = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.homeButton_5.setFont(font)
        self.homeButton_5.setStyleSheet("color: white;")
        self.homeButton_5.setFlat(True)
        self.homeButton_5.setObjectName("homeButton_5")
        self.horizontalLayout_7.addWidget(self.homeButton_5)
        self.profileButton_5 = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.profileButton_5.setFont(font)
        self.profileButton_5.setStyleSheet("color: white;")
        self.profileButton_5.setFlat(True)
        self.profileButton_5.setObjectName("profileButton_5")
        self.horizontalLayout_7.addWidget(self.profileButton_5)
        self.aboutButton_5 = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.aboutButton_5.setFont(font)
        self.aboutButton_5.setStyleSheet("color: white;")
        self.aboutButton_5.setFlat(True)
        self.aboutButton_5.setObjectName("aboutButton_5")
        self.horizontalLayout_7.addWidget(self.aboutButton_5)
        self.backButton_3 = QtWidgets.QPushButton(self.navBarWidget_5)
        self.backButton_3.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.backButton_3.setStyleSheet("color: white;")
        self.backButton_3.setObjectName("backButton_3")
        self.verticalLayout_5.addWidget(self.navBarWidget_5)
        self.altMainWidget_5 = QtWidgets.QWidget(self.layoutWidget_8)
        self.altMainWidget_5.setStyleSheet("")
        self.altMainWidget_5.setObjectName("altMainWidget_5")
        self.verticalLayout_5.addWidget(self.altMainWidget_5)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.profileButton.setText(_translate("MainWindow", "PROFILE"))
        self.aboutButton.setText(_translate("MainWindow", "ABOUT"))
        self.homeButton_3.setText(_translate("MainWindow", "HOME"))
        self.profileButton_3.setText(_translate("MainWindow", "PROFILE"))
        self.aboutButton_3.setText(_translate("MainWindow", "ABOUT"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.homeButton_5.setText(_translate("MainWindow", "HOME"))
        self.profileButton_5.setText(_translate("MainWindow", "PROFILE"))
        self.aboutButton_5.setText(_translate("MainWindow", "ABOUT"))
        self.backButton_3.setText(_translate("MainWindow", "Back"))
