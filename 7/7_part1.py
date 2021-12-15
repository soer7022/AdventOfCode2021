with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]
min_fuel = 9999999999999999
for i in range(min(data), max(data) + 1):
    total = 0
    data_copy = data.copy()
    for num in data_copy:
        total += abs(num - i)
    if total < min_fuel:
        min_fuel = total
print(min_fuel)
