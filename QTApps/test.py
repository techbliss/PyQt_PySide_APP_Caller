# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sat Jan 10 14:04:44 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Tester(object):
    def setupUi(self, Tester):
        Tester.setObjectName(_fromUtf8("Tester"))
        Tester.resize(906, 516)
        self.label = QtGui.QLabel(Tester)
        self.label.setGeometry(QtCore.QRect(50, 25, 711, 210))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Tester)
        QtCore.QMetaObject.connectSlotsByName(Tester)

    def retranslateUi(self, Tester):
        Tester.setWindowTitle(_translate("Tester", "Tester fot PyQtCaller", None))
        self.label.setText(_translate("Tester", "YOU DID IT M8 ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    Tester = QtGui.QWidget()
    ui = Ui_Tester()
    ui.setupUi(Tester)
    Tester.show()
    app.exec_()

