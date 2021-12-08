with open('input.txt') as f:
    data = [i.strip().split(" ") for l in f.readlines() for i in l.split("|")]

total = 0

def seen_string(string: set, know:dict):
    for key in know.keys():
        if type(key) != int:
            if string == set(key):
                return know[key]
    return False

for i in range(0, len(data), 2):
    known = {}
    readings = data[i]
    to_find = data[i+1]
    for i in range(200):
        for reading in readings:
            letters = set(reading)
            if reading not in known and not seen_string(letters, known):
                if len(reading) == 2:
                    known[reading] = 1
                    known[1] = reading
                elif len(reading) == 4:
                    known[reading] = 4
                    known[4] = reading
                elif len(reading) == 3:
                    known[reading] = 7
                    known[7] = reading
                elif len(reading) == 7:
                    known[reading] = 8
                    known[8] = reading
                elif len(reading) == 5:
                    # Number is 5, 2 or 3
                    # Check if number is 3
                    if 1 in known:
                        if set(known[1]).issubset(letters):
                            #must be 3
                            known[reading] = 3
                            known[3] = reading
                            continue
                    # Check if number is 2
                    if 4 in known and 3 in known:
                        diff = letters.difference(set(known[4]))
                        if len(diff) == 2:
                            # must be 5
                            known[reading] = 5
                            known[5] = reading
                        elif len(diff) == 3:
                            # must be 2
                            known[reading] = 2
                            known[2] = reading

                    pass
                elif len(reading) == 6:
                    # Number is 9, 6 or 0
                    letters = set(reading)
                    num_9 = set("cefabd")
                    # Check if number is 0 or 9
                    if 3 in known and 6 in known:
                        #print(set(known[3]).issubset(letters))
                        #print(set(known[3]).issubset(num_9))
                        pass
                    # Check if number is 9
                    if 4 in known:
                        letters_in_4 = set(known[4])
                        if letters_in_4.issubset(letters):
                            # number must be 9
                            known[9] = reading
                            known[reading] = 9
                            continue
                        if 1 in known:
                            if not set(known[1]).issubset(letters):
                                # must be 6
                                known[reading] = 6
                                known[6] = reading
                            else:
                                # must be 0
                                known[reading] = 0
                                known[0] = reading
    total += int(str(seen_string(set(to_find[0]), known))+ str(seen_string(set(to_find[1]), known)) + str(seen_string(set(to_find[2]), known)) + str(seen_string(set(to_find[3]), known)))

print(total)

