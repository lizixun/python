def city_country(city, country):
    citycountry = city.title() + "," + country.title()
    return citycountry


home = city_country('new', 'china')
print(home)


def make_album(name, songname, num=''):
    album = {'name': name, 'songname': songname}
    if num:
        album['num'] = num
    return album


while True:
    name = input("Enter the name: \n(Enter 'q' to quit.)")
    if name == 'q':
        break
    songname = input("Enter the songname: \n(Enter 'q' to quit.)")
    if songname == 'q':
        break
    one = make_album(name, songname)
    print(one)
