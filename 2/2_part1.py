with open('input.txt') as f:
    data = []
    for line in f.readlines():
        (direction, distance) = line.split(" ")
        data.append((direction, int(distance)))
horizontal = 0
vertical = 0
for (direction, distance) in data:
    if direction == "forward":
        horizontal += distance
    elif direction == "up":
        vertical -= distance
    elif direction == "down":
        vertical += distance

print(vertical*horizontal)
