def get_checksum(string, disk_layout):
    empty_block_ptr = int(string[0])
    last_full_block_ptr = len(disk_layout) - 1 - int(string[-1] if len(string) % 2 == 0 else 0)

    while empty_block_ptr < last_full_block_ptr and empty_block_ptr < len(disk_layout):
        if disk_layout[last_full_block_ptr] == ".":
            last_full_block_ptr -= 1
            continue

        if disk_layout[empty_block_ptr] != ".":
            empty_block_ptr += 1
            continue

        disk_layout[last_full_block_ptr], disk_layout[empty_block_ptr] = disk_layout[empty_block_ptr], disk_layout[last_full_block_ptr]

        empty_block_ptr += 1
        last_full_block_ptr -= 1

    return sum(index * val for index, val in enumerate(disk_layout) if val != ".")


if __name__ == "__main__":
    string = []

    with open("day_9/day_9_1.in") as f:
        string = list(f.readline().strip())

    disk_layout = []
    id_number = 0

    for i in range(len(string)):
        if i % 2 == 0:
            disk_layout.extend([id_number] * int(string[i]))
            id_number += 1
        else:
            disk_layout.extend(["."] * int(string[i]))

    print(get_checksum(string, disk_layout))
