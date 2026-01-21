import random
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def generate_gentle_message():
    moods = [
        "温柔安慰",
        "轻微鼓励",
        "平静陪伴",
        "积极但不过分热情",
        "像朋友一样的关心"
    ]

    openings = [
        "你好呀，",
        "想和你说一句，",
        "不知道你现在过得怎么样，",
        "今天想轻轻问候你，",
        "在忙碌的生活里，"
    ]

    closings = [
        "希望这些话能给你一点温暖。",
        "愿你今天过得还算轻松。",
        "不急着回应，也不用有压力。",
        "照顾好自己，我们慢慢来。",
        "祝你有一个安静而顺利的一天。"
    ]

    mood = random.choice(moods)
    opening = random.choice(openings)
    closing = random.choice(closings)

    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
你是一位善于用文字安慰人的朋友。
今天是 {today}。

请写一小段中文文字，风格是：{mood}。
要求：
- 语气自然，不像营销文案
- 不说教，不鸡汤
- 不超过 120 字
- 像真正的人写给朋友的

开头参考（可以变化）：{opening}
结尾参考（可以变化）：{closing}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()

