from wechat_lib import WeChatBot
from qwen_model import QwenModel
import time

def main():
    # 初始化组件
    wx_bot = WeChatBot()
    model = QwenModel()
    
    # 添加监听对象（示例）
    wx_bot.add_listen_chat("陈雨微")
    # wx_bot.add_listen_chat("庄旭晖")
    
    print("微信智能助手已启动...")
    
    while True:
        try:
            # 获取新消息
            messages = wx_bot.listen_messages()
            
            # 处理每条消息
            for msg in messages:
                print(f"收到来自 {msg['user']} 的消息: {msg['content']}")
                
                # 生成回复
                reply = model.generate(msg['content'])
                print(f"生成回复: {reply}")
                
                # 发送回复
                wx_bot.send_reply(msg['chat_win'], reply)
            
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\n程序已终止")
            break
        except Exception as e:
            print(f"运行时错误: {str(e)}")
            time.sleep(5)

if __name__ == "__main__":
    main()