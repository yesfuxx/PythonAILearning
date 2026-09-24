# # 读文件

# # 1.打开文件

# f = open("resources/text.txt", "r", encoding="utf-8")

# # 2.读取文件内容

# # content = f.read() #读取所有内容
# # print(content)
# try:
#     content_list = f.readlines() #读取所有内容，返回列表
#     for line in content_list:
#         print(line.strip()) #去掉换行符

# finally:
#     # 3.关闭文件
#     f.close()

# ##################

# # 写文件
# # 1.打开文件

# f = open("resources/output.txt", "w", encoding="utf-8")

# # 2.写入文件内容
# try:
#     f.write("Hello, World! 你好\n")
#     f.write("This is a test file.\n")
#     f.write("Python file operations are easy!\n")

# finally:
#     # 3.关闭文件
#     f.close()




# 写文件
with open("resources/output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World! 你好\n")
    f.write("Hello, World! 你好\n")
    f.write("This is a test file.\n")
    f.write("Python file operations are easy!\n")






