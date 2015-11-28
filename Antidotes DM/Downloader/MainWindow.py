from PyQt4 import QtCore, QtGui
import DownloadBox
from DownloadBox import *
from Proxy import *
from Bugs import *
from About import *
from Credits import *
from multiprocessing import *

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

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(510, 390)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Direct_label = QtGui.QLabel(self.centralwidget)
        self.Direct_label.setGeometry(QtCore.QRect(55, 60, 91, 20))
        self.Direct_label.setObjectName(_fromUtf8("Direct_label"))
        self.Direct_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Direct_lineEdit.setGeometry(QtCore.QRect(180, 60, 141, 20))
        self.Direct_lineEdit.setObjectName(_fromUtf8("Direct_lineEdit"))
        self.Direct_pushButton = QtGui.QPushButton(self.centralwidget)
        self.Direct_pushButton.setGeometry(QtCore.QRect(360, 60, 75, 23))
        self.Direct_pushButton.setObjectName(_fromUtf8("Direct_pushButton"))
        self.EBook_pushButton = QtGui.QPushButton(self.centralwidget)
        self.EBook_pushButton.setGeometry(QtCore.QRect(360, 270, 75, 23))
        self.EBook_pushButton.setObjectName(_fromUtf8("EBook_pushButton"))
        self.EBook_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.EBook_lineEdit.setGeometry(QtCore.QRect(180, 270, 141, 20))
        self.EBook_lineEdit.setObjectName(_fromUtf8("EBook_lineEdit"))
        self.EBook_label = QtGui.QLabel(self.centralwidget)
        self.EBook_label.setGeometry(QtCore.QRect(55, 270, 91, 20))
        self.EBook_label.setObjectName(_fromUtf8("EBook_label"))
        self.Music_pushButton = QtGui.QPushButton(self.centralwidget)
        self.Music_pushButton.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.Music_pushButton.setObjectName(_fromUtf8("Music_pushButton"))
        self.Music_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Music_lineEdit.setGeometry(QtCore.QRect(180, 200, 141, 20))
        self.Music_lineEdit.setObjectName(_fromUtf8("Music_lineEdit"))
        self.Music_label = QtGui.QLabel(self.centralwidget)
        self.Music_label.setGeometry(QtCore.QRect(55, 200, 91, 20))
        self.Music_label.setObjectName(_fromUtf8("Music_label"))
        self.Youtube_pushButton = QtGui.QPushButton(self.centralwidget)
        self.Youtube_pushButton.setGeometry(QtCore.QRect(360, 130, 75, 23))
        self.Youtube_pushButton.setObjectName(_fromUtf8("Youtube_pushButton"))
        self.Youtube_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Youtube_lineEdit.setGeometry(QtCore.QRect(180, 130, 141, 20))
        self.Youtube_lineEdit.setObjectName(_fromUtf8("Youtube_lineEdit"))
        self.Youtube_label = QtGui.QLabel(self.centralwidget)
        self.Youtube_label.setGeometry(QtCore.QRect(55, 130, 91, 20))
        self.Youtube_label.setObjectName(_fromUtf8("Youtube_label"))
##        self.Crawler_pushButton = QtGui.QPushButton(self.centralwidget)
##        self.Crawler_pushButton.setGeometry(QtCore.QRect(360, 130, 75, 23))
##        self.Crawler_pushButton.setObjectName(_fromUtf8("Youtube_pushButton"))
##        self.Crawler_lineEdit = QtGui.QLineEdit(self.centralwidget)
##        self.Crawler_lineEdit.setGeometry(QtCore.QRect(180, 130, 141, 20))
##        self.Crawler_lineEdit.setObjectName(_fromUtf8("Youtube_lineEdit"))
##        self._label = QtGui.QLabel(self.centralwidget)
##        self.Youtube_label.setGeometry(QtCore.QRect(55, 130, 91, 20))
##        self.Youtube_label.setObjectName(_fromUtf8("Youtube_label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAdd_URL = QtGui.QMenu(self.menuFile)
        self.menuAdd_URL.setObjectName(_fromUtf8("menuAdd_URL"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuPrefrences = QtGui.QMenu(self.menuSettings)
        self.menuPrefrences.setObjectName(_fromUtf8("menuPrefrences"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionProxy_Settings = QtGui.QAction(MainWindow)
        self.actionProxy_Settings.setObjectName(_fromUtf8("actionProxy_Settings"))
        self.actionCredits = QtGui.QAction(MainWindow)
        self.actionCredits.setObjectName(_fromUtf8("actionCredits"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionDirect_Download = QtGui.QAction(MainWindow)
        self.actionDirect_Download.setObjectName(_fromUtf8("actionDirect_Download"))
        self.actionYoutube_Download = QtGui.QAction(MainWindow)
        self.actionYoutube_Download.setObjectName(_fromUtf8("actionYoutube_Download"))
        self.actionE_Book_Download = QtGui.QAction(MainWindow)
        self.actionE_Book_Download.setObjectName(_fromUtf8("actionE_Book_Download"))
        self.actionMusic_Download = QtGui.QAction(MainWindow)
        self.actionMusic_Download.setObjectName(_fromUtf8("actionMusic_Download"))
        self.actionBugs_and_Issues = QtGui.QAction(MainWindow)
        self.actionBugs_and_Issues.setObjectName(_fromUtf8("actionBugs_and_Issues"))
        self.menuAdd_URL.addAction(self.actionDirect_Download)
        self.menuAdd_URL.addAction(self.actionYoutube_Download)
        self.menuAdd_URL.addAction(self.actionE_Book_Download)
        self.menuAdd_URL.addAction(self.actionMusic_Download)
        self.menuFile.addAction(self.menuAdd_URL.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPrefrences.addAction(self.actionProxy_Settings)
        self.menuSettings.addAction(self.menuPrefrences.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCredits)
        self.menuHelp.addAction(self.actionBugs_and_Issues)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QObject.connect(self.Direct_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.DirectUrl)
        QtCore.QObject.connect(self.Youtube_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.YoutubeUrl)
        QtCore.QObject.connect(self.Music_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.MusicUrl)
        QtCore.QObject.connect(self.EBook_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.EBookUrl)

        QtCore.QObject.connect(self.Direct_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.DirectUrl)
        QtCore.QObject.connect(self.Youtube_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.YoutubeUrl)
        QtCore.QObject.connect(self.Music_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MusicUrl)
        QtCore.QObject.connect(self.EBook_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.EBookUrl)

        QtCore.QObject.connect(self.Direct_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.Direct_lineEdit.clear)
        QtCore.QObject.connect(self.Youtube_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.Youtube_lineEdit.clear)
        QtCore.QObject.connect(self.Music_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.Music_lineEdit.clear)
        QtCore.QObject.connect(self.EBook_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.EBook_lineEdit.clear)

        QtCore.QObject.connect(self.Direct_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Direct_lineEdit.clear)
        QtCore.QObject.connect(self.Youtube_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Youtube_lineEdit.clear)
        QtCore.QObject.connect(self.Music_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Music_lineEdit.clear)
        QtCore.QObject.connect(self.EBook_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.EBook_lineEdit.clear)

        QtCore.QObject.connect(self.actionProxy_Settings, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Proxy)
        QtCore.QObject.connect(self.actionBugs_and_Issues, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Bugs)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), self.About)
        QtCore.QObject.connect(self.actionCredits, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Credits)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Proxy(self):
        dialog = Ui_ProxyDialog()
        dialog.exec_()

    def Bugs(self):
        dialog = Ui_BugsDialog()
        dialog.exec_()

    def About(self):
        dialog = Ui_AboutDialog()
        dialog.exec_()

    def Credits(self):
        dialog = Ui_CreditsDialog()
        dialog.exec_()

    def DirectUrl(self):
        text = unicode(self.Direct_lineEdit.text())
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'File Name', 'C:/')
        if fileName and text:
            initValues= {'URL': text, 'filename': fileName, 'extractor':'1'}
            print text
            dialog = Ui_Form(initValues)
            dialog.show()
        
    def YoutubeUrl(self):
        text = unicode(self.Youtube_lineEdit.text())
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'File Name', 'C:/', selectedFilter='(*.mp4)')
        if fileName and text:
            initValues= {'URL': text, 'filename': fileName, 'extractor': '2'}
            print text
            dialog = Ui_Form(initValues)
            dialog.show()
        
    def MusicUrl(self):
        text = unicode(self.Music_lineEdit.text())
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'File Name', 'C:/', '(*.mp3)')
        if fileName and text:
            initValues= {'URL': text, 'filename': fileName, 'extractor': '3'}
            print text
            dialog = Ui_Form(initValues)
            dialog.show()
        
    def EBookUrl(self):
        text = unicode(self.EBook_lineEdit.text())
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'File Name', 'C:/', selectedFilter='(*.pdf)')
        if fileName and text:
            initValues= {'URL': text, 'filename': fileName, 'extractor': '4'}
            print text
            #dialog = Ui_Form(initValues)
            #dialog.exec_()
            #t = Process(target=DownloadBox.test, args=(initValues,))
            #t.start()
            window2 = Ui_Form(initValues)
            window2.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Manager", None))
        self.Direct_label.setText(_translate("MainWindow", "Direct Download", None))
        self.Direct_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Downloadable URL", None))
        self.Direct_pushButton.setText(_translate("MainWindow", "Download", None))
        self.EBook_pushButton.setText(_translate("MainWindow", "Search", None))
        self.EBook_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Book Name", None))
        self.EBook_label.setText(_translate("MainWindow", "E-Book Download", None))
        self.Music_pushButton.setText(_translate("MainWindow", "Download", None))
        self.Music_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Music Name", None))
        self.Music_label.setText(_translate("MainWindow", "Music Download", None))
        self.Youtube_pushButton.setText(_translate("MainWindow", "Download", None))
        self.Youtube_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Youtube URL", None))
        self.Youtube_label.setText(_translate("MainWindow", "Youtube Download", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAdd_URL.setTitle(_translate("MainWindow", "Add URL", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuPrefrences.setTitle(_translate("MainWindow", "Prefrences", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the Software", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionProxy_Settings.setText(_translate("MainWindow", "Proxy Settings", None))
        self.actionProxy_Settings.setStatusTip(_translate("MainWindow", "Change Proxy Settings", None))
        self.actionProxy_Settings.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionCredits.setText(_translate("MainWindow", "Credits", None))
        self.actionCredits.setStatusTip(_translate("MainWindow", "Credentials", None))
        self.actionCredits.setShortcut(_translate("MainWindow", "Ctrl+W", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About the Software", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.actionDirect_Download.setText(_translate("MainWindow", "Direct Download", None))
        self.actionDirect_Download.setStatusTip(_translate("MainWindow", "Directly download the file from link", None))
        self.actionYoutube_Download.setText(_translate("MainWindow", "Youtube Download", None))
        self.actionYoutube_Download.setStatusTip(_translate("MainWindow", "Download video from Youtube URL", None))
        self.actionE_Book_Download.setText(_translate("MainWindow", "E-Book Download", None))
        self.actionE_Book_Download.setStatusTip(_translate("MainWindow", "Download E-Books by Name", None))
        self.actionMusic_Download.setText(_translate("MainWindow", "Music Download", None))
        self.actionMusic_Download.setStatusTip(_translate("MainWindow", "Download Music by Name", None))
        self.actionBugs_and_Issues.setText(_translate("MainWindow", "Bugs and Issues", None))
        self.actionBugs_and_Issues.setStatusTip(_translate("MainWindow", "Bugs and Issues", None))
        self.actionBugs_and_Issues.setShortcut(_translate("MainWindow", "Ctrl+B", None))


app = QtGui.QApplication(sys.argv)
win = Ui_MainWindow()
win.show()
app.exec_()


