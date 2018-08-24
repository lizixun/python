bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())  # 访问第一个元素
print(bicycles[-1])  # 访问最后一个元素
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
bicycles.append('motorcycles')                                    #  insert:插入元素（插入位置和值） append：在末尾插入元素（值）
print(bicycles)                                                         #  del:删除元素，不能再访问（根据索引）
bicycles.insert(2, 'danche')                                            #  pop:删除元素，能后接着使用（根据索引）
print(bicycles)                                                         #  remove：删除元素（根据值）
del bicycles[2]
print(bicycles)
popped_bicycles = bicycles.pop(1)  # 弹出第二个元素
print(bicycles)
print(popped_bicycles)
too_expensive = 'motorcycles'
bicycles.remove(too_expensive)
print(bicycles)
print("A. " + too_expensive.title() + " is too expensive for me. ")
removed_bicycles = bicycles.remove('trek')
print(removed_bicycles)
