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
            print("\033[91m" + str(curr) + "\033[0m", end="")
        else:
            print(curr, end="")
    print()

print(total)
