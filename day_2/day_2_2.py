from enum import Enum


class ValidityCheck(Enum):
    INCREASING = 1
    DECREASING = 2


def is_valid(level, choice, removed=False):
    valid = True
    i = 0
    while i < len(level) - 1:
        if choice == ValidityCheck.INCREASING:
            valid = level[i] < level[i + 1]
        else:
            valid = level[i] > level[i + 1]

        valid = valid and not abs(level[i + 1] - level[i]) > 3

        if not valid and not removed:
            valid = is_valid(level[: i + 1] + level[i + 2 :], choice, True) or is_valid(level[:i] + level[i + 1 :], choice, True)
            break
        elif not valid:
            break
        i += 1

    return valid


levels = []

with open("day_2/day_2.in", "r") as f:
    levels = f.readlines()

safe_count = 0

for level in levels:
    level = [int(i) for i in level.split()]
    if is_valid(level[:], ValidityCheck.INCREASING) or is_valid(level[:], ValidityCheck.DECREASING):
        safe_count += 1

print(safe_count)
