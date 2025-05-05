import streamlit as st
from utils import generate_persona, image_to_base64

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "persona" not in st.session_state:
    st.session_state.persona = None

if "avatar_base64" not in st.session_state:
    st.session_state.avatar_base64 = None

with st.container():
    name = st.text_input("犬の名前を入力してください")
    image_file = st.file_uploader("犬の画像をアップロードしてください", type=["jpg", "jpeg", "png"])
    if image_file:
        filename = image_file.name
        media_type = f"image/{'png' if filename.split('.')[1] == 'png' else 'jpeg'}"
        st.write(media_type)
    if st.button("ペルソナ生成", type='primary') and name and image_file:
        image_base64 = image_to_base64(image_file)
        with st.spinner("ペルソナを生成中..."):
            persona = generate_persona(image_base64, media_type, name)
            st.session_state.persona = persona
            st.session_state.name = name
            st.session_state.avatar_base64 = image_base64
            st.session_state.avatar_media_type = media_type
            st.success("ペルソナ生成完了！")
            st.switch_page("chat_page.py")