import Config
Address=Config.Address
Port=Config.Port
import socket
import datetime
import os
import random
import requests
import Event
se = requests.session()
#初始化事件接收器
def InitSocket(address,port):
    Other_time("绑定地址");
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        sock.bind((address,port));
        sock.listen(5);
        print("   成功以IP地址：{}访问网络".format(address));
    except:
        print("   IP绑定错误");
    return sock;
def CloseListening(sock):#关闭事件监听器
    sock.close();
def Other_time(behavior):#进行监听事件报告
    global Address;
    global Port;
    print(str(datetime.datetime.now()).split('.')[0]+" 机器人处理后端——————["+behavior+"]");
#开启整套系统
def main():
    global Address;
    global Port;
    address=Address;
    port=Port
    sock=InitSocket(address,port);
    Event.StartListening(sock,address,port);#挂载事件处理器
    CloseListening(sock);
    return 0;
main();
