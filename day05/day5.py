import numpy as np


def filter_nonempty(lst):
    return [x for x in lst if x.strip()]


def parse_cranes(lines):
    rotated = np.rot90(lines[:-1], k=-1)
    cranes = [filter_nonempty(rotated[i].tolist()) for i in range(1, len(rotated), 4)]
    return cranes


def parse_move(stripped):
    tokens = stripped.split(' ')
    # Change to 0..N-1
    return int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1


def get_input():
    cranes = None
    moves = []
    with open("input2.txt") as fp:
        lines = []

        # First part of the input
        for line in fp:
            if not line.strip():
                # End first part of the input
                break
            chars = list(line)
            lines.append(chars)
        cranes = parse_cranes(lines)

        # Second part of the input
        for line in fp:
            stripped = line.strip()
            if stripped:
                moves.append(parse_move(stripped))

    return cranes, moves


def apply_moves(cranes, moves):
    for q, s, t in moves:
        for i in range(0, q):
            item = cranes[s].pop()
            cranes[t].append(item)


def exec():
    cranes, moves = get_input()
    apply_moves(cranes, moves)
    print(''.join([c.pop() for c in cranes]))

if __name__ == '__main__':
    exec()
