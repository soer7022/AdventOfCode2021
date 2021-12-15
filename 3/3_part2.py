with open("input.txt") as f:
    data = [s.strip() for s in f.readlines()]


oxygen_numbers = data.copy()
# Find oxygen rating
for index in range(len(data[0])):
    oxygen = ""
    for i in range(len(oxygen_numbers[0])):
        zeros = 0
        ones = 0
        for j in range(len(oxygen_numbers)):
            if oxygen_numbers[j][i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros <= ones:
            oxygen += "1"
        else:
            oxygen += "0"
    new_list = []
    if len(oxygen_numbers) == 1:
        break
    for number in oxygen_numbers:
        if number[index] == oxygen[index]:
            new_list.append(number)
    oxygen_numbers = new_list

print(oxygen_numbers[0])

# Find Co2 rating
co2_numbers = data.copy()
for index in range(len(data[0])):
    co2 = ""
    for i in range(len(co2_numbers[0])):
        zeros = 0
        ones = 0
        for j in range(len(co2_numbers)):
            if co2_numbers[j][i] == "0":
                zeros += 1
            else:
                ones += 1
        if ones >= zeros:
            co2 += "0"
        else:
            co2 += "1"
    new_list = []
    if len(co2_numbers) == 1:
        break
    for number in co2_numbers:
        if number[index] == co2[index]:
            new_list.append(number)
    co2_numbers = new_list

print(co2_numbers[0])

print(int(co2_numbers[0], 2) * int(oxygen_numbers[0], 2))
