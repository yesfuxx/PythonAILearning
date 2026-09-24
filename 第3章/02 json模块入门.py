import json

# 写入json数据文件
user = {
    "name": "帅哥",
    "age": 18,
    "gender": "男",
    "hobby": ["篮球", "足球", "游泳", "watch TV"]
}

with open("resources/user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=4)

# 读取json数据文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)
    print(user_data)
    print(type(user_data))
    print(user_data["name"])
