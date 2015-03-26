from PyQt4 import QtCore, QtGui
import requests,json,sys

global url
url = 'http://dev.opal-coin.com:8080/'


def getBalance():
    global r
    r = requests.post(url + "getbalance").json()

def sendAsset(address,amnt,toaddy):
    global r2
    payload = {'address': address, 'to': toaddy, 'amount': amnt}
    r2 = requests.post(url + "sendasset", params=payload)

def issueAsset(address,amnt,asset):
    global r3
    payload = {'address': address, 'asset': asset, 'amount': amnt}
    r3 = requests.post(url + "issueasset", params=payload)

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
        Form.resize(427, 338)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)
        self.issue_amnt = QtGui.QLineEdit(Form)
        self.issue_amnt.setText(_fromUtf8(""))
        self.issue_amnt.setObjectName(_fromUtf8("issue_amnt"))
        self.gridLayout.addWidget(self.issue_amnt, 9, 2, 1, 1)
        self.addressWidget = QtGui.QTreeWidget(Form)
        self.addressWidget.setObjectName(_fromUtf8("addressWidget"))
        self.gridLayout.addWidget(self.addressWidget, 0, 0, 1, 3)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.send_add = QtGui.QLineEdit(Form)
        self.send_add.setText(_fromUtf8(""))
        self.send_add.setObjectName(_fromUtf8("send_add"))
        self.gridLayout.addWidget(self.send_add, 11, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 2, 1, 1)
        self.sa_btn = QtGui.QPushButton(Form)
        self.sa_btn.setObjectName(_fromUtf8("sa_btn"))
        self.gridLayout.addWidget(self.sa_btn, 13, 0, 1, 1)
        self.ia_btn = QtGui.QPushButton(Form)
        self.ia_btn.setObjectName(_fromUtf8("ia_btn"))
        self.gridLayout.addWidget(self.ia_btn, 13, 2, 1, 1)
        self.assetsWidget = QtGui.QTreeWidget(Form)
        self.assetsWidget.setObjectName(_fromUtf8("assetsWidget"))
        self.gridLayout.addWidget(self.assetsWidget, 2, 0, 1, 3)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 10, 2, 1, 1)
        self.issue_add = QtGui.QLineEdit(Form)
        self.issue_add.setText(_fromUtf8(""))
        self.issue_add.setObjectName(_fromUtf8("issue_add"))
        self.gridLayout.addWidget(self.issue_add, 11, 2, 1, 1)
        self.snd_amnt = QtGui.QLineEdit(Form)
        self.snd_amnt.setText(_fromUtf8(""))
        self.snd_amnt.setObjectName(_fromUtf8("snd_amnt"))
        self.gridLayout.addWidget(self.snd_amnt, 9, 0, 1, 1)
        self.rf_btn = QtGui.QPushButton(Form)
        self.rf_btn.setObjectName(_fromUtf8("rf_btn"))
        self.gridLayout.addWidget(self.rf_btn, 3, 2, 1, 1)
        self.chw_btn = QtGui.QPushButton(Form)
        self.chw_btn.setObjectName(_fromUtf8("chw_btn"))
        self.gridLayout.addWidget(self.chw_btn, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)   

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ColorUI", None))
        self.addressWidget.headerItem().setText(0, _translate("Form", "Addresses", None))
        __sortingEnabled = self.addressWidget.isSortingEnabled()
        self.addressWidget.setSortingEnabled(False)

        for item in r:
            qi = QtGui.QTreeWidgetItem()
            qi.setText(0, _translate("Form", item['address'], None))
            qi_c = QtGui.QTreeWidgetItem()
            qi_c.setText(0, _translate("Form", item['value'], None))
            qi.addChild(qi_c)
            self.addressWidget.addTopLevelItem(qi)

        self.addressWidget.setSortingEnabled(__sortingEnabled)
        self.assetsWidget.headerItem().setText(0, _translate("Form", "Assets", None))
        __sortingEnabled = self.assetsWidget.isSortingEnabled()
        self.assetsWidget.setSortingEnabled(False)

        for item in r:
            print item
            for a in item['assets']:
                qi = QtGui.QTreeWidgetItem()
                qi.setText(0, _translate("Form", a['asset_id'], None))
                qi_c = QtGui.QTreeWidgetItem()
                qi_c.setText(0, _translate("Form", a['quantity'], None))
                qi.addChild(qi_c)
                self.assetsWidget.addTopLevelItem(qi)

        self.assetsWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Ammount:", None))
        self.label_3.setText(_translate("Form", "Ammount:", None))
        self.sa_btn.setText(_translate("Form", "Send Assets", None))
        self.ia_btn.setText(_translate("Form", "Issue Assets", None))
        self.assetsWidget.headerItem().setText(0, _translate("Form", "Assets", None))
        __sortingEnabled = self.assetsWidget.isSortingEnabled()
        self.assetsWidget.setSortingEnabled(False)
        self.assetsWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Form", "Address:", None))
        self.label.setText(_translate("Form", "Address:", None))
        self.rf_btn.setText(_translate("Form", "Refresh", None))
        self.chw_btn.setText(_translate("Form", "Change Wallet", None))
        self.rf_btn.clicked.connect(self.refresh)
        self.chw_btn.clicked.connect(self.chWallet)

    def refresh(self):
        getBalance()

    def chWallet(self):
        ex2.hide()
        ex.show()




class Ui_Form2(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi2(self)
    def setupUi2(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(528, 227)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, -10, 141, 101))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 140, 231, 16))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 110, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 180, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.retranslateUi2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi2(self, Form):
        Form.setWindowTitle(_translate("Form", "ColorUI", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">ColorUI</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "Enter URL:", None))
        self.pushButton.setText(_translate("Form", "Access Wallet", None))
        self.pushButton.clicked.connect(self.screen2)



    def screen2(form):
        ex2.hide()
        ex.show()


if __name__ == '__main__':
    getBalance()
    app2 = QtGui.QApplication(sys.argv)
    global ex2
    ex2 = Ui_Form2()
    ex2.show()
    global ex
    ex = Ui_Form()
    sys.exit(app2.exec_())






