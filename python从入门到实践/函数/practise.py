def show_magicians(magicians):
    """打印每个魔术师的名字"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """在每个名字之前加'the Great'"""
    great_magicians = []
    for magician in magicians:
        great_magician = "the Great " + magician
        great_magicians.append(great_magician)
    return great_magicians


magicians = ['asd', 'asda', 'dwq']
show_magicians(magicians)
print("\n")
show_magicians(make_great(magicians))
print(magicians)
