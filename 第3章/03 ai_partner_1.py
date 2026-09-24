import streamlit as st
import aiutilities

st.set_page_config(
    page_title="AI智能伴侣", 
    page_icon="😃",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

system_prompt = "你是可爱的AI助理，你的名字叫小甜甜。"

st.title("AI智能伴侣")

st.logo("resources/trump.jpg")

if "messages" not in st.session_state:
    st.session_state.messages = []
else:
    for message in st.session_state.messages:
       st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("请输入您的问题或需求：")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    plain_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    response = aiutilities.unified_chat_test(plain_messages)
    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

