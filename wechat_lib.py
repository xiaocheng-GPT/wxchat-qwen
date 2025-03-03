from wxauto import WeChat
import time

class WeChatBot:
    def __init__(self):
        self.wx = WeChat()
        self.listened_chats = set()

    def add_listen_chat(self, who):
        """添加监听对象"""
        self.wx.AddListenChat(who=who)
        self.listened_chats.add(who)

    def listen_messages(self):
        """监听消息并返回消息列表"""
        messages = []
        listen_dict = self.wx.GetListenMessage()
        
        for chat_win, msg_list in listen_dict.items():
            chat_user = chat_win.who
            for msg in msg_list:
                if msg.type == "friend" and chat_user in self.listened_chats:
                    messages.append({
                        "user": chat_user,
                        "content": msg.content,
                        "chat_win": chat_win
                    })
        return messages

    def send_reply(self, chat_win, reply):
        """发送回复"""
        chat_win.SendMsg(reply)