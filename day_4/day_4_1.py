matrix = []
with open("day_4/day_4.in") as f:
    matrix = f.readlines()

count = 0


def check_up(i, j):
    if i < 0:
        return 0

    length = 3

    while length > 0 and i >= 0:
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break
        i -= 1

    if length == 0:
        return 1
    else:
        return 0


def check_down(i, j):
    if i >= len(matrix):
        return 0

    length = 3

    while length > 0 and i < len(matrix):
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        i += 1

    if length == 0:
        return 1
    else:
        return 0


def check_left(i, j):
    if j < 0:
        return 0

    len = 3

    while len > 0 and j >= 0:
        if len == 3 and matrix[i][j] == "M":
            len -= 1
        elif len == 2 and matrix[i][j] == "A":
            len -= 1
        elif len == 1 and matrix[i][j] == "S":
            len -= 1
        else:
            break

        j -= 1

    if len == 0:
        return 1
    else:
        return 0


def check_right(i, j):
    if j >= len(matrix[0]):
        return 0

    length = 3

    while length > 0 and j < len(matrix[i]):
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        j += 1

    if length == 0:
        return 1
    else:
        return 0


def check_up_left(i, j):
    if j < 0 or i < 0:
        return 0

    length = 3

    while length > 0 and j >= 0 and i >= 0:
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        j -= 1
        i -= 1

    if length == 0:
        return 1
    else:
        return 0


def check_up_right(i, j):
    if j >= len(matrix[i]) or i < 0:
        return 0

    length = 3

    while length > 0 and j < len(matrix[i]) and i >= 0:
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        j += 1
        i -= 1

    if length == 0:
        return 1
    else:
        return 0


def check_down_left(i, j):
    if i >= len(matrix) or j < 0:
        return 0

    length = 3

    while length > 0 and j >= 0 and i < len(matrix):
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        j -= 1
        i += 1

    if length == 0:
        return 1
    else:
        return 0


def check_down_right(i, j):
    if i >= len(matrix) or j >= len(matrix[i]):
        return 0

    length = 3

    while length > 0 and i < len(matrix) and j < len(matrix[i]):
        if length == 3 and matrix[i][j] == "M":
            length -= 1
        elif length == 2 and matrix[i][j] == "A":
            length -= 1
        elif length == 1 and matrix[i][j] == "S":
            length -= 1
        else:
            break

        j += 1
        i += 1

    if length == 0:
        return 1
    else:
        return 0


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != "X":
            continue

        count += (
            check_up(i - 1, j)
            + check_down(i + 1, j)
            + check_left(i, j - 1)
            + check_right(i, j + 1)
            + check_up_left(i - 1, j - 1)
            + check_up_right(i - 1, j + 1)
            + check_down_left(i + 1, j - 1)
            + check_down_right(i + 1, j + 1)
        )


print(count)
