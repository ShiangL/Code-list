import sys
import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_Form(object):
   
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 267)
        self.InputPath = QtWidgets.QTextEdit(Form)
        self.InputPath.setGeometry(QtCore.QRect(40, 40, 211, 31))
        self.InputPath.setObjectName("InputPath")
        self.OutputPath = QtWidgets.QTextEdit(Form)
        self.OutputPath.setGeometry(QtCore.QRect(40, 100, 211, 31))
        self.OutputPath.setObjectName("OutputPath")
        self.FixW = QtWidgets.QTextEdit(Form)
        self.FixW.setGeometry(QtCore.QRect(40, 160, 101, 31))
        self.FixW.setObjectName("FixW")
        self.FixH = QtWidgets.QTextEdit(Form)
        self.FixH.setGeometry(QtCore.QRect(150, 160, 101, 31))
        self.FixH.setObjectName("FixH")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 211, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 211, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 140, 101, 16))
        self.label_4.setObjectName("label_4")
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(40, 210, 101, 31))
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(Form)
        self.btnCancel.setGeometry(QtCore.QRect(150, 210, 101, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.btnOK.clicked.connect(self.btn_OK) #function藥用底線'_'分開
        self.btnCancel.clicked.connect(self.chk_fun)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "批次修正照片尺寸"))
        self.InputPath.setPlaceholderText(_translate("Form", "EX: C:\\Input"))
        self.OutputPath.setPlaceholderText(_translate("Form", "EX: C:\\Output"))
        self.FixW.setPlaceholderText(_translate("Form", "1024"))
        self.FixH.setPlaceholderText(_translate("Form", "768"))
        self.label.setText(_translate("Form", "請輸入圖片路徑"))
        self.label_2.setText(_translate("Form", "請輸入存檔路徑"))
        self.label_3.setText(_translate("Form", "修正後尺寸(寬)"))
        self.label_4.setText(_translate("Form", "修正後尺寸(高)"))
        self.btnOK.setText(_translate("Form", "OK"))
        self.btnCancel.setText(_translate("Form", "Exit"))   
    
    def btn_OK(self):
        iPath=self.InputPath.toPlainText() #讀入InputPath 輸入值
        oPath=self.OutputPath.toPlainText() #讀入InputPath 輸入值
        wResize=int(self.FixW.toPlainText()) #讀入InputPath 輸入值
        hResize=int(self.FixH.toPlainText()) #讀入InputPath 輸入值
        # self.InputPath.setPlainText('Hello PyQt5!\n单击按钮') #反向將設定值顯示在InputPath上
        Tan_fun(iPath,oPath,wResize,hResize)
        
    def chk_fun(self):
        print("Bye.")
        sys.exit()
        
def Tan_fun(iPath,oPath,wResize,hResize):

    k=os.listdir(iPath)
    out=os.listdir(oPath)
    iPath=iPath+"\\"
    oPath=oPath+"\\"
    for i in range (len(k)):
        im = cv2.imdecode(np.fromfile(iPath+str(k[i]), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        res_img=cv2.resize(im, (wResize,hResize),interpolation=cv2.INTER_CUBIC)
        oPath1=oPath+"resize"+str(k[i])
        cv2.imwrite(oPath1, res_img)
    print("批次縮圖完成")
    sys.exit()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QWidget()
    w = Ui_Form()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
