alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['color'] = 'yellow'
alien_0['speed'] = 'mediun'
print(alien_0)
print("Original x_position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'low':
    x_increment = 1
elif alien_0['speed'] == 'mediun':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_positon: " + str(alien_0['x_position']))
print(alien_0.items())