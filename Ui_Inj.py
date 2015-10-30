# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\Injection_points\Inj.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1057, 642)
        Dialog.setSizeGripEnabled(True)
        self.lE_1 = QtWidgets.QLineEdit(Dialog)
        self.lE_1.setGeometry(QtCore.QRect(110, 20, 651, 31))
        self.lE_1.setObjectName("lE_1")
        self.lb_1 = QtWidgets.QLabel(Dialog)
        self.lb_1.setGeometry(QtCore.QRect(40, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_1.setFont(font)
        self.lb_1.setObjectName("lb_1")
        self.b_1 = QtWidgets.QPushButton(Dialog)
        self.b_1.setGeometry(QtCore.QRect(790, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_1.setFont(font)
        self.b_1.setObjectName("b_1")
        self.b_2 = QtWidgets.QPushButton(Dialog)
        self.b_2.setGeometry(QtCore.QRect(334, 322, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.b_2.setFont(font)
        self.b_2.setObjectName("b_2")
        self.lW_1 = QtWidgets.QListWidget(Dialog)
        self.lW_1.setGeometry(QtCore.QRect(10, 60, 321, 581))
        self.lW_1.setObjectName("lW_1")
        self.lW_2 = QtWidgets.QListWidget(Dialog)
        self.lW_2.setGeometry(QtCore.QRect(420, 60, 631, 581))
        self.lW_2.setObjectName("lW_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Injection_points"))
        self.lb_1.setText(_translate("Dialog", "文件路径"))
        self.b_1.setText(_translate("Dialog", "加载网站列表"))
        self.b_2.setText(_translate("Dialog", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

