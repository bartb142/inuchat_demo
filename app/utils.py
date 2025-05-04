import streamlit as st
import base64
import anthropic
from PIL import Image
import io

ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def image_to_base64(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")

def generate_persona(image_base64: str, media_type: str, name: str) -> str:
    prompt = f"""
    この画像に写っている犬について以下のフォーマットに従って日本語でペルソナを作成してください。
    名前は「{name}」です。

    フォーマット：
    名前：<名前>
    犬種：<犬種（わからなければ"不明"）>
    性格：<3つ程度の性格特徴>
    背景：<一文の背景ストーリー>
    好きなこと：<3つ程度の好み>
    """

    msg = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=500,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": image_base64}}
                ]
            }
        ]
    )
    return msg.content[0].text.strip()
