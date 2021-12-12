with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

starts = {"(", "[", "<", "{"}
close = {")", "]", ">", "}"}
pair = {"(": ")", "[": "]", "<": ">", "{": "}"}
scores =  {")": 3, "]": 57, ">": 25137, "}": 1197}
total = 0
for line in data:
    looking_for = []
    for char in line:
        if char in starts:
            looking_for.append(pair[char])
        elif char in close and char != looking_for[-1]:
            total += scores[char]
            print(line)
            break
        elif char in close and char == looking_for[-1]:
            looking_for.pop()


print(total)