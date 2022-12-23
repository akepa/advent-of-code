NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

def build_actions():
    move_n = lambda pos: (pos[0] - 1, pos[1])
    move_s = lambda pos: (pos[0] + 1, pos[1])
    move_w = lambda pos: (pos[0], pos[1] - 1)
    move_e = lambda pos: (pos[0], pos[1] + 1)
    return [move_n, move_s, move_w, move_e]


def build_valid_checks():
    move_n = lambda pos, occupied: (pos[0] - 1, pos[1] - 1) not in occupied and (
        pos[0] - 1, pos[1]) not in occupied and (pos[0] - 1, pos[1] + 1) not in occupied
    move_s = lambda pos, occupied: (pos[0] + 1, pos[1] - 1) not in occupied and (
        pos[0] + 1, pos[1]) not in occupied and (pos[0] + 1, pos[1] + 1) not in occupied
    move_w = lambda pos, occupied: (pos[0] - 1, pos[1] - 1) not in occupied and (
        pos[0], pos[1] - 1) not in occupied and (pos[0] + 1, pos[1] - 1) not in occupied
    move_e = lambda pos, occupied: (pos[0] - 1, pos[1] + 1) not in occupied and (
        pos[0], pos[1] + 1) not in occupied and (pos[0] + 1, pos[1] + 1) not in occupied
    return [move_n, move_s, move_w, move_e]


def exec():
    with open("input2.txt") as fp:
        m = [list(line.strip()) for line in fp if line.strip()]

    elfs = build_elfs(m)
    occupied = set(elfs.keys())
    actions = build_actions()
    valid_checks = build_valid_checks()

    num_rounds = 10
    i = 0
    while True:

        next_action = i % 4

        candidates = {}
        # Find candidate actions
        for id, elf in elfs.items():
            if can_move(elf["pos"], occupied):
                is_valid_action = False
                for a in range(0, 4):
                    candidate_action = (next_action + a) % 4
                    if valid_checks[candidate_action](elf["pos"], occupied):
                        is_valid_action = True
                        break
                if is_valid_action:
                    candidate_pos = actions[candidate_action](elf["pos"])
                    items = candidates.get(candidate_pos, [])
                    items.append((elf["id"], candidate_action))
                    candidates[candidate_pos] = items

        # Filter out the candidates having more than two elves
        to_move = {}
        for candidate_pos, elf_ids in candidates.items():
            if len(elf_ids) < 2:
                elf_id = elf_ids[0][0]
                candidate_action = elf_ids[0][1]
                to_move[elf_id] = (candidate_pos, candidate_action)



        # Apply update
        print(f'Round {i+1}')
        if len(to_move) == 0:
            exit(0)

        for elf_id, (candidate_pos, candidate_action) in to_move.items():
            elf = elfs[elf_id]
            old_pos = elf["pos"]
            elf["pos"] = candidate_pos

            elf["next_action"] = (candidate_action + 1) % 4
            #print(f'{elf_id} moves from {old_pos} to {candidate_pos}')
            occupied.add(candidate_pos)
            occupied.remove(old_pos)

        i = i+1

    # Compute edges
    min_x = 999
    min_y = 999
    max_x = -1000
    max_y = -1000

    for id, elf in elfs.items():
        x,y = elf["pos"]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1

    print(len_x*len_y-len(elfs))

def can_move(pos, occupied):
    return (pos[0] - 1, pos[1] - 1) in occupied or (pos[0] - 1, pos[1]) in occupied or (
        pos[0] - 1, pos[1] + 1) in occupied or (
        pos[0], pos[1] - 1) in occupied or (pos[0], pos[1] + 1) in occupied or (
        pos[0] + 1, pos[1] - 1) in occupied or (
        pos[0] + 1, pos[1]) in occupied or (pos[0] + 1, pos[1] + 1) in occupied


def build_elfs(m):
    num_rows = len(m)
    num_cols = len(m[0])
    nodes = {}
    for r in range(0, num_rows):
        for c in range(0, num_cols):
            if m[r][c] == '#':
                id = (r, c)
                nodes[id] = {'id': id, 'pos': id}

    return nodes


if __name__ == '__main__':
    exec()