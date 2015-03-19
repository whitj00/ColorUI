from PyQt4 import QtCore, QtGui
import requests,json,sys

global url
url = 'http://dev.opal-coin.com:8080/'


def getBalance():
    global r
    r = requests.post(url + "getbalance").json()

def sendAsset(address,amnt):
    global r2
    payload = {'address': address, 'amount': amnt}
    r2 = requests.post(url + "sendasset", params=payload)


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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(488, 432)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget_2 = QtGui.QTreeWidget(Form)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        self.gridLayout.addWidget(self.treeWidget_2, 0, 0, 1, 2)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        getBalance()
        Form.setWindowTitle(_translate("Form", "ColorUI", None))
        self.treeWidget_2.headerItem().setText(0, _translate("Form", "Addresses", None))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)

        for item in r:
            qi = QtGui.QTreeWidgetItem()
            qi.setText(0, _translate("Form", item['address'], None))
            qi_c = QtGui.QTreeWidgetItem()
            qi_c.setText(0, _translate("Form", item['value'], None))
            qi.addChild(qi_c)
            self.treeWidget_2.addTopLevelItem(qi)

        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("Form", "Assets", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        for item in r:
            for a in item['assets']:
                qi = QtGui.QTreeWidgetItem()
                qi.setText(0, _translate("Form", a['asset_id'], None))
                qi_c = QtGui.QTreeWidgetItem()
                qi_c.setText(0, _translate("Form", a['quantity'], None))
                qi.addChild(qi_c)
                self.treeWidget.addTopLevelItem(qi)

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Amount:", None))
        self.label_3.setText(_translate("Form", "Amount:", None))
        self.label.setText(_translate("Form", "Address:", None))
        self.label_4.setText(_translate("Form", "Address:", None))
        self.pushButton.setText(_translate("Form", "Send Assets", None))
        self.pushButton_2.setText(_translate("Form", "Issue Assets", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())


