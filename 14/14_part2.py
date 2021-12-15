from functools import cache

with open("input.txt", "r") as f:
    template = f.readline().strip()
    f.readline()
    data = {pair: result for pair, result in [line.strip().split(" -> ") for line in f]}


pair_map_thing = {"NN": "C"}


@cache
def function(pair, iters):

    if not iters or not data.get(pair):
        return ""

    triple = pair[0] + data[pair] + pair[1]

    return f"{function(triple[0:2], iters - 1)}{triple[1]}{function(triple[1:3], iters - 1)}"


print(function("NN", 40))
for i in range(len(template) - 1):
    print(template[i] + function(template[i : i + 2], 2) + template[i + 1])
