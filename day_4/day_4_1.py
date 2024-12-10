from enum import Enum
from dataclasses import dataclass


@dataclass
class XYIncrement:
    x: int
    y: int


class Direction(Enum):
    UP = XYIncrement(0, -1)
    DOWN = XYIncrement(0, 1)
    LEFT = XYIncrement(-1, 0)
    RIGHT = XYIncrement(1, 0)
    UP_LEFT = XYIncrement(-1, -1)
    UP_RIGHT = XYIncrement(1, -1)
    DOWN_LEFT = XYIncrement(-1, 1)
    DOWN_RIGHT = XYIncrement(1, 1)


def check_direction(matrix, i, j, dir: XYIncrement):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
        return 0

    length = 3

    while length > 0 and i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        if length == 3 and matrix[i][j] == "M" or length == 2 and matrix[i][j] == "A" or length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        i += dir.y
        j += dir.x

    return 1 if length == 0 else 0


matrix = []
with open("day_4/day_4.in") as f:
    matrix = f.readlines()

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != "X":
            continue

        for dir in Direction:
            count += check_direction(matrix, i + dir.value.y, j + dir.value.x, dir.value)

print(count)
