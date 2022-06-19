import requests
se = requests.session()

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
        Post_url = "http://127.0.0.1:5700/set_group_special_title?group_id="+group_id+"&user_id="+uesr_id+"&special_title="+special_title
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
        Post_url = "http://127.0.0.1:5700/_set_model_show?model="+modle+"&modle_show="+modle_show
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
class Private_msg:
    sender = ""
    self_id = ""
    msg_id = ""
    msg = ""
    def __init__(self,msg1):
        SQz = msg1.split("\"user_id\":")
        sq = SQz[1].split("},\"sub")
        idz = msg1.split("message_id\":")
        _id = idz[1].split(",\"message")
        sfz = msg1.split("\"self_id\":")
        sf = sfz[1].split(",\"sender\"")
        nr = msg1.split("\"message\":\"")
        nrz = nr[1].split("\",\"message_id\":")
        self.msg = nrz[0]
        self.self_id = sf[0]
        self.sender = sq[0]
        self.msg_id = _id[0]
class Group_Recall:
    group_id = ""
    sender = ""
    msg_id = ""
    def __init__(self,msg1):
        qhz = msg1.split("\"group_id\":")
        qhy = qhz[1].split(",\"message_id\":")
        SQz = msg1.split("\"user_id\":")
        sq = SQz[1].split("}")
        xxz = msg1.split("\"message_id\":")
        xxm = xxz[1].split(",\"notice_type\"")
        self.group_id=qhy[0]
        self.msg_id=xxm[0]
        self.sender=sq[0]
class Group_msg:
    group_id = ""
    self_id = ""
    sender = ""
    msg_id = ""
    msg = ""
    def __init__(self,msg1):
        qhz = msg1.split("\"group_id\":")
        qhy = qhz[1].split(",\"message\"")
        SQz = msg1.split("\"user_id\":")
        sq = SQz[1].split("},\"sub")
        idz = msg1.split("message_id\":")
        _id = idz[1].split(",\"message")
        sfz = msg1.split("\"self_id\":")
        sf = sfz[1].split(",\"sender\"")
        nr = msg1.split("\"message\":\"")
        nrz = nr[1].split("\",\"message_id\":")
        self.group_id = qhy[0]
        self.self_id = sf[0]
        self.sender = sq[0]
        self.msg_id = _id[0]
        self.msg = nrz[0]
class Group_ban:
    group_id = ""
    time = ""
    operator_id = ""
    user_id = ""
    def __init__(self,msg1):
        qhz = msg1.split("\"group_id\":")
        qhy = qhz[1].split(",\"notice_type\"")
        sjz = msg1.split("\"duration\":")
        sjy = sjz[1].split(",\"group_id")
        czz = msg1.split("\"operator_id\":")
        czy = czz[1].split(",\"post_type")
        bez = msg1.split("\"user_id\":")
        bey = bez[1].split("}")
        self.group_id = qhy[0]
        self.operator_id = czy[0]
        self.time = sjy[0]
        self.user_id = bey[0]
class Group_Admin:
    group_id = ""
    sub_type = ""
    user_id = ""
    def __init__(self,msg1):
        qhz = msg1.split("\"group_id\":")
        qhy = qhz[1].split(",\"notice_type\"")
        setz = msg1.split("\"sub_type\":\"")
        sety = setz[1].split("\",\"time\"")
        bez = msg1.split("\"user_id\":")
        bey = bez[1].split("}")
        self.group_id = qhy[0]
        self.sub_type = sety[0]
        self.user_id = bey[0]