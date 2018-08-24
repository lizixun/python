#字典列表
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))


#在字典中储存列表
pizza={'crust':'thick',
       'toppings':['mushrooms','extra cheese'],
       }
print("You ordered a "+pizza['crust']+"-crust pizza"+" with the toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

#在字典中储存字典
users={
    'lizixun':{
        'first_name':'li',
        'last_name':'zixun',
        'location':'灶市',
    },
    'xiefei':{
        'first_name':'xie',
        'last_name':'fei',
        'location':'西湖游园',
    },
}
for name,information in users.items():
    print("\nusername:"+name)
    fullname=information['first_name']+information['last_name']
    location=information['location']
    print("\tfullname: "+fullname.title())
    print("\tlocation: "+location.title())