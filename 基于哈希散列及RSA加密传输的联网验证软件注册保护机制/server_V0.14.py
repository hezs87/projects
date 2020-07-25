# -*- coding: utf-8 -*-
import rsa
import socketserver
import socket
import sys
import time
import ast
import threading
import pickle
import pymysql as ps
import hashlib


db=ps.connect(host="localhost",user="root",password="Xbl9527@",database="Registration",charset="utf8")
cur=db.cursor()



def Verif(mac,rc):#预留验证函数，mac为客户端mac地址，rc为客户机注册码
    print ("客服端mac地址:" ,mac)
    print ("客服端注册码:" ,rc)
    sql="select mac,Rcode from codes where mac=%s"
    cur.execute(sql,(mac))
    data=cur.fetchone()
    print(data)
    if(data==None):
        jieguo="验证失败"
        return jieguo
    else:
        dmac=data[0]
        drc=data[1]
        if(dmac==mac and drc==rc):
            jieguo="验证成功"
        else:
            jieguo="验证失败"
        #data = input("验证结果:")
        return jieguo



def sc(string,hash_name='sha1',salt='boywang',iterations=100000,encode_type='utf-8'):#注册码生成函数
    try:
        result = hashlib.pbkdf2_hmac(hash_name,string.encode(encode_type),salt.encode(encode_type),iterations).hex()
    except Exception as e:
        print('[strhash()]:',e,':',hash_name)
        return
    return result

def apply(mac):#申请注册码，mac为客户端mac地址
    print("客服端mac地址:",mac)
    #data = input("新注册码:")
    sql="select mac,Rcode from codes where mac=%s"
    cur.execute(sql,(mac))
    data=cur.fetchone()
    if(data==None):
        Newrc=sc(mac)
        if(Newrc==None):
            Newrc=" "
            appstat="注册失败，请重新注册"

            return Newrc,appstat

        appstat="申请成功"
        #INSERT INTO codes(mac,Rcode)VALUES(%s,%s);
        sql="INSERT INTO codes(mac,Rcode) VALUES (%s, %s)"
             
        try:
            cur.execute(sql,(mac,Newrc))
            db.commit()
        except:
            print("数据库出错")
            db.rollback()
            Newrc=" "
            appstat="注册出错，请重新注册"
    else:
        Newrc=" "
        appstat="您已注册过，请勿重复注册"
    return Newrc,appstat





def encryption(fasong,cPubKey):#加密函数,传参与返回值请处理为字符串类型
    #(PubKey, PrivateKey) = rsa.newkeys(1024)
##    print(PubKey)
##    print(PrivateKey)
    content = fasong.encode('utf8')
    Encrypt_Str = rsa.encrypt(content, cPubKey)
    print(Encrypt_Str)
    return (Encrypt_Str)



def Decrypt(jieshou,pk):#解密函数,传参与返回值请处理为字符串类型
    Decrypt_Str = rsa.decrypt(jieshou,pk)
    Decrypt_Str_1 = Decrypt_Str.decode('utf8')
    return Decrypt_Str_1



##servicesocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##servicesocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

##print("等待连接中")
##servicesocket.bind((host,port))
##print("等待连接中2")
##servicesocket.listen(5)
##print("等待连接中3")
##ClientSock,addr=servicesocket.accept()
##print("等待连接")
##while True:
##    buf = ClientSock.recv(1024)
##    if len(buf):
##        buff=str(buf,'utf-8')
##        print(buf)
##        jiemi=Decrypt(buff)
##        #buff="{'state':1,'mac':'40490f2beddd','rc':'aolidhaosfhcalksfh'}"
##        buff_dict=ast.literal_eval(jiemi)
##        #print(buff_dict,buff_dict["mac"])
##        if (buff_dict['state']==1):#验证
##            data = Verif(buff_dict['mac'],buff_dict['rc'])
##            jieguo="{'验证结果':'"+data+"'}"
##            jiami=encryption(jieguo)
##            ClientSock.sendall(jiami.encode('utf-8'))
##            continue
##        elif (buff_dict['state']==2):
##            print("已接收")
##            Nrc=apply(buff_dict['mac'])
##            jieguo="{'Nrc':'"+Nrc+"'}"
##            jiami=encryption(jieguo)
##            ClientSock.sendall(jiami.encode('utf-8'))
##            continue
##    else:
##        continue
        
LOCALHOST=socket.gethostname()
PORT=9999
class MyServer(socketserver.BaseRequestHandler):
 
    #定义handle方法，函数名只能是handle
    def handle(self):
        ClientSock=self.request
        print("等待1")
        buf=ClientSock.recv(1024)
        self.cPubKey=pickle.loads(buf)
        print(self.cPubKey)

        (self.PubKey, self.PrivateKey) = rsa.newkeys(1024)
        print(self.PubKey)
        print(self.PrivateKey)
        x=pickle.dumps(self.PubKey)


        ClientSock.sendall(x)
        while True:
            buf = ClientSock.recv(1024)
            print("等待2")
            if len(buf):
                #buff=str(buf,'utf-8')
                recvdata = pickle.loads(buf)
                jiemi = Decrypt(recvdata,self.PrivateKey)
                #jiemi=Decrypt(buff)
                print(jiemi)
                print("等待3")
                #buff="{'state':1,'mac':'40490f2beddd','rc':'aolidhaosfhcalksfh'}"
                buff_dict=ast.literal_eval(jiemi)
                #print(buff_dict,buff_dict["mac"])
                if (buff_dict['state']==1):#验证
                    data = Verif(buff_dict['mac'],buff_dict['rc'])
                    jieguo="{'验证结果':'"+data+"'}"
                    #jiami=encryption(jieguo)
                    encryptdata = encryption(jieguo,self.cPubKey)
                    jiami = pickle.dumps(encryptdata)
                    ClientSock.sendall(jiami)
                    continue
                #Nrc(newrc,appstat)   {'Nrc':   ,'appstat':''}
                elif (buff_dict['state']==2):#申请
                    print("已接收")
                    Nrc=apply(buff_dict['mac'])
                    jieguo="{'Nrc':'"+Nrc[0]+"','appstat':'" +Nrc[1]+"'}"
                    #jiami=encryption(jieguo)
                    encryptdata = encryption(jieguo,self.cPubKey)
                    jiami = pickle.dumps(encryptdata)
                    ClientSock.sendall(jiami)
                    #ClientSock.sendall(jiami.encode('utf-8'))
                    continue
            else:
                continue
        






if __name__ == '__main__':
    print("等待5")
    server = socketserver.ForkingTCPServer((LOCALHOST, PORT), MyServer)
    print("等待4")
    server.serve_forever()







