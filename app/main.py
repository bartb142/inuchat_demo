import streamlit as st

st.set_page_config(
        page_title='PawTeQ',
        layout='centered',
        initial_sidebar_state='collapsed',
        page_icon="🐶"

    )

# Page setup 
page1 = st.Page(
    page='persona_setup.py',
    title='ワンちゃん情報設定',
    default=True,
)

page2 = st.Page(
    page='chat_page.py',
    title='チャット',
    url_path='chat'
)

page3 = st.Page(
    page='persona_editor.py',
    title='ペルソナ設定',
    icon=':material/settings:',
    url_path='persona-edit'
)

# Nav setup
pg = st.navigation(pages=[page1,page2,page3])
pg .run()
