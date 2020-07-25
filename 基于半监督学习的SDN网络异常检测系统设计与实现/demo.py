# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jiemian.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from sklearn.datasets import load_iris,load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pandas as pd
import os
import time
import sys
import csv
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit,QApplication, QMessageBox,QLabel, QGridLayout,QTextEdit,QDialog
from PyQt5.QtCore import QCoreApplication

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(677, 346)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 651, 191))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 41, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 250, 61, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 300, 61, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 270, 61, 20))
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(380, 270, 108, 16))
        self.label_9.setObjectName("label_9")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(20, 240, 48, 91))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        self.label_7.setObjectName("label_7")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(300, 10, 401, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "基于机器学习的SDN异常流量检测系统"))
        self.label.setText(_translate("Form", "时间"))
        self.pushButton.setText(_translate("Form", "开始检测"))
        self.lineEdit_4.setText(_translate("Form", "10"))
        self.label_9.setText(_translate("Form", "分析间隔（单位 S）"))
        self.label_6.setText(_translate("Form", "网络状态"))
        self.label_7.setText(_translate("Form", "攻击概率"))
        self.label_2.setText(_translate("Form", "源IP地址"))
        self.label_3.setText(_translate("Form", "源端口号"))
        self.label_4.setText(_translate("Form", "目的端口号"))
        self.label_5.setText(_translate("Form", "OpenFlow协议类型"))
        self.pushButton.clicked.connect(self.starta)

    def rd(self):
        """
        读取数据测试
        :return:
        """
        data = pd.read_csv("ex.csv")
        # print(data.head(10))
        x = data[['frame.time_delta', 'tcp.len', 'tcp.analysis.flags', 'openflow_v4.type', 'openflow_v4.length']]
        y = data[['an']]

        # print(y)
        # #缺失值处理
        # x['ip.src'].fillna(0, inplace=True)
        x['tcp.len'].fillna(0, inplace=True)
        # x['icmp'].fillna(0,inplace=True)
        # x['udp'].fillna(0, inplace=True)
        x['tcp.analysis.flags'].fillna(0, inplace=True)
        # x['tcp.analysis.bytes_in_flight'].fillna(0, inplace=True)
        # x['openflow_v4.action.length'].fillna(0, inplace=True)
        x['openflow_v4.type'].fillna(0, inplace=True)
        x['openflow_v4.length'].fillna(0, inplace=True)
        # x.dropna(inplace=True)

        # #划分测试集
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
        # print(x_train)
        # #特征工程处理
        dict = DictVectorizer(sparse=False)
        x_train = dict.fit_transform(x_train.to_dict(orient="records"))
        # print(dict.get_feature_names())
        x_test = dict.transform(x_test.to_dict(orient="records"))
        # print(x_train)
        # 用决策树预测
        dec = DecisionTreeClassifier()
        dec.fit(x_train, y_train)
        # #得出预测结果
        # y_predict = dec.predict(x_test)
        # print("预测结果为：",y_predict)
        # #预测准确率
        # print("预测成功率为：",dec.score(x_test,y_test))

        # # #测试陌生数据#
        data1 = pd.read_csv("2.csv")
        ## # print(data.head(10))
        x1 = data1[['frame.time_delta', 'tcp.len', 'tcp.analysis.flags', 'openflow_v4.type', 'openflow_v4.length']]
        # y1 = data1[['an']]
        # # # #缺失值处理
        x1['tcp.len'].fillna(0, inplace=True)
        # x1['icmp'].fillna(0, inplace=True)
        # x['udp'].fillna(0, inplace=True)
        x1['tcp.analysis.flags'].fillna(0, inplace=True)
        # x['tcp.analysis.bytes_in_flight'].fillna(0, inplace=True)
        # x['openflow_v4.action.length'].fillna(0, inplace=True)
        x1['openflow_v4.type'].fillna(0, inplace=True)
        x1['openflow_v4.length'].fillna(0, inplace=True)

        # # #x_train1, x_test1, y_train1, y_test1 = train_test_split(x1, y1, test_size=0.25)
        # # # #特征工程处理
        dict1 = DictVectorizer(sparse=False)
        x1 = dict1.fit_transform(x1.to_dict(orient="records"))
        # print(dict1.get_feature_names())
        # #
        # # # 得出预测结果
        dec.fit(x_train, y_train)

        y_predict1 = dec.predict(x1)

        # print("预测结果为：", y_predict1)

        total = 0

        for ele in range(0, len(y_predict1)):
            total = total + y_predict1[ele]
            # # # 预测准确率
        # print("列表元素之和为: ", total)
        print("攻击可能性为: ", total / len(y_predict1))
        self.lineEdit_3.setText(str(total / len(y_predict1)))
        if total / len(y_predict1) >= 0.3:
            print('检测到攻击！')
            self.lineEdit_2.setText('受到攻击！')
        else:
            print('未检测到攻击')
            self.lineEdit_2.setText('网络正常！')

        # print("预测成功率为：", dec.score(x1, y1))

        return None

    def get(self):
        '''
        实时抓包存储
        :return:
        '''
        # sudoPassword = 'root'
        command = 'tshark -i any -c 10 -w 1.pcap'
        command1 = 'chmod 666 1.pcap'
        command2 = 'tshark -r 1.pcap -T fields  -e frame.time  -e ip.src -e tcp.srcport -e tcp.dstport   -e openflow_v4.type  -E header=y -E separator=, -E quote=d -E occurrence=f > test.csv'
        command3 = 'tshark -r 1.pcap -T fields  -e frame.time_delta   -e tcp.len -e icmp   -e tcp.analysis.flags  -e openflow_v4.type -e openflow_v4.length  -E header=y -E separator=, -E quote=d -E occurrence=f > 2.csv'
        # str = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        os.system(command)
        os.system(command1)
        os.system(command2)
        os.system(command3)

        # os.system('D: & cd wireshark64_3987.com\Wireshark\ & tshark.exe -i any -c 10 -w test1.pcap')
        # ＆ tshark -i any -c 10 -w D:\\Py-pycharm\\test1.pcap'
        # os.system("ipconfig")
    def readtest(self):
        print('进入了！')
        with open('test.csv', encoding='utf-8')as f:
            f_csv = csv.reader(f)
            print('进入2')
            for row in f_csv:
                # print(row)
                # if len(row[2])!=0:
                time = re.sub(r'中.*$', "", row[0])
                print("时间：", time, "源地址：", row[1], "源端口：", row[2], "目的端口：", row[3], "消息类型：", row[4])
                str1=str(time+"                        "+row[1]+"                  "+row[2]+"            "+row[3]+"                      "+row[4])
                self.textEdit.append(str1)




    def starta(self,event):
        self.get()
        a = self.lineEdit_4.text()
        time.sleep(int(a))
        self.readtest()
        self.rd()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QDialog()  # 创建主框体（必须），调用了pyqt的QDialog()，见第十一行最后
    ui = Ui_Form()  # 创建对话框Ui_Dialog为类名，实例化类
    ui.setupUi(windows)  # setupUi()为Ui_Dialog的方法
    # windows.setStyleSheet("#MainWindow{border-image:url(E:\study\liaotianxiaochengxu\bj.jpg);}")
    windows.show()  # 显示框体
    sys.exit(app.exec_())