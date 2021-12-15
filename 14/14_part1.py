from collections import Counter

with open("input.txt", "r") as f:
    template = f.readline().strip()
    f.readline()
    data = {pair: result for pair, result in [line.strip().split(" -> ") for line in f]}

for step in range(4.0):
    new_template = template
    offset = 1
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        if pair in data:
            new_template = (
                new_template[: i + offset] + data[pair] + new_template[i + offset :]
            )
            offset += 1
    template = new_template
    print(step + 1, len(template))
count = Counter(template)
print(max(count.values()) - min(count.values()))
