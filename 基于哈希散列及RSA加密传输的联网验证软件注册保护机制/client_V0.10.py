# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientV_0.01.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#state:1为验证，2为申请


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit,QApplication, QMessageBox,QLabel, QGridLayout,QTextEdit,QDialog
from PyQt5.QtCore import QCoreApplication
import socket
import sys
import time
import sys
import threading
import uuid
import ast
import re
import pickle
import rsa


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.settimeout(10)
# 获取本地主机名
#host = socket.gethostname()
host = "49.234.60.164"

# 设置端口号
port = 9999
s.connect((host, port))
(PubKey, PrivateKey) = rsa.newkeys(1024)
x=pickle.dumps(PubKey)
s.send(x)
while True:
    buf = s.recv(1024)
    if len(buf):
        sPubKey = pickle.loads(buf)
        print(sPubKey)
        break



def encryption(fasong):#加密函数,传参与返回值请处理为字符串类型
    #(PubKey, PrivateKey) = rsa.newkeys(1024)
    content = fasong.encode('utf8')
    print(sPubKey)
    Encrypt_Str = rsa.encrypt(content, sPubKey)
    return Encrypt_Str


def Decrypt(jieshou):#解密函数,传参与返回值请处理为字符串类型
    Decrypt_Str = rsa.decrypt(jieshou,PrivateKey)
    Decrypt_Str_1 = Decrypt_Str.decode('utf8')
    return Decrypt_Str_1

def replace_all_blank(value):#字符串处理函数，防止注入
    """
    去除value中的所有非字母内容，包括标点符号、空格、换行、下划线等
    :param value: 需要处理的内容
    :return: 返回处理后的内容
    """
    # \W 表示匹配非数字字母下划线
    result = re.sub('\W+', '', value).replace("_", '')
    print(result)
    return result



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 328)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 431, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 280, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 200, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 120, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.MACtext = QtWidgets.QLineEdit(Dialog)
        self.MACtext.setGeometry(QtCore.QRect(90, 20, 311, 20))
        self.MACtext.setReadOnly(True)
        self.MACtext.setObjectName("MACtext")
        self.RCtext = QtWidgets.QLineEdit(Dialog)
        self.RCtext.setGeometry(QtCore.QRect(90, 70, 311, 20))
        self.RCtext.setReadOnly(True)
        
        self.RCtext.setObjectName("RCtext")
        self.RCstate = QtWidgets.QLineEdit(Dialog)
        self.RCstate.setGeometry(QtCore.QRect(90, 120, 211, 20))
        self.RCstate.setObjectName("RCstate")
        self.Applystate = QtWidgets.QLineEdit(Dialog)
        self.Applystate.setGeometry(QtCore.QRect(90, 230, 311, 20))
        self.Applystate.setObjectName("Applystate")
        self.NewRC = QtWidgets.QLineEdit(Dialog)
        self.NewRC.setGeometry(QtCore.QRect(90, 280, 311, 20))
        self.NewRC.setReadOnly(True)
        self.NewRC.setObjectName("NewRC")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "本机硬件地址："))
        self.label_2.setText(_translate("Dialog", "本机注册码："))
        self.label_3.setText(_translate("Dialog", "注册码状态："))
        self.label_4.setText(_translate("Dialog", "若无注册码，请在此处申请（本操作需要先获取您的硬件地址，以及网络连接）"))
        self.pushButton.setText(_translate("Dialog", "申请注册码"))
        self.label_5.setText(_translate("Dialog", "新注册码："))
        self.label_6.setText(_translate("Dialog", "申请状态："))
        self.pushButton_2.setText(_translate("Dialog", "刷新注册状态"))
        self.pushButton_3.setText(_translate("Dialog", "验证"))
        print("进入button_3")
        self.pushButton_3.clicked.connect(self.theard1)
        self.pushButton.clicked.connect(self.theard2)
        self.pushButton_2.clicked.connect(self.theard3)
        print("进入run")
        self.runol()



        
    def get_mac_address(self): #获取本机mac地址
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
        #print(mac)
        return mac
    
    def get_local_RC(self):#获取本地注册码
        try:
            fi=open("zhucema.txt","r",encoding="utf-8")
            #fi.seek(0)
            a=fi.read()
            if(len(a)==0):
                print("无")
                self.RCtext.setText("无注册码")
                #self.RCstate.clear()
                self.RCstate.setText("无注册码")
            else:
                #print(a)
                b=replace_all_blank(a)
                self.RCtext.setText(b)
                #self.RCstate.clear()
                self.RCstate.setText("未验证")
            #print(a)
            fi.close()
        except:
            self.RCtext.setText("无注册码")
            b=" "
        
        return b


    
    def theard1(self):
        thread_01=threading.Thread(target=self.Verif)#验证子线程
        thread_01.start()


        
    def theard2(self):
        thread_02=threading.Thread(target=self.apply)#申请子线程
        thread_02.start()

        
    def theard3(self):
        thread_03=threading.Thread(target=self.Refresh)#刷新子线程
        thread_03.start()


    def Verif(self):#验证函数
##        #print("进入验证")
##        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##        #s.settimeout(10)
##        # 获取本地主机名
##        host = socket.gethostname()
##        #host = "49.234.60.164"
##
##        # 设置端口号
##        port = 9999

        # 连接服务，指定主机和端口
        #s.connect((host, port))
        #print("等待连接1")
        # 接收小于 1024 字节的数据
        #print("等待连接2")
        data = self.get_mac_address()
        rc1=self.RCtext.text()
        rc=replace_all_blank(rc1)
        #print(rc)
        #print("等待连接3")
        q="{'state':1,'mac':'"+data+"','rc':'"+rc+"'}"
        print(q)

        
##        x=encryption(q)#加密

        encryptdata= encryption(q)
        x = pickle.dumps(encryptdata)
        

        print(x)
        s.send(x)

        
        #s.send(a.encode("utf-8"))
        buf = s.recv(1024)
        if len(buf):
##            buff=str(buf,'utf-8')
##            
##            buff1=Decrypt(buff)#解密

            recvdata = pickle.loads(buf)
            buff1 = Decrypt(recvdata)




            
            print(buff1)
            buff_dict=ast.literal_eval(buff1)
            print(buff_dict)
            self.RCstate.setText(str(buff_dict["验证结果"]))
            #s.close()
            
    def apply(self):#申请函数
##        #print("进入验证")
##        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(10)
##        # 获取本地主机名
##        host = socket.gethostname()
##        #host = "49.234.60.164"
##
##        # 设置端口号
##        port = 9999

##        # 连接服务，指定主机和端口
##        s.connect((host, port))
        print("等待连接1")
        # 接收小于 1024 字节的数据
        print("等待连接2")
        data = self.get_mac_address()
        #rc=self.get_local_RC()
        #print(rc)
        q="{'state':2,'mac':'"+data+"'}"
        #x=encryption(q)#加密
        print("等待连接3")

        encryptdata= encryption(q)
        x = pickle.dumps(encryptdata)
        
        s.send(x)
        print("hahahahah")
        #s.send(a.encode("utf-8"))
        buf = s.recv(1024)

        
        if len(buf):
##            buff=str(buf,'utf-8')
##            print(buff)
##            buff1=Decrypt(buff)#解密
            recvdata = pickle.loads(buf)
            buff1 = Decrypt(recvdata)

            
            buff_dict=ast.literal_eval(buff1)
            print(buff_dict)
            self.NewRC.setText(str(buff_dict["Nrc"]))
            self.Applystate.setText(str(buff_dict["appstat"]))
            #s.close()
        

        

    def Refresh(self):#刷新注册状态
        if(self.NewRC.text()!=" "):
            print(self.NewRC.text())
            self.RCtext.setText(self.NewRC.text())
            self.RCstate.setText("未验证")
            print(self.NewRC.text())
            fi=open("zhucema.txt","w+",encoding="utf-8")
            fi.write(self.NewRC.text())
            fi.close()
        else:
            print("111")
        

    def runol(self):#主流程函数
        print(self.get_mac_address())
        str1=self.get_mac_address()
        str1.encode("utf-8")
        self.MACtext.setText(str1)
        self.get_local_RC()
        #s.connect((host, port))










if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    windows=QDialog()#创建主框体（必须），调用了pyqt的QDialog()，见第十一行最后
    ui = Ui_Dialog()#创建对话框Ui_Dialog为类名，实例化类
    ui.setupUi(windows)#setupUi()为Ui_Dialog的方法
    #windows.setStyleSheet("#MainWindow{border-image:url(E:\study\liaotianxiaochengxu\bj.jpg);}")
    windows.show()#显示框体
    sys.exit(app.exec_())
