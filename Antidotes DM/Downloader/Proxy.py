from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ProxyDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Ui_ProxyDialog, self).__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(344, 233)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 60, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 151, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 110, 151, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 60, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 150, 151, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 60, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Save_pushButton = QtGui.QPushButton(Dialog)
        self.Save_pushButton.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.Save_pushButton.setObjectName(_fromUtf8("Save_pushButton"))
        self.Cancel_pushButton = QtGui.QPushButton(Dialog)
        self.Cancel_pushButton.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.Cancel_pushButton.setObjectName(_fromUtf8("Cancel_pushButton"))

        self.retranslateUi(Dialog)

        QtCore.QObject.connect(self.Save_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Save)

        QtCore.QObject.connect(self.Save_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_4.clear)
        QtCore.QObject.connect(self.Save_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.Save_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.Save_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.Cancel_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Save(self):
        address = unicode(self.lineEdit.text())
        port = unicode(self.lineEdit_2.text())
        username = unicode(self.lineEdit_3.text())
        password = unicode(self.lineEdit_4.text())
        final = address + ' ' + port + ' ' + username + ' ' + password
        target = open('Proxy.txt', 'w')
        target.write(final)
        target.close()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Proxy Settings", None))
        self.label.setText(_translate("Dialog", "Address", None))
        self.label_2.setText(_translate("Dialog", "Port", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Address", None))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter Port", None))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Enter Username (optional)", None))
        self.label_3.setText(_translate("Dialog", "Username", None))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Enter Password (optional)", None))
        self.label_4.setText(_translate("Dialog", "Password", None))
        self.Save_pushButton.setText(_translate("Dialog", "Save", None))
        self.Cancel_pushButton.setText(_translate("Dialog", "Cancel", None))

