from itertools import cycle
import time

# Cycle: 106,18,352,28,125,40,15,293,271,169,9,92,288,34,66,115,88,29,24,217,132,101,83,58,18,352,28,125,40,15,293,271,169,9,92,288,34,66,115,88,29,24,217,132,101,83,58,18


def get_init_state_1(y_start):
    return [(2, y_start), (3, y_start), (4, y_start), (5, y_start)]


def get_init_state_2(y_start):
    return [(3, y_start), (2, y_start + 1), (3, y_start + 1), (4, y_start + 1), (3, y_start + 2)]


def get_init_state_3(y_start):
    return [(2, y_start), (3, y_start), (4, y_start), (4, y_start + 1), (4, y_start + 2)]


def get_init_state_4(y_start):
    return [(2, y_start), (2, y_start + 1), (2, y_start + 2), (2, y_start + 3)]


def get_init_state_5(y_start):
    return [(2, y_start), (3, y_start), (2, y_start + 1), (3, y_start + 1)]


def get_init_state(y_start, fig):
    if fig == 1:
        return get_init_state_1(y_start)
    if fig == 2:
        return get_init_state_2(y_start)
    if fig == 3:
        return get_init_state_3(y_start)
    if fig == 4:
        return get_init_state_4(y_start)
    if fig == 5:
        return get_init_state_5(y_start)


def move_right(coords):
    return [(x + 1, y) for (x, y) in coords]


def move_left(coords):
    return [(x - 1, y) for (x, y) in coords]


def is_blocked(x, y, fixed_coords):
    return x in fixed_coords.get(y, set())


def can_move_right(coords, fixed_coords):
    for x, y in coords:
        if x == 6 or is_blocked(x + 1, y, fixed_coords):
            return False
    return True


def can_move_left(coords, fixed_coords):
    for x, y in coords:
        if x == 0 or is_blocked(x - 1, y, fixed_coords):
            return False
    return True


def move_down(coords):
    return [(x, y - 1) for (x, y) in coords]


def can_move_down(coords, fixed_coords):
    for x, y in coords:
        if y == 0 or is_blocked(x, y - 1, fixed_coords):
            return False
    return True


def fix_coordinates(fixed_coords, coords, y_prev, i):
    for x, y in coords:
        y_d = fixed_coords.get(y, set())
        y_d.add(x)
        fixed_coords[y] = y_d
        # Optimization to remove the size of the dictionary
        if len(y_d) == 7:
            new_d = {}
            for k,v in fixed_coords.items():
                if k >= y:
                    new_d[k] = v
            fixed_coords = new_d
            if y_prev != -1:
                print(f'{y-y_prev} -> {y} --> {i}')
            y_prev = y

    return fixed_coords, y_prev


def exec():
    with open("input2.txt") as fp:
        jet_pattern = list(fp.readline().strip())

    iter_jet = cycle(jet_pattern)
    iter_fig = cycle([1, 2, 3, 4, 5])

    max_y = 0
    fixed_coords = {}
    y_prev = -1

    num_rocks = 1000000000000 - 1710 * 584795320 # every 1710 rocks, it grows 2647 lines
    for i in range(0, num_rocks):

        y_start = max_y + 3
        fig = next(iter_fig)
        coords = get_init_state(y_start, fig)
        is_fixed = False
        while not is_fixed:
            move = next(iter_jet)
            if move == '>' and can_move_right(coords, fixed_coords):
                coords = move_right(coords)
            elif move == '<' and can_move_left(coords, fixed_coords):
                coords = move_left(coords)

            if can_move_down(coords, fixed_coords):
                coords = move_down(coords)
            else:
                fixed_coords, y_prev = fix_coordinates(fixed_coords, coords, y_prev, i)
                is_fixed = True
        max_y = max(fixed_coords.keys()) + 1
        #print(fixed_coords)
    print(max_y + 584795320*2647)

if __name__ == '__main__':
    exec()
