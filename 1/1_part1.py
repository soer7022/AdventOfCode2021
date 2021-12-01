with open('input.txt') as f:
    data = [int(i) for i in f.readlines()]
count = 0
prev = 0
for i in data:
    if i > prev != 0:
        count += 1
    prev = i

print(count)