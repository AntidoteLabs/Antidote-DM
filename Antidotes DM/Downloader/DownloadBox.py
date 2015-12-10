from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import requests
import thread
from EBook import *
from Music import *
import time
from multiprocessing import Process
import os

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

try:
    flag = 1
    target = open('Proxy.txt', 'r')
    target_lst = target.read()
    target_lst = target_lst.split()
    address = target_lst[0]
    port = target_lst[1]
    user = target_lst[2]
    password = target_lst[3]

    http_proxy  = "http://" + user + ":" + password + "@" + address + ":" + port
    https_proxy = "http://" + user + ":" + password + "@" + address + ":" + port
    ftp_proxy   = "http://" + user + ":" + password + "@" + address + ":" + port

    proxyDict = {
                  "http"  : http_proxy,
                  "https" : https_proxy,
                  "ftp"   : ftp_proxy
                }
except:
    flag = 0

count = 0
class Ui_Form(QtGui.QWidget):

    filesize = pyqtSignal(int, str)
    pbar = pyqtSignal(str, str)
    speed = pyqtSignal(float, float,str)

    def __init__(self, initValues):
        super(Ui_Form, self).__init__()
        self.initValues = initValues
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(385, 166)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 271, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 271, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 141, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(40, 65, 311, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 130, 81, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        thread.start_new_thread(self.download,(0,'wb'))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Pause)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Cancel)

        self.filesize.connect(self.UpdateFilesize)
        self.pbar.connect(self.UpdatePbar)
        self.speed.connect(self.UpdateSpeed)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Downloading...", None))
        self.label.setText(_translate("Form", "URL : " + self.initValues['URL'], None))
        self.label_2.setText(_translate("Form", "File Name : " + self.initValues['filename'], None))
        self.label_3.setText(_translate("Form", "Speed:", None))
        self.label_4.setText(_translate("Form", "File Size: " , None))
        self.pushButton.setText(_translate("Form", "Pause", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))

    def Cancel(self):
        None

    def UpdateFilesize(self, size,s):
        print size
        self.label_4.setText(_translate("Form", "FileSize: " + str(size) + s, None))

    def UpdatePbar(self, counter, length):
        counter=int(counter)
        length=int(length)
        percentage = counter*100/length
        #print percentage
        self.progressBar.setProperty("value", percentage)

    def UpdateSpeed(self, after, before,y):
        try:
            speed = 1.0/((after-before))
            speed = str(speed)
            self.label_3.setText(_translate("Form", "Speed: " + str(speed) + y, None))
        except:
            self.label_3.setText(_translate("Form","Speed:0"+"KB/s",None))
    def Pause(self):
##        global count
##        if count == 0 :
##            thread.exit()
##            count = 1
##            self.pushButton.setText(_translate("Form", "Resume", None))
##        else:
##            count = 0
##            thread.start_new_thread(target=self.download, args=(1,'ab'))
##            self.pushButton.setText(_translate("Form", "Pause", None))
        None

    def download(self,resume = 0,mode = 'wb'):

        if self.initValues['extractor'] == '3':
            s=music(self.initValues["URL"])
            self.initValues["URL"] = s.song_url
            print s.song_url

        if self.initValues['extractor'] == '4':
            s=Search_ebook(self.initValues["URL"])
            self.initValues["URL"] = s.books_urls[0]

        if flag == 1 and resume == 0:
            r = requests.get(self.initValues["URL"], stream=True, proxies=proxyDict)

        elif flag == 1 and resume == 1 :
            resume_length = os.path.getsize(self.initValues["filename"])
            resume_length = int(resume_length)
            resume_header = {'Range': 'bytes=%d-' % resume_length}
            r = requests.get(self.initValues["URL"], stream=True, proxies=proxyDict, headers=resume_header)

        elif flag == 0 and resume == 0:
            r = requests.get(self.initValues["URL"], stream=True)

        else:
            resume_length = os.path.getsize(self.initValues["filename"])
            resume_length = int(resume_length)
            resume_header = {'Range': 'bytes=%d-' % resume_length}
            r = requests.get(self.initValues["URL"], stream=True, headers=resume_header)

        with open(self.initValues["filename"], mode) as f:
            length=long(r.headers['content-length'])
            if length > 1073741824 :
                x=length/1073741824
                x=int(x)
                self.filesize.emit(x,'GB')
                chunk_size= 1048576
                y='MB/s'
            else:
                x=length/1048576
                x=int(x)
                self.filesize.emit(x,'MB')
                chunk_size=1024
                y='KB/s'
            counter = 0
            print length
            start=time.time()
            now=None
            before=start
            for chunk in r.iter_content(chunk_size):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    counter += chunk_size
                    self.pbar.emit(str(counter),str(length))
                    now=time.time()
                    after=now
                    self.speed.emit(after,before,y)
                    before=after
            if counter >= int(length):
                self.pbar.emit(length,length)



