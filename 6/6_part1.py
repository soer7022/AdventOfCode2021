with open("input.txt") as f:
    data = [int(n) for n in f.readline().split(",")]

for i in range(80):
    for index, fish in enumerate(data):
        if fish == 0:
            data.append(9)
            data[index] = 6
        else:
            data[index] -= 1
    print(i)
print(len(data))
