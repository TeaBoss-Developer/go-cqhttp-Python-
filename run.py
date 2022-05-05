import Config
Address=Config.Address
Port=Config.Port
Path=Config.Path
Ports=Config.Ports
Types=Config.Types
import socket
import json
import datetime
import os
import random
import requests
se = requests.session()
#HttpServer
def InitSocket(address,port):
    Other_time("绑定地址");
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        sock.bind((address,port));
        sock.listen(5);
        print("   成功以IP地址：{}访问网络".format(address));
    except:
        print("   Ip wrong");
    return sock;

def StartListening(sock,address,port):
    Other_time("开启服务器");
    while(1):
        clientdata,clientaddress=sock.accept();
        Other_time("收到一个请求");
        buf=clientdata.recv(1024);
        recvdata=buf.decode('utf-8','ignore');
        f = buf.decode('utf-8','ignore').split("\r\n\r\n")
        g = f[1].split("\n'")
        content='HTTP/1.1 200 ok\r\nContent-Type: application/json\r\n\r\n{"status":"100"}';
        clientdata.sendall(content.encode('utf-8','ignore'));
        clientdata.close();
        txx = open("code.txt",'r')
        txt = txx.read()
        syt = txt.split("\n")
        txx.close()
        if True:
            if "\"message_type\":\"group" in buf.decode('utf-8','ignore'):
                qhz = g[0].split("\"group_id\":")
                qhy = qhz[1].split(",\"message\"")
                SQz = g[0].split("\"user_id\":")
                sq = SQz[1].split("},\"sub")
                idz = g[0].split("message_id\":")
                _id = idz[1].split(",\"message")
                sfz = g[0].split("\"self_id\":")
                sf = sfz[1].split(",\"sender\"")
                nr = g[0].split("\"message\":\"")
                nrz = nr[1].split("\",\"message_id\":")
                print("收到群聊消息\n"+"群号:"+qhy[0]+"\n发送人QQ号:"+sq[0]+"\n消息内容:"+nrz[0]+"\n框架QQ:"+sf[0]+"\n消息ID:"+_id[0])
                for myg in syt:
                    info = myg.split(" ")
                    if(info[1] == "精确"):
                        if(info[0] == nrz[0]):
                            if("tcq:img" in myg):
                                img = info[2].split("info=")
                                imgu = img[1].split("]")
                                Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message=[CQ:image,file="+imgu[0]+",id=40000]"
                                Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                                print(Text)
                            if("tcq:img" not in myg):
                                Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message="+info[2]
                                Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                                print(Text)
                    if(info[1] == "模糊"):
                        if(info[0] in nrz[0]):
                            Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message="+info[2]
                            Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                            print(Text)
                if("Hello" in nrz[0]):
                    Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message=World"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
            if "\"message_type\":\"private" in buf.decode('utf-8','ignore'):
                SQz = g[0].split("\"user_id\":")
                sq = SQz[1].split("},\"sub")
                idz = g[0].split("message_id\":")
                _id = idz[1].split(",\"message")
                sfz = g[0].split("\"self_id\":")
                sf = sfz[1].split(",\"sender\"")
                nr = g[0].split("\"message\":\"")
                nrz = nr[1].split("\",\"message_id\":")
                print("收到私聊消息\n"+"发送人QQ号:"+sq[0]+"\n消息内容:"+nrz[0]+"\n框架QQ:"+sf[0]+"\n消息ID:"+_id[0])
                if("Hello" in nrz[0]):
                    Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+sq[0]+"&message=World[CQ:face,id=4]"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if("图片" in nrz[0]):
                    Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+sq[0]+"&message=[CQ:image,file=http://49.232.165.213:8119/www.jpg,type=show,id=40000]"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if("链接" in nrz[0]):
                    Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+sq[0]+"&message=[CQ:share,url=http://baidu.com,title=百度]"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if("文字转语音" in nrz[0]):
                    Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+sq[0]+"&message=[CQ:tts,text=这是一条测试消息]"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if("卡片" in nrz[0]):
                    file = open("卡片.txt",'r')
                    a = file.read()
                    Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+sq[0]+"&message=[CQ:xml,data="+a+"]"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if("logo" in nrz[0]):
                    Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+sq[0]+"&message=[CQ:image,file=logo.jpg,id=40000]"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
            if("\"notice_type\":\"group_recall\"" in g[0]):
                qhz = g[0].split("\"group_id\":")
                qhy = qhz[1].split(",\"message_id\":")
                SQz = g[0].split("\"user_id\":")
                sq = SQz[1].split("}")
                xxz = g[0].split("\"message_id\":")
                xxm = xxz[1].split(",\"notice_type\"")
                print("收到消息撤回事件\n群号为:"+qhy[0]+"\n发送人QQ:"+sq[0]+"\n消息ID为(用来查询消息内容):"+xxm[0])
            if("group_ban" in g[0]):
                qhz = g[0].split("\"group_id\":")
                qhy = qhz[1].split(",\"notice_type\"")
                sjz = g[0].split("\"duration\":")
                sjy = sjz[1].split(",\"group_id")
                czz = g[0].split("\"operator_id\":")
                czy = czz[1].split(",\"post_type")
                bez = g[0].split("\"user_id\":")
                bey = bez[1].split("}")
                if(sjy[0] != "0"):
                    print("收到禁言事件\n群号为:"+qhy[0]+"\n管理QQ:"+czy[0]+"\n封禁时间:"+sjy[0]+"\n被禁言者QQ:"+bey[0])
                    Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message="+bey[0]+"被"+czy[0]+"塞口球了。时间是:"+sjy[0]+"秒"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if(sjy[0] == "0"):
                    print("收到解禁言事件\n群号为:"+qhy[0]+"\n管理QQ:"+czy[0]+"\n解开禁言者QQ:"+bey[0])
                    Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message="+bey[0]+"被解开口球了。"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
            if("group_admin" in g[0]):
                qhz = g[0].split("\"group_id\":")
                qhy = qhz[1].split(",\"notice_type\"")
                setz = g[0].split("\"sub_type\":\"")
                sety = qhz[1].split("\",\"time\"")
                bez = g[0].split("\"user_id\":")
                bey = bez[1].split("}")
                if(sety[0] == "set"):
                    print("收到设置管理事件\n群号:"+qhy[0]+"被设置人员:"+bey[0])
                if(sety[0] == "unset"):
                    print("收到收回管理事件\n群号:"+qhy[0]+"被设置人员:"+bey[0])
            if("\"message_type\":\"private" not in buf.decode('utf-8','ignore') and "\"message_type\":\"group" not in buf.decode('utf-8','ignore')and "\"notice_type\":\"group_recall\"" not in g[0] and "group_ban" not in g[0]):
                print("未知事件JSON为:"+g[0])
        else:
             print("遇到错误源JSON为:"+g[0])
            
def CloseListening(sock):
    sock.close();
    
#CmdSolve


def Other_time(behavior):
    global Address;
    global Port;
    print(str(datetime.datetime.now()).split('.')[0]+" TeaBoss机器人处理后端——————["+behavior+"]");

#Main

def main():
    global Address;
    global Port;
    address=Address;
    port=Port
    
    sock=InitSocket(address,port);

    StartListening(sock,address,port);
    CloseListening(sock);
    return 0;

main();
