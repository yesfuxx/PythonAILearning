import streamlit as st

st.set_page_config(
    page_title="Streamlit 入门示例", 
    page_icon="🔣",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=
    {
        "Get Help": "https://www.baidu.com", 
        "Report a bug": "https://www.baidu.com", 
        "About": "# 这是一个 Streamlit 入门示例应用"
    }
)



# 大标题
st.title("Streamlit 入门示例")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落文字
st.write("天气就像大自然调皮的脸庞，时而温柔明媚，时而活泼热闹，为我们的生活添上了不一样的色彩。观察天气的变化，总能让我收获别样的美好。")
st.write("晴朗的日子里，阳光洒满大地，天空蓝得清澈透亮。微风轻轻拂过脸颊，树叶沙沙作响，鸟儿在枝头欢快歌唱。课间时分，我和同学们在阳光下奔跑嬉戏，温暖的阳光包裹着我们，心里满是轻松与惬意。")
st.write("夏日的雨天格外有趣。乌云悄悄聚拢，细雨淅淅沥沥落下，洗去了夏日的燥热。雨后的空气清新甘甜，树叶青翠欲滴，校园里的花草挂满晶莹的水珠，生机勃勃。偶尔还能看见天边淡淡的彩虹，绚烂又温柔。")
st.write("阴晴雨雪，各有风情。多变的天气装点着平凡的日常，让生活不再单调。我喜欢这变幻万千的天气，也懂得不同风景皆有美好，用心感受，便能发现生活处处藏着温柔与惊喜。")

#图片
st.image("./resources/trump.jpg")
st.image("resources/trump.jpg",width=300, caption="特朗普")

#音频
st.audio("resources/music.mp3", format="audio/mp3")

#视频
st.video("resources/video.mp4", format="video/mp4")

#logo
st.logo("resources/trump.jpg")

#表格
st.table({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 35]
})

student_data={
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 35],
    "性别": ["男", "女", "男"],
    "成绩": [90, 85, 95]
}
st.table(student_data)

#输入框
name = st.text_input("请输入您的姓名：")
st.write(f"您输入的姓名是：{name}")

#输入框
password = st.text_input("请输入您的密码：", type="password")
st.write(f"您输入的密码是：{password}")

#单选按钮
gender = st.radio("请输入你的性别：", ["男", "女","其他"], index = 1)
st.write(f"您选择的性别是：{gender}")