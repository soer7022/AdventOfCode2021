with open("input.txt") as f:
    data = []
    for line in f.readlines():
        (direction, distance) = line.split(" ")
        data.append((direction, int(distance)))
horizontal = 0
vertical = 0
aim = 0
for (direction, distance) in data:
    if direction == "forward":
        horizontal += distance
        vertical += distance * aim
    elif direction == "up":
        aim -= distance
    elif direction == "down":
        aim += distance

print(vertical * horizontal)
