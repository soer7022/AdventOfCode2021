with open("input.txt") as f:
    data = [l.split("|")[-1].strip().split(" ") for l in f.readlines()]

total = 0
for line in data:
    for num in line:
        if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
            total += 1
print(total)
