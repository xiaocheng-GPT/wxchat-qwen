import requests
import json

class QwenModel:
    def __init__(self, base_url="http://localhost:11434"):
        self.api_url = f"{base_url}/api/chat"
        
    def generate(self, prompt):
        """生成回复"""
        try:
            response = requests.post(
                url=self.api_url,
                json={
                    "model": "qwen-2:latest",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False
                },
                timeout=60
            )
            return response.json()["message"]["content"]
        except Exception as e:
            print(f"模型调用失败: {str(e)}")
            return "当前无法处理您的请求，请稍后再试"