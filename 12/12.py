vertices = {}
with open("input.txt") as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.split("-")
    try:
        vertices[line[0]].add(line[1])
    except KeyError:
        vertices[line[0]] = {line[1]}
    try:
        vertices[line[1]].add(line[0])
    except KeyError:
        vertices[line[1]] = {line[0]}


def travel(curr, visited, twice):
    if curr == "end":
        return 1
    out = 0
    for v in vertices[curr]:
        if v.islower():
            if v not in visited:
                out += travel(v, visited | {v}, twice)
            elif twice and v not in {"start", "end"}:
                out += travel(v, visited | {v}, False)
        else:
            out += travel(v, visited, twice)
    return out


print(travel("start", {"start"}, False))
print(travel("start", {"start"}, True))
