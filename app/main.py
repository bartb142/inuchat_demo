import streamlit as st
from utils import generate_persona, save_persona, load_persona, image_to_base64
import litellm




litellm.model_alias_map = {"chat": "anthropic/claude-3-opus-20240229"}
litellm.api_key = st.secrets["ANTHROPIC_API_KEY"]

st.set_page_config(page_title="犬チャットボット", page_icon="🐶")
st.title("🐶 犬チャットボット")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "persona" not in st.session_state:
    st.session_state.persona = None

if "avatar_base64" not in st.session_state:
    st.session_state.avatar_base64 = None

with st.sidebar:
    name = st.text_input("犬の名前を入力してください")
    image_file = st.file_uploader("犬の画像をアップロードしてください", type=["jpg", "jpeg", "png"])
    if image_file:
        filename = image_file.name
        media_type = f"image/{'png' if filename.split('.')[1] == 'png' else 'jpeg'}"
        st.write(media_type)
    if st.button("ペルソナ生成") and name and image_file:
        image_base64 = image_to_base64(image_file)
        with st.spinner("ペルソナを生成中..."):
            persona = generate_persona(image_base64, media_type, name)
            save_persona(persona)
            st.session_state.persona = persona
            st.session_state.name = name
            st.session_state.avatar_base64 = image_base64
            st.session_state.avatar_media_type = media_type
            st.success("ペルソナ生成完了！")

if st.session_state.persona is None:
    try:
        st.session_state.persona = load_persona()
    except FileNotFoundError:
        st.warning("先に画像と名前でペルソナを生成してください。")

if st.session_state.persona:
    st.markdown("### チャット開始")
    avatar = None # setting avatar for chatbot
    if st.session_state.avatar_base64:
        avatar = f"data:{st.session_state.avatar_media_type};base64,{st.session_state.avatar_base64}"

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    if prompt := st.chat_input("犬に話しかけてみよう！"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        system_prompt = f"あなたは犬「{name}」です。以下のペルソナに従って、犬になりきって日本語で返答してください。語尾に犬っぽい特徴を出してもOKです。\n{st.session_state.persona}"

        response = litellm.completion(
            model="chat",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.chat_history,
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant",avatar=avatar):
            st.markdown(reply)
