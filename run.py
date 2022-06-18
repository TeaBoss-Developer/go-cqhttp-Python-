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
#初始化事件接收器
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
#开始监听上报事件
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
        try:
            if "\"message_type\":\"group" in buf.decode('utf-8','ignore'):#监听群消息
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
                if("CQ:image" in nrz[0] and "type=flash" in nrz[0]):
                    Api.send_private_msg("3302347619",qhy[0]+"里"+sq[0]+"发的闪照破解完啦"+nrz[0].replace("flash",""))
                    Api.send_private_msg("2220067959",qhy[0]+"里"+sq[0]+"发的闪照破解完啦"+nrz[0].replace("flash",""))
            if "\"message_type\":\"private" in buf.decode('utf-8','ignore'):#监听私聊消息
                SQz = g[0].split("\"user_id\":")
                sq = SQz[1].split("},\"sub")
                idz = g[0].split("message_id\":")
                _id = idz[1].split(",\"message")
                sfz = g[0].split("\"self_id\":")
                sf = sfz[1].split(",\"sender\"")
                nr = g[0].split("\"message\":\"")
                nrz = nr[1].split("\",\"message_id\":")
                print("收到私聊消息\n"+"发送人QQ号:"+sq[0]+"\n消息内容:"+nrz[0]+"\n框架QQ:"+sf[0]+"\n消息ID:"+_id[0])
                if("新建词汇" in nrz[0]):
                    lists = nrz[0].split(" ")#[1]模式(精确/模糊)[2]关键词[3]返回内容
                    readcode = open("code.txt",'r')
                    text = readcode.read()
                    readcode.close()
                    buf1 = text + "\n" + lists[2]+" "+lists[1]+" "+lists[3]
                    save=open("code.txt",'w')
                    save.write(buf1)
                    save.close()
                    Api.send_private_msg(sq[0],Texts.face("30")+"添加词汇成功,请尝试触发.")
                    
            if("\"notice_type\":\"group_recall\"" in g[0]):#监听撤回消息
                qhz = g[0].split("\"group_id\":")
                qhy = qhz[1].split(",\"message_id\":")
                SQz = g[0].split("\"user_id\":")
                sq = SQz[1].split("}")
                xxz = g[0].split("\"message_id\":")
                xxm = xxz[1].split(",\"notice_type\"")
                print("收到消息撤回事件\n群号为:"+qhy[0]+"\n发送人QQ:"+sq[0]+"\n消息ID为(用来查询消息内容):"+xxm[0])
            if("group_ban" in g[0]):#监听禁言消息
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
                    Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message="+bey[0]+"被"+czy[0]+"禁言了。时间是:"+sjy[0]+"秒"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
                if(sjy[0] == "0"):
                    print("收到解禁言事件\n群号为:"+qhy[0]+"\n管理QQ:"+czy[0]+"\n解开禁言者QQ:"+bey[0])
                    Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+qhy[0]+"&message="+bey[0]+"被解开禁言了。"
                    Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
                    print(Text)
            if("group_admin" in g[0]):#监听设置管理员事件
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
        except:
             print("遇到错误源JSON为:"+g[0])
class Texts:#文本代码类(SA:@at)
    def face(id_):
        return("[CQ:face,id="+id_+"]")
    def record(file_url):
        return("[CQ:record,file="+file_url+"]")
    def at(user_id):
        return("[CQ:at,qq="+user_id+"]")
    def share(url,title):
        return("[CQ:share,url="+url+",title="+title+"]")
    def image(file,_type,url,_id):
        return("[CQ:image,file="+url+",type="+_type+",id="+_id+"]")
    def redbag(title):
        return("[CQ:redbag,title="+title+"]")
    def poke(qq):
        return("[CQ:poke,qq="+qq+"]")
    def xml(data):
        return("[CQ:xml,data="+data+"]")
    def json(data):
        bufo = data.replace(",","&#44;")
        buft = bufo.replace("&","&amp;")
        bufth = buft.replace("[","&#91;")
        buff = bufth.replace("]","&#93")
        return("[CQ:json,data="+buff+"]")
    def tts(text):
        return("[CQ:tts,text="+text+"]")
    def pyrhon(code):
        try:
            return(exec(code))
        except Exception as error:
            a = str(type(error))
            err = a.split("class '")[1].split("'")[0]
            return(err+":"+str(error))
class Api:#API类(SA:好友消息,群消息.)
    def send_private_msg(private_id,msg):
        Post_url = "http://127.0.0.1:5700/send_private_msg?user_id="+private_id+"&message="+msg
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def send_group_msg(group_id,msg):
        Post_url = "http://127.0.0.1:5700/send_group_msg?group_id="+group_id+"&message="+msg
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def delete_msg(msg_id):
        Post_url = "http://127.0.0.1:5700/delete_msg?message_id="+msg_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def group_kick(group_id,user_id,boolean):
        Post_url = "http://127.0.0.1:5700/set_group_kick?group_id="+group_id+"&user_id="+user_id+"&reject_add_request="+boolean
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def group_talk_ban(group_id,user_id,time):
        Post_url = "http://127.0.0.1:5700/set_group_ban?group_id="+group_id+"&user_id="+user_id+"&duration="+time
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def group_whole_talk_ban(group_id,boolean):
        Post_url = "http://127.0.0.1:5700/set_group_whole_ban?group_id="+group_id+"&enable="+boolean
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def set_group_admin(group_id,user_id,boolean):
        Post_url = "http://127.0.0.1:5700/set_group_admin?group_id="+group_id+"&user_id="+user_id+"&enable="+boolean
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def set_group_rank(group_id,user_id,rank):
        Post_url = "http://127.0.0.1:5700/set_group_card?group_id="+group_id+"&user_id="+user_id+"&card="+rank
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def leave_group(group_id,is_dismiss):
        Post_url = "http://127.0.0.1:5700/set_group_leave?group_id="+group_id+"&is_dismiss="+is_dismiss
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def set_group_special_title(group_id,uesr_id,special_title):
        Post_url = "http://127.0.0.1:5700/set_group_special_title?group_id="+group_id+"&user_id="+user_id+"&special_title="+special_title
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def set_friend_add_request():
        print("暂时不支持,建议查看https://docs.go-cqhttp.org/api/#%E5%A4%84%E7%90%86%E5%8A%A0%E5%A5%BD%E5%8F%8B%E8%AF%B7%E6%B1%82")
    def set_group_add_request():
        print("暂时不支持,建议查看https://docs.go-cqhttp.org/api/#%E5%A4%84%E7%90%86%E5%8A%A0%E5%A5%BD%E5%8F%8B%E8%AF%B7%E6%B1%82")
    def get_login_info():
        Post_url = "http://127.0.0.1:5700/get_login_info"
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def get_stranger_info():
        Post_url = "http://127.0.0.1:5700/get_stranger_info"
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def delete_friend(friend_id):
        Post_url = "http://127.0.0.1:5700/delete_friend?friend_id="+friend_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def get_group_info(group_id):
        Post_url = "http://127.0.0.1:5700/get_group_info?group_id="+group_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def get_friend_list():
        Post_url = "http://127.0.0.1:5700/get_friend_list"
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def get_group_list():
        Post_url = "http://127.0.0.1:5700/get_group_list"
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def get_group_member_info(group_id,user_id):
        Post_url = "http://127.0.0.1:5700/get_group_member_info?group_id="+group_id+"&user_id="+user_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def get_group_member_list(group_id):
        Post_url = "http://127.0.0.1:5700/get_group_member_list?group_id="+group_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def restart_robot(delay):
        Post_url = "http://127.0.0.1:5700/set_restart?delay="+delay
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def set_essence_msg(message_id):
        Post_url = "http://127.0.0.1:5700/set_essence_msg?message_id="+message_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def delete_essence_msg(message_id):
        Post_url = "http://127.0.0.1:5700/delete_essence_msg?message_id="+message_id
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def _set_model_show(modle,modle_show):
        Post_url = "http://127.0.0.1:5700/_set_model_show?model="+model+"&modle_show="+modle_show
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print("具体机型在这个链接里查看:https://github.com/Mrs4s/go-cqhttp/pull/872#issuecomment-831180149")
    def _send_group_notice(group_id,content,image_path):
        Post_url = "http://127.0.0.1:5700/_send_group_notice?group_id="+group_id+"&content="+content+"&image="+image_path
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print(Text)
    def upload_group_file():
        print("开发中,请敬请等待.")
    def get_group_system_msg():
        Post_url = "http://127.0.0.1:5700/get_group_system_msg"
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        return(Text)
    def set_group_icon(group_id,file,cache):
        Post_url = "http://127.0.0.1:5700/set_group_portrait?group_id="+group_id+"&file="+file+"&cache="+cache
        Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
        print("具体操作file可以为什么数据请看https://docs.go-cqhttp.org/api/#%E8%AE%BE%E7%BD%AE%E7%BE%A4%E5%A4%B4%E5%83%8F")
    
def CloseListening(sock):#关闭事件监听器
    sock.close();
    
#CmdSolve


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

    StartListening(sock,address,port);
    CloseListening(sock);
    return 0;

main();
