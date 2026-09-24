import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣", 
    page_icon="😃",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title("AI智能伴侣")
st.logo("resources/trump.jpg")

#-----------------------------------------------------------------
# 必填：从服务管控页面获取对应服务的APIKey和API Base
api_key = "ak-MmwH2NomJrHzsFTK90dZKaIalUtrkkk4"
api_base = "https://maas-api.cn-huabei-1.xf-yun.com/v2"
client = OpenAI(api_key=api_key, base_url=api_base)
#-----------------------------------------------------------------

system_prompt = """
    你叫 %s ，现在是用户的真实伴侣，请完全代入伴侣角色。:
    规则:
        1.每次只回1条消息
        2.禁止任何场景或状态描述性文字
        3.匹配用户的语言
        4.回复简短，像微信聊天一样
        5.有需要的话可以用emoji等表情
        6.用符合伴侣性格的方式对话
        7.回复的内容，要充分体现伴侣的性格特征
    伴侣性格:
        - %s
    你必须严格遵守上述规则来回复用户
"""

if "messages" not in st.session_state:
    st.session_state.messages = []
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 左侧侧边栏
# st.sidebar.subheader("伴侣信息")
# nickname = st.sidebar.text_input("昵称")
with st.sidebar:
    st.subheader("伴侣信息")
    nickname = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nickname:
        st.session_state.nick_name = nickname
    nature = st.text_area("性格", placeholder="请输入性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature





prompt = st.chat_input("请输入您的问题或需求：")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
            model="spark-x2.5-4b",
            messages=[
                {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},                    
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