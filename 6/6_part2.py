from functools import cache

with open("input.txt") as f:
    data = [int(n) for n in f.readline().split(",")]


@cache
def simulate_fish(timer, days_remaining):
    if days_remaining == 0:
        return 1
    elif timer == 0:
        return simulate_fish(6, days_remaining - 1) + simulate_fish(
            8, days_remaining - 1
        )
    else:
        return simulate_fish(timer - 1, days_remaining - 1)


print(sum(simulate_fish(t, 256) for t in data))
