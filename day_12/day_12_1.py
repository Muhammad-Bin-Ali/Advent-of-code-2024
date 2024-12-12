from enum import Enum


class Direction(Enum):
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]


def get_all_occurences(char, plot):
    occurences = ([(i, j) for j in range(len(plot[i])) if plot[i][j] == char] for i in range(len(plot)))
    return [i for x in occurences for i in x if x]


def get_area(plot, i, j, char, coords):
    for direction in Direction:
        new_i = direction.value[0] + i
        new_j = direction.value[1] + j

        if new_i >= 0 and new_j >= 0 and new_i < len(plot) and new_j < len(plot[new_i]) and plot[new_i][new_j] == char and [new_i, new_j] not in coords:
            coords.append([new_i, new_j])
            get_area(plot, new_i, new_j, char, coords)


def get_perimeter(char, coords, plot):
    count = 0
    for i, j in coords:
        if i == 0:
            count += 1
        elif plot[i - 1][j] != char:
            count += 1

        if i == len(plot) - 1:
            count += 1
        elif plot[i + 1][j] != char:
            count += 1

        if j == 0:
            count += 1
        elif plot[i][j - 1] != char:
            count += 1

        if j == len(plot[i]) - 1:
            count += 1
        elif plot[i][j + 1] != char:
            count += 1

    return count


if __name__ == "__main__":
    data = []
    chars = set()

    with open("day_12/day_12_1.in") as f:
        temp = f.readlines()
        for line in temp:
            data.append([x for x in line.strip()])
            chars.update(data[-1])

    areas = []

    for char in chars:
        occurences = get_all_occurences(char, data)
        found = []

        for i, j in occurences:
            if (i, j) in found:
                continue
            coords = [[i, j]]
            get_area(data, i, j, char, coords)

            for i_1, j_1 in coords:
                found.append((i_1, j_1))

            areas.append((char, coords))

    print(sum(get_perimeter(char, coords, data) * len(coords) for char, coords in areas))
