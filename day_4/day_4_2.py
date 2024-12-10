matrix = []
with open("day_4/day_4.in") as f:
    matrix = f.readlines()

count = 0


def top_left(i, j):
    if i < 0 or j < 0:
        return False

    if matrix[i][j] == "A":
        i -= 1
        j -= 1
        if i >= 0 and j >= 0 and matrix[i][j] == "S":
            return True

    return False


def top_right(i, j):
    if i < 0 or j >= len(matrix[i]):
        return False

    if matrix[i][j] == "A":
        i -= 1
        j += 1
        if i >= 0 and j < len(matrix[i]) and matrix[i][j] == "S":
            return True

    return False


def bottom_left(i, j):
    if i >= len(matrix) or j < 0:
        return False

    if matrix[i][j] == "A":
        i += 1
        j -= 1
        if i < len(matrix) and j >= 0 and matrix[i][j] == "S":
            return True

    return False


def bottom_right(i, j):
    if i >= len(matrix) or j >= len(matrix[i]):
        return False

    if matrix[i][j] == "A":
        i += 1
        j += 1
        if i < len(matrix) and j < len(matrix[i]) and matrix[i][j] == "S":
            return True

    return False


count = 0

i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        if matrix[i][j] != "M":
            j += 1
            continue

        temp = False

        if top_right(i - 1, j + 1):
            if j + 2 < len(matrix[i]) and matrix[i][j + 2] == "M" and top_left(i - 1, j + 1):
                count += 1

            if i - 2 >= 0 and matrix[i - 2][j] == "M" and bottom_right(i - 1, j + 1):
                count += 1

        if bottom_right(i + 1, j + 1):
            if j + 2 < len(matrix[i]) and matrix[i][j + 2] == "M" and bottom_left(i + 1, j + 1):
                count += 1

        if top_left(i - 1, j - 1):
            if i - 2 >= 0 and matrix[i - 2][j] == "M" and bottom_left(i - 1, j - 1):
                count += 1

        j += 1

    i += 1

print(count)
