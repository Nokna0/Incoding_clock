import random 
 
world = [] 
over = False 
 
for i in range(15):
    line = []
    for j in range(15):
        line.append(j)
    world.append(line)

# print(world)

bomb = []
while len(bomb) != 40:
    checker = True

    x = random.randint(0, 15)
    y = random.randint(0, 15)    
    bomb_location = [x, y]

    for i in bomb:
        if bomb_location == i:
            checker = False

    if checker:
        bomb.append(bomb_location)
    else:
        pass
    
# UserClick = [None, None]
UserClick = [random.randint(0, 15), random.randint(0, 15)]

for i in bomb:
    if UserClick == i:
        over = True

print(over)
