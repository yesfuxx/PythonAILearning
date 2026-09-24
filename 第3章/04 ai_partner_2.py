import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣", 
    page_icon="😃",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#-----------------------------------------------------------------
# 必填：从服务管控页面获取对应服务的APIKey和API Base
api_key = "ak-MmwH2NomJrHzsFTK90dZKaIalUtrkkk4"
api_base = "https://maas-api.cn-huabei-1.xf-yun.com/v2"
client = OpenAI(api_key=api_key, base_url=api_base)
#-----------------------------------------------------------------

system_prompt = "你是可爱的AI助理，你的名字叫小甜甜。"

st.title("AI智能伴侣")

st.logo("resources/trump.jpg")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])


prompt = st.chat_input("请输入您的问题或需求：")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
            model="spark-x2.5-4b",
            messages=[
                {"role": "system", "content": system_prompt},                    
                *st.session_state.messages
            ],
            stream=True                          
    )
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    response_message = st.empty()

    full_response = ""

    for chunk in response:
        if not chunk.choices:
            continue
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
  
    st.session_state.messages.append({"role": "assistant", "content": full_response})