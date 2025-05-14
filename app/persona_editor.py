import streamlit as st

if "persona" not in st.session_state:
    st.session_state.persona = None

if not st.session_state.persona:
    st.switch_page("persona_setup.py")

text = st.session_state.persona
new_text = st.text_area("現在のペルソナ", value=text, height=300)

if st.button("保存"):
    st.session_state.persona = new_text
    st.session_state.name = new_text.split('\n')[0].split('：')[1]
    st.success("ペルソナが保存されました！")
