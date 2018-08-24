current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
pets=['dog','cat','dog','goldfish','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)