with open('input.txt') as f:
    data = [[int(n) for n in f.strip()] for f in f.readlines()]

low_points = []
total = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        curr = data[i][j]
        above = 99 if i - 1 < 0 else data[i - 1][j]
        below = 99 if i + 1 >= len(data) else data[i + 1][j]
        left = 99 if j - 1 < 0 else data[i][j - 1]
        right = 99 if j + 1 >= len(data[0]) else data[i][j + 1]

        if curr < min(above, below, left, right):
            low_points.append((i, j))
            total += (curr + 1)



def find_basin(point):
    points_to_check = [point]
    checked = set()
    while len(points_to_check) > 0:
        (i, j) = points_to_check.pop(0)
        checked.add((i, j))
        above = 99 if i - 1 < 0 else data[i - 1][j]
        below = 99 if i + 1 >= len(data) else data[i + 1][j]
        left = 99 if j - 1 < 0 else data[i][j - 1]
        right = 99 if j + 1 >= len(data[0]) else data[i][j + 1]
        if above < 9 and (i - 1, j) not in checked:
            points_to_check.append((i - 1, j))
        if below < 9 and (i + 1, j) not in checked:
            points_to_check.append((i + 1, j))
        if left < 9 and (i, j - 1) not in checked:
            points_to_check.append((i, j - 1))
        if right < 9 and (i, j + 1) not in checked:
            points_to_check.append((i, j + 1))

    return checked


basins = set()
basin_sizes = []
for point in low_points:
    points = find_basin(point)
    basins = basins.union(points)
    basin_sizes.append(len(points))

for i in range(len(data)):
    for j in range(len(data[0])):
        if (i,j) in basins:
            print("\033[91m" + str(data[i][j]) + "\033[0m", end="")
        else:
            print(data[i][j], end="")
    print()
basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
