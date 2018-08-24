players=['charles','martina','michael','florance','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[-3:])
for player in players[:3]:
    print(player.title())
players1=players[:]
print(players1)
players2=players
players2.append('ads')
print(players)