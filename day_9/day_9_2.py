def get_checksum(string, disk_layout):
    return sum(index * val for index, val in enumerate(disk_layout) if val != ".")


def move_last_to_first_free(disk_layout, id_to_move, seq_length, free_mem):
    for idx, (index, length) in enumerate(free_mem):
        if length == -1 or length < seq_length:
            continue

        id_idx = disk_layout.index(id_to_move)

        if id_idx <= index:
            break

        for i in range(index, index + seq_length):
            disk_layout[i] = id_to_move

        for i in range(id_idx, id_idx + seq_length):
            disk_layout[i] = "."

        free_mem[idx] = (index + seq_length, length - seq_length)
        break


if __name__ == "__main__":
    string = []

    with open("day_9/day_9_2.in") as f:
        string = list(f.readline().strip())

    disk_layout = []
    seq_lens = []
    free_mem = []
    id_number = 0

    for i in range(len(string)):
        if i % 2 == 0:
            disk_layout.extend([id_number] * int(string[i]))
            seq_lens.append(int(string[i]))
            id_number += 1
        else:
            idx = len(disk_layout)
            disk_layout.extend(["."] * int(string[i]))
            free_mem.append((idx, int(string[i])))

    for i in range(id_number - 1, -1, -1):
        move_last_to_first_free(disk_layout, i, seq_lens[i], free_mem)

    print(get_checksum(string, disk_layout))
