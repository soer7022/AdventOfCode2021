points = set()
folds = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            continue
        if "fold along" in line:
            line = line.strip()
            axis, amount = line.split(" ")[-1].split("=")
            folds.append((axis, int(amount)))
            continue
        line = line.strip()
        x, y = line.split(",")
        points = points | {(int(x), int(y))}
# fold nr. 1


for fold in folds:
    if fold[0] == "y":
        points_to_move = [point for point in points if point[1] > fold[1]]
        points = points - set(points_to_move)
        for point in points_to_move:
            y = point[1]
            diff = fold[1] - y
            new_y = fold[1] + diff
            points = points | {(point[0], new_y)}

    else:
        points_to_move = [point for point in points if point[0] > fold[1]]
        points = points - set(points_to_move)
        for point in points_to_move:
            x = point[0]
            diff = fold[1] - x

            new_x = fold[1] + diff
            points = points | {(new_x, point[1])}
for y in range(max(points, key=lambda x: x[1])[1] + 1):
    for x in range(max(points, key=lambda x: x[0])[0] + 1):
        if (x, y) in points:
            print("#", end="")
        else:
            print(".", end="")
    print()
