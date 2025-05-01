import streamlit as st
from utils import load_persona, save_persona

if "persona" not in st.session_state:
    st.session_state.persona = None

if not st.session_state.persona:
    st.info('ペルソナを作成してください', icon="ℹ️")
    st.switch_page("persona_setup.py")

text = load_persona()
new_text = st.text_area("現在のペルソナ", value=text, height=300)

if st.button("保存"):
    save_persona(new_text)
    st.success("ペルソナが保存されました！")
