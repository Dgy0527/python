import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-314c1475d4594fd7802a02c9b49c2a5c",  # 注意这里必须有个英文逗号隔开
    base_url="https://api.deepseek.com"      # 这是最后一行，不需要逗号
)

# 放在 client 初始化代码之后
print("=== DeepSeek 聊天机器人 (输入 'quit' 退出) ===")

while True:
    user_input = input("\n你: ")
    if user_input.lower() == 'quit':
        break
        
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[{"role": "user", "content": user_input}],
        stream=False
    )
    print("AI:", response.choices[0].message.content)