from statistics import median

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

starts = {"(", "[", "<", "{"}
close = {")", "]", ">", "}"}
pair = {"(": ")", "[": "]", "<": ">", "{": "}"}
scores = {")": 1, "]": 2, ">": 4, "}": 3}
high_scores = []


def calculate_score(closers):
    score = 0
    while len(closers) > 0:
        c = closers.pop()
        score = score * 5 + scores[c]
    return score


for line in data:
    looking_for = []
    invalid_line = False
    for char in line:
        if char in starts:
            looking_for.append(pair[char])
        elif char in close and char != looking_for[-1]:
            invalid_line = True
            break
        elif char in close and char == looking_for[-1]:
            looking_for.pop()
    if not invalid_line:
        high_scores.append(calculate_score(looking_for))

high_scores.sort()
print(high_scores[len(high_scores) // 2])
