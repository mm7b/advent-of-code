from collections import defaultdict


def to_blocks(disk_map):
    blocks = []
    for i, n in enumerate(disk_map):
        bs = [str(i // 2)] * n if i % 2 == 0 else [0] * n
        blocks.extend(bs)
    return blocks


def reorder(blocks):
    s, e = 0, len(blocks) - 1
    while True:
        while blocks[s]:
            s += 1
        while not blocks[e]:
            e -= 1
        if s >= e:
            break
        blocks[s], blocks[e] = blocks[e], blocks[s]
    return blocks


def get_free_slots(blocks):
    free_slots = defaultdict(int)
    i = 1
    while i < len(blocks) - 1:
        if not blocks[i]:
            ii = i + 1
            while not blocks[ii]:
                ii += 1
            free_slots[i] = ii - i
            i = ii
        i += 1
    return free_slots


def get_block(blocks, i):
    ii = i - 1
    while blocks[ii] == blocks[i]:
        ii -= 1
    length = i - ii
    return ii + 1, length


def find_slot(free_slots, i, length):
    slot, slot_size = None, None
    for s, size in free_slots.items():
        # Items can be added to the free_slots dictionnary -> finding
        # the min slot index is 2x faster than sorting the dict
        if s < i and length <= size and (not slot or s < slot):
            slot = s
            slot_size = size
    return slot, slot_size


def reorder_no_frag(blocks):
    free_slots = get_free_slots(blocks)
    seen = set()
    i = len(blocks)
    while i > 1:
        i -= 1
        if blocks[i] and blocks[i] not in seen:
            seen.add(blocks[i])
            i, length = get_block(blocks, i)
            slot, slot_size = find_slot(free_slots, i, length)
            if slot:
                # Move block
                blocks[slot : slot + length], blocks[i : i + length] = (
                    blocks[i : i + length],
                    blocks[slot : slot + length],
                )
                # Update free_slots dict by removing index of used free block and
                # adding the remaining free slots to (previous index + moved block size)
                del free_slots[slot]
                if (diff := slot_size - length) > 0:
                    free_slots[slot + length] += diff
    return blocks


def main():
    with open("inputs/day9.txt", "r", encoding="utf8") as f:
        blocks = to_blocks([int(n) for n in f.readline().strip()])

    # PART 1
    # print(sum([i * int(b) for i, b in enumerate(reorder(blocks))]))
    # PART 2
    print(sum([i * int(b) for i, b in enumerate(reorder_no_frag(blocks))]))


if __name__ == "__main__":
    main()
