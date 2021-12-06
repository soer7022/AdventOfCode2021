lines = []
with open('input.txt') as f:
    for line in f.readlines():
        p1, p2 = line.split('->')
        p1 = p1.split(",")
        p2 = p2.split(",")
        x1 = int(p1[0])
        y1 = int(p1[1])
        x2 = int(p2[0])
        y2 = int(p2[1])
        lines.append((x1, y1, x2, y2))

coordinates = {}
straight_lines = []
for point in lines:
    if point[0] == point[2] or point[1] == point[3]:
        straight_lines.append(point)

for line in straight_lines:
    dist_x = abs(line[0] - line[2])
    dist_y = abs(line[1] - line[3])
    if dist_x == 0:
        for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
            try:
                coordinates[(line[0], y)] += 1
            except KeyError:
                coordinates[(line[0], y)] = 1
    elif dist_y == 0:
        for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
            try:
                coordinates[(x, line[1])] += 1
            except KeyError:
                coordinates[(x, line[1])] = 1
total = 0
for key in coordinates:
    if coordinates[key] > 1:
        total += 1
print(total)