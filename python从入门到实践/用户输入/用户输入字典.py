responses={}
polling_active = True
while polling_active:
    name = input("\nPlease enter your name: ")
    response = input("where do you want to go today? ")
    responses[name] = response
    repeat =input("Is there another person responding?(yes or no) ")
    if repeat=='no':
        polling_active=False
for name,response in responses.items():
    print(name+" would like to go  "+response+".")
