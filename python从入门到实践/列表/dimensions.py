dimensions = (200, 50)
print(dimensions[0])
dimensions = (250, 0)

users = ['谢', '刘', '廖', '李']
if users:
    print(users)
else:
    print("无用户！")
for user in users:
    if user == '李':
        print(user + "主人，您好！")
    else:
        print(user + "奴隶,你好!")
new_users = ['李', 'a']
for user in new_users:
    if user in users:
        print("用户名" + user + "已被使用")
    else:
        print("用户名" + user + "未被使用")
