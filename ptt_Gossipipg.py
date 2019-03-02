# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import requests
from bs4 import BeautifulSoup

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 175)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 58, 15))
        self.label_3.setObjectName("label_3")
        self.btnExit = QtWidgets.QPushButton(Form)
        self.btnExit.setGeometry(QtCore.QRect(250, 80, 81, 31))
        self.btnExit.setObjectName("btnExit")
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(160, 80, 81, 31))
        self.btnOK.setObjectName("btnOK")
        self.inputPath = QtWidgets.QTextEdit(Form)
        self.inputPath.setGeometry(QtCore.QRect(20, 40, 311, 31))
        self.inputPath.setObjectName("inputPath")
        self.outputLog = QtWidgets.QTextEdit(Form)
        self.outputLog.setGeometry(QtCore.QRect(20, 120, 311, 31))
        self.outputLog.setObjectName("outputLog")
        self.inputPage = QtWidgets.QTextEdit(Form)
        self.inputPage.setGeometry(QtCore.QRect(90, 80, 61, 31))
        self.inputPage.setObjectName("inputPage")
        self.btnOK.clicked.connect(self.btn_ok)
        self.btnExit.clicked.connect(self.btn_Exit)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PTT Gossiping 爬蟲程式"))
        self.label_2.setText(_translate("Form", "檔案存放位置"))
        self.label_3.setText(_translate("Form", "抓取頁數"))
        self.btnExit.setText(_translate("Form", "離開"))
        self.btnOK.setText(_translate("Form", "開始"))
        self.inputPath.setPlaceholderText(_translate("Form", "C:\\Gossipipg"))
        self.outputLog.setPlaceholderText(_translate("Form", "~~Log~~"))
        self.inputPage.setPlaceholderText(_translate("Form", "3"))
    
    def btn_ok(self):
        iPath=self.inputPath.toPlainText() #讀入InputPath 輸入值
        iPage=self.inputPage.toPlainText() #讀入InputPath 輸入值
        oLog=self.outputLog.setPlaceholderText
        GossipingFun(iPath,iPage,oLog)
    
    def btn_Exit(self):
        print("Bye.")
        sys.exit()
    
def GossipingFun(iPath,iPage,oLog):
    url='http://www.ptt.cc/bbs/Gossiping/index.html'
    payload={
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
    }
    S1=requests.session()
    S=S1.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)
    S=S1.get('https://www.ptt.cc/bbs/Gossiping/index.html',verify=False)
    soup=BeautifulSoup(S.text)
    S4=str(soup.select('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)'))
    S5=re.findall('index(.*?).html">',S4,re.S)
    S6=int(S5[0]*1)
    rePage=int(iPage)
    InPath=iPath
    
    for k in range (S6,S6-rePage,-1):
        print('https://www.ptt.cc/bbs/Gossiping/index'+str(k)+'.html')
        S=S1.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)
        reS=S1.get('https://www.ptt.cc/bbs/Gossiping/index'+str(k)+'.html',verify=False)
        soup2=BeautifulSoup(reS.text)
        S3=[]
        p=0
        p1=1
        for i in soup2.select('.r-ent'):
            S9=str('#main-container > div.r-list-container.action-bar-margin.bbs-screen > div:nth-child('+str(p1+1)+') > div.title > a')
            S10=str('https://www.ptt.cc/'+str(re.findall('href="(.*?)">',str(soup2.select(S9)),re.S))[3:40])
            S2=[i.select('.date')[0].text, re.findall("\n(.*?)\n",i.select('.title')[0].text,re.S),i.select('.author')[0].text,S10]
            S3.append(S2)
            fp=open(InPath+'\\Gossiping'+'.txt','a',encoding='utf-8-sig')
            S7=str(S3[p][:])+"\n"
            fp.write(str(S7))
            p+=1
            p1+=1
            fp.close()
    oLog('抓取完成請按離開鍵結束程式') #反向將設定值顯示在InputPath上
    print("結束")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QWidget()
    w = Ui_Form()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())


