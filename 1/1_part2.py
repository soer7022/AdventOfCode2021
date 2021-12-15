with open("input.txt") as f:
    data = [int(i) for i in f.readlines()]

count = 0
prev = data[0] + data[1] + data[2]

for i in range(len(data)):
    try:
        curr = data[i] + data[i + 1] + data[i + 2]
    except IndexError:
        break
    if curr > prev:
        count += 1
    prev = curr
print(count)
