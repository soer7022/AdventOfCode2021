from functools import cache

with open('input.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]
min_fuel = 9999999999999999


@cache
def fuel_required(distance):
    fuel = 0
    for i in range(distance + 1):
        fuel += i
    return fuel


assert fuel_required(11) == 66
for i in range(min(data), max(data) + 1):
    total = 0
    data_copy = data.copy()
    for num in data_copy:
        total += fuel_required(abs(num - i))
    if total < min_fuel:
        min_fuel = total
print(min_fuel)
