lines = []

with open("day_8/day_8_1.in") as f:
    data = f.readlines()
    for line in data:
        lines.append(list(line.strip()))


def determine_antinodes(lines, i1, j1, i2, j2):
    y_dist = abs(i1 - i2)
    x_dist = abs(j1 - j2)

    bottom_node_y = max(i1, i2) + y_dist if max(i1, i2) + y_dist < len(lines) else -1
    top_node_y = min(i1, i2) - y_dist if min(i1, i2) - y_dist >= 0 else -1

    right_node_x = max(j1, j2) + x_dist if max(j1, j2) + x_dist < len(lines[0]) else -1
    left_node_x = min(j1, j2) - x_dist if min(j1, j2) - x_dist >= 0 else -1

    nodes = []

    if max(j1, j2) == j1:
        if i1 <= i2:  # i1 j1 is bottom left
            while bottom_node_y != -1 and left_node_x >= 0 and bottom_node_y < len(lines):
                nodes.append((left_node_x, bottom_node_y))
                left_node_x -= x_dist
                bottom_node_y += y_dist

            while right_node_x != -1 and right_node_x < len(lines[0]) and top_node_y >= 0:
                nodes.append((right_node_x, top_node_y))
                right_node_x += x_dist
                top_node_y -= y_dist

        else:  ##i1 j1 is bottom right
            while right_node_x != -1 and bottom_node_y != -1 and right_node_x < len(lines[0]) and bottom_node_y < len(lines):
                nodes.append((right_node_x, bottom_node_y))
                right_node_x += x_dist
                bottom_node_y += y_dist

            while left_node_x >= 0 and top_node_y >= 0:
                nodes.append((left_node_x, top_node_y))
                left_node_x -= x_dist
                top_node_y -= y_dist
    else:
        if i2 <= i1:  # i2 j2 is bottom left
            while bottom_node_y != -1 and left_node_x >= 0 and bottom_node_y < len(lines):
                nodes.append((left_node_x, bottom_node_y))
                left_node_x -= x_dist
                bottom_node_y += y_dist

            while right_node_x != -1 and right_node_x < len(lines[0]) and top_node_y >= 0:
                nodes.append((right_node_x, top_node_y))
                right_node_x += x_dist
                top_node_y -= y_dist
        else:  ##i2 j2 is bottom right
            while right_node_x != -1 and bottom_node_y != -1 and right_node_x < len(lines[0]) and bottom_node_y < len(lines):
                nodes.append((right_node_x, bottom_node_y))
                right_node_x += x_dist
                bottom_node_y += y_dist

            while left_node_x >= 0 and top_node_y >= 0:
                nodes.append((left_node_x, top_node_y))
                left_node_x -= x_dist
                top_node_y -= y_dist

    nodes.append((j1, i1))
    nodes.append((j2, i2))

    return nodes


freqs = dict()
node_count = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == ".":
            continue

        freq = lines[i][j]

        if freq not in freqs:
            freqs[freq] = [(i, j)]
        else:
            freqs[freq].append((i, j))


for freq, locations in freqs.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            loc1 = locations[i]
            loc2 = locations[j]

            antinodes = determine_antinodes(lines, loc1[0], loc1[1], loc2[0], loc2[1])
            print(loc1, loc2)
            print(antinodes)

            for x, y in antinodes:
                if x == -1 or y == -1 or lines[y][x] == "#":
                    continue

                lines[y][x] = "#"
                node_count += 1

print(node_count)

for line in lines:
    print("".join(line))
