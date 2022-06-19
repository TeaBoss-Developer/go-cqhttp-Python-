import socket
from datetime import datetime
from SDK import Texts,Api,Group_Admin,Group_ban,Group_msg,Group_Recall,Private_msg
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
                Gm = Group_msg(g[0])
                print("收到群聊消息\n"+"群号:"+Gm.group_id+"\n发送人QQ号:"+Gm.sender+"\n消息内容:"+Gm.msg+"\n框架QQ:"+Gm.self_id+"\n消息ID:"+Gm.msg_id)
                for myg in syt:
                    info = myg.split(" ")
                    if(info[1] == "精确"):
                        if(info[0] == Gm.msg):
                            if("tcq:img" in myg):
                                img = info[2].split("info=")
                                imgu = img[1].split("]")
                                Api.send_group_msg(Gm.group_id,Texts.image(imgu[0]))
                            if("tcq:img" not in myg):
                                Api.send_private_msg(Gm.group_id,info[2])
                    if(info[1] == "模糊"):
                        if(info[0] in Gm.msg):
                            Api.send_group_msg(Gm.group_id,info[2])
                if("CQ:image" in Gm.msg and "type=flash" in Gm.msg):
                    Api.send_private_msg("3302347619",Gm.group_id+"里"+Gm.sender+"发的闪照破解完啦"+Group_msg.msg.replace("flash",""))
                    Api.send_private_msg("2220067959",Gm.group_id+"里"+Gm.sender+"发的闪照破解完啦"+Group_msg.msg.replace("flash",""))
            if "\"message_type\":\"private" in buf.decode('utf-8','ignore'):#监听私聊消息
                Pm = Private_msg(g[0])
                print("收到私聊消息\n"+"发送人QQ号:"+Pm.sender+"\n消息内容:"+Pm.msg+"\n框架QQ:"+Pm.self_id+"\n消息ID:"+Pm.msg_id)
                if("新建词汇" in Pm.msg):
                    lists = Pm.msg.split(" ")#[1]模式(精确/模糊)[2]关键词[3]返回内容
                    readcode = open("code.txt",'r')
                    text = readcode.read()
                    readcode.close()
                    buf1 = text + "\n" + lists[2]+" "+lists[1]+" "+lists[3]
                    save=open("code.txt",'w')
                    save.write(buf1)
                    save.close()
                    Api.send_private_msg(Pm.sender,Texts.face("30")+"添加词汇成功,请尝试触发.")
                    
            if("\"notice_type\":\"group_recall\"" in g[0]):#监听撤回消息
                GR = Group_Recall(g[0])
                print("收到消息撤回事件\n群号为:"+GR.group_id+"\n发送人QQ:"+GR.sender+"\n消息ID为(用来查询消息内容):"+GR.msg_id)
            if("group_ban" in g[0]):#监听禁言消息
                GB = Group_ban(g[0])
                if(GB.time != "0"):
                    print("收到禁言事件\n群号为:"+GB.group_id+"\n管理QQ:"+GB.operator_id+"\n封禁时间:"+GB.time+"\n被禁言者QQ:"+GB.user_id)
                    Api.send_group_msg(GB.group_id,GB.user_id+"被"+GB.operator_id+"禁言了。时间是:"+GB.timeddd+"秒")
                if(GB.time == "0"):
                    print("收到解禁言事件\n群号为:"+GB.group_id+"\n管理QQ:"+GB.operator_id+"\n解开禁言者QQ:"+GB.user_id)
                    Api.send_group_msg(GB.group_id,GB.user_id+"被"+GB.operator_id+"解开禁言了。")
            if("group_admin" in g[0]):#监听设置管理员事件
                GA = Group_Admin(g[0])
                if(GA.sub_type == "set"):
                    print("收到设置管理事件\n群号:"+GA.group_id+"被设置人员:"+GA.user_id)
                if(GA.sub_type == "unset"):
                    print("收到收回管理事件\n群号:"+GA.group_id+"被设置人员:"+GA.user_id)
            if("\"message_type\":\"private" not in buf.decode('utf-8','ignore') and "\"message_type\":\"group" not in buf.decode('utf-8','ignore')and "\"notice_type\":\"group_recall\"" not in g[0] and "group_ban" not in g[0]):
                print("未知事件JSON为:"+g[0])
        except:
             print("遇到错误源JSON为:"+g[0])


def Other_time(behavior):#进行监听事件报告
    print(str(datetime.datetime.now()).split('.')[0]+" 机器人处理后端——————["+behavior+"]");
