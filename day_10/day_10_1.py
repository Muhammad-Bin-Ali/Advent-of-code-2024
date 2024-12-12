from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def backtrack(data, i, j, count):
    if data[i][j] == 9:
        return count + 1

    for dir in Direction:
        (vert, hor) = dir.value
        new_i = i + vert
        new_j = j + hor

        if new_i >= 0 and new_i < len(data) and new_j >= 0 and new_j < len(data[new_i]) and data[new_i][new_j] - data[i][j] == 1:
            count = backtrack(data, new_i, new_j, count)

    return count


if __name__ == "__main__":
    data = []

    with open("day_10/day_10_2.in") as f:
        temp = f.readlines()
        for line in temp:
            data.append([int(x) for x in line.strip()])

    total_score = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                continue
            score = backtrack(data, i, j, 0)
            print(i, j, score)
            total_score += score

    print(total_score)
