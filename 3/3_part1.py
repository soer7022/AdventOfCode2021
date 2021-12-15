with open("input.txt") as f:
    data = [s.strip() for s in f.readlines()]

final = ""
for i in range(len(data[0])):
    zeros = 0
    ones = 0
    for j in range(len(data)):
        if data[j][i] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        final += "0"
    else:
        final += "1"

print(int(final, 2) * int("".join("1" if x == "0" else "0" for x in final), 2))
