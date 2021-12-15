with open("input.txt", "r") as f:
    data = [[int(x) for x in line.strip()] for line in f.readlines()]


def step_2():
    global flashes
    to_increase = []
    has_flashed = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > 9:
                to_increase.append((i, j))
    while len(to_increase) > 0:
        curr = to_increase.pop()
        if data[curr[0]][curr[1]] > 9:
            flashes += 1
            has_flashed.append(curr)
            data[curr[0]][curr[1]] = 0
            # Increase all adjacent values by 1
            for i in range(curr[0] - 1, curr[0] + 2):
                for j in range(curr[1] - 1, curr[1] + 2):
                    if 0 <= i < len(data) and 0 <= j < len(data[i]):
                        data[i][j] += 1
                        if data[i][j] > 9:
                            to_increase.append((i, j))
    for i, j in has_flashed:
        data[i][j] = 0


flashes = 0

print(f"Before any steps:")
for line in data:
    for num in line:
        print(num, end="")
    print()
print()


def part_1():
    global flashes
    for step in range(1, 101):
        # first all energy levels are increased by 1
        for line in data:
            for i in range(len(line)):
                line[i] += 1
        # then any that are higher than 9 flashes and is set to 0, this increases the energy level of all adjacent octopuses by 1
        step_2()
        if step < 10 or step % 10 == 0:
            print(f"After step {step}:")
            for line in data:
                for num in line:
                    print(num, end="")
                print()
            print()


step = 0


def part_2():
    global flashes
    global step
    while sum([sum(line) for line in data]) != 0:
        step += 1
        # first all energy levels are increased by 1
        for line in data:
            for i in range(len(line)):
                line[i] += 1
        # then any that are higher than 9 flashes and is set to 0, this increases the energy level of all adjacent octopuses by 1
        step_2()


# part_1()
part_2()
print(step)
print(flashes)
