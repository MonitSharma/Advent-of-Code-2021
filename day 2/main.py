

with open('day 2\input.txt','r') as f:
    lines = f.readlines()
    commands = [entry.strip() for entry in lines]



horizontal_pos, depth = 0,0 
for command in commands:
    direction, amount = command.split(' ')[0], int(command.split(" ")[1])
    if 'forward' in direction:
        horizontal_pos += amount
    elif 'up' in direction:
        depth -= amount
    elif 'down' in direction:
        depth += amount


print(depth* horizontal_pos)



horizontal_pos, depth , aim = 0,0,0

for command in commands:
    direction, amount = command.split(' ')[0], int(command.split(' ')[1])
    if 'forward' in direction:
        horizontal_pos += amount
        depth += aim * amount
    elif 'up' in direction:
        aim -= amount
    elif 'down' in direction:
        aim += amount


print("Part 2 Solution", depth* horizontal_pos)