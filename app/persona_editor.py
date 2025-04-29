import streamlit as st
from utils import load_persona, save_persona

text = load_persona()
new_text = st.text_area("現在のペルソナ", value=text, height=300)

if st.button("保存"):
    save_persona(new_text)
    st.success("ペルソナが保存されました！")
# TODO: this page is not functioning yet still work in progress but I might delete it since it's a demo app