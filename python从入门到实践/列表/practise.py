guests = ['小俊', '小李', '小鹏']
print(guests[0] + ",今晚请和我共进晚餐。")
print(guests[1] + ",今晚请和我共进晚餐。")
print(guests[2] + ",今晚请和我共进晚餐。")
print("对不起，" + guests[2] + "无法赴约。")
print("小鹏无法赴约，让我们邀请小飞吧！")
guests[2] = "小飞"
print(guests[0] + ",今晚请和我共进晚餐。")
print(guests[1] + ",今晚请和我共进晚餐。")
print(guests[2] + ",今晚请和我共进晚餐。")
print("我们找到一张大桌子，把小鹏拖出来吧！")
guests.append("小鹏")
print(guests[0] + ",今晚请和我共进晚餐。")
print(guests[1] + ",今晚请和我共进晚餐。")
print(guests[2] + ",今晚请和我共进晚餐。")
print(guests[3] + ",今晚请和我共进晚餐。")
print("对不起，由于餐桌被小鹏吃了，只能邀请两个人和我共进晚餐了")
name=guests.pop(3)
print("对不起，"+name+",你太胖了。")
name=guests.pop(2)
print("对不起，"+name+",你太矮了。")
print(guests[0] + ",今晚请和我共进晚餐。")
print(guests[1] + ",今晚请和我共进晚餐。")
print("邀请了"+str(len(guests))+"个人。")