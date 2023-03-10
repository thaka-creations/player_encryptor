# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1440, 872)
        self.altMainWidget = QtWidgets.QWidget(Form)
        self.altMainWidget.setGeometry(QtCore.QRect(10, 10, 1169, 689))
        self.altMainWidget.setStyleSheet("")
        self.altMainWidget.setObjectName("altMainWidget")
        self.layoutWidget = QtWidgets.QWidget(self.altMainWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 0, 1171, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(1169, 0))
        self.widget.setMaximumSize(QtCore.QSize(1169, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newProductButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.newProductButton.setFont(font)
        self.newProductButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newProductButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newProductButton.setStyleSheet("color: white;\n"
"background: #5968B0;")
        self.newProductButton.setFlat(False)
        self.newProductButton.setObjectName("newProductButton")
        self.horizontalLayout.addWidget(self.newProductButton)
        self.verticalLayout.addWidget(self.widget)
        self.layoutWidget_2 = QtWidgets.QWidget(self.altMainWidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(2, 72, 1161, 611))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.displayWidget = QtWidgets.QWidget(self.layoutWidget_2)
        self.displayWidget.setStyleSheet("")
        self.displayWidget.setObjectName("displayWidget")
        self.productListWidget = QtWidgets.QListWidget(self.displayWidget)
        self.productListWidget.setGeometry(QtCore.QRect(-5, -9, 1171, 591))
        self.productListWidget.setObjectName("productListWidget")
        self.verticalLayout_2.addWidget(self.displayWidget)
        self.selectProductButton = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.selectProductButton.setFont(font)
        self.selectProductButton.setStyleSheet("background: #5968B0;\n"
"color: white;")
        self.selectProductButton.setObjectName("selectProductButton")
        self.verticalLayout_2.addWidget(self.selectProductButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.newProductButton.setText(_translate("Form", "New Product"))
        self.selectProductButton.setText(_translate("Form", "Select Product"))
