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


def get_diagonal_points(start_x, start_y, end_x, end_y):
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        try:
            coordinates[(i, j)] += 1
        except KeyError:
            coordinates[(i, j)] = 1
    try:
        coordinates[(end_x, end_y)] += 1
    except KeyError:
        coordinates[(end_x, end_y)] = 1


for line in lines:
    dist_x = abs(line[0] - line[2])
    dist_y = abs(line[1] - line[3])
    if dist_x != 0 and dist_y != 0:
        get_diagonal_points(line[0], line[1], line[2], line[3])
    elif dist_x == 0:
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
