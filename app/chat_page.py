import streamlit as st
import litellm
import random



litellm.model_alias_map = {"chat": "anthropic/claude-3-opus-20240229"}
litellm.api_key = st.secrets["ANTHROPIC_API_KEY"]

if "persona" not in st.session_state:
    st.session_state.persona = None

if st.session_state.persona:
    
    if st.session_state.avatar_base64:
        avatar = f"data:{st.session_state.avatar_media_type};base64,{st.session_state.avatar_base64}"
    else:
        avatar = None # setting avatar for chatbot
    col1, col2 = st.columns([3, 5])
    with col1:
        st.image(avatar)
    with col2:
        st.markdown(f'## {st.session_state.name}')
        personality = st.session_state.persona.split('\n')[2]
        st.write(personality)
    st.markdown("### チャット")
    system_prompt = f"あなたは犬「{st.session_state.name}」です。以下のペルソナに従って、犬になりきって日本語で返答してください。語尾に犬っぽい特徴を出してもOKです。できるだけリアルな犬を演じてください。あとなるべく質問で会話を終わってください。\n{st.session_state.persona}"

    if not st.session_state.chat_history:
        intros = [
            f'わんわんっ！あなたのバーチャルわんこ、{st.session_state.name}だよ！なんでも聞いてワン！',
            f'ご主人さま、{st.session_state.name}はいつでもそばにいるワン！お手伝いできることがあれば、何でも言ってねっ！'
        ]
        reply = random.choices(intros, k=1)[0]
        # reply = f'ご主人さま、{st.session_state.name}はいつでもそばにいるワン！お手伝いできることがあれば、何でも言ってねっ！' 
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"],avatar=avatar if chat["role"] == "assistant" else None):
            st.markdown(chat["content"])

    if prompt := st.chat_input("犬に話しかけてみよう！"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

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
else:
    st.switch_page("persona_setup.py")
