import heapq
import sys
from copy import deepcopy

with open("input.txt", "r") as f:
    data = [[int(y) for y in x.strip()] for x in f.readlines()]

cost = [[sys.maxsize for _ in range(len(data[0]))] for _ in range(len(data))]
cost[0][0] = 0
visited = {}


def find_cheapest_coord():
    min_coord = (0, 0)
    min_cost = sys.maxsize
    for y in range(len(cost)):
        for x in range(len(cost[0])):
            if (x, y) not in visited:
                if cost[y][x] < min_cost:
                    min_cost = cost[y][x]
                    min_coord = (x, y)
    return min_coord


# love me some djikstra
while cost[-1][-1] == sys.maxsize:
    x, y = find_cheapest_coord()
    visited[(x, y)] = True
    cur = data[y][x]
    # relax
    if x > 0 and cost[y][x - 1] > cost[y][x] + data[y][x - 1]:
        cost[y][x - 1] = cost[y][x] + data[y][x - 1]
    if x < len(data[0]) - 1 and cost[y][x + 1] > cost[y][x] + data[y][x + 1]:
        cost[y][x + 1] = cost[y][x] + data[y][x + 1]
    if y > 0 and cost[y - 1][x] > cost[y][x] + data[y - 1][x]:
        cost[y - 1][x] = cost[y][x] + data[y - 1][x]
    if y < len(data) - 1 and cost[y + 1][x] > cost[y][x] + data[y + 1][x]:
        cost[y + 1][x] = cost[y][x] + data[y + 1][x]
print(cost[-1][-1])
