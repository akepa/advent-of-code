def find_bounds(coords):
    min_x = 0
    max_x = -1
    min_y = 0
    max_y = -1

    for x in range(0, len(coords)):
        for y in range(0, len(coords[x])):
            c = coords[x][y]
            if c[0] > max_x:
                max_x = c[0]
            if c[1] > max_y:
                max_y = c[1]
    return (min_x, max_x*2), (min_y, max_y + 2)


def print_scenario(s):
    for l in s:
        print(l)


def add_rocks_line(s, a, b):
    if a[0] != b[0]:
        mn = min(a[0], b[0])
        mx = max(a[0], b[0])
        for i in range(mn, mx + 1):
            s[a[1]][i] = "#"
    else:
        mn = min(a[1], b[1])
        mx = max(a[1], b[1])
        for i in range(mn, mx + 1):
            s[i][a[0]] = "#"


def add_rocks(s, coords):
    for c in coords:
        for i in range(0, len(c) - 1):
            add_rocks_line(s, c[i], c[i + 1])


def normalize_x_axis(coords, c_min):
    coords_norm = []
    for c in coords:
        coords_norm.append([(i[0] - c_min, i[1]) for i in c])
    return coords_norm


def to_scenario(coords):
    c, r = find_bounds(coords)
    # coords_norm = normalize_x_axis(coords, c[0])
    num_rows = r[1] - r[0] + 1
    num_cols = c[1] - c[0] + 1

    s = init_scenario(num_cols, num_rows)
    source = (500, 0)

    add_rocks(s, coords)
    for i in range(0, c[1]):
        s[r[1]][i] = "#"

    return s, source, r[1]


def init_scenario(num_cols, num_rows):
    s = []
    for i in range(0, num_rows):
        v = []
        for j in range(0, num_cols):
            v.append('.')
        s.append(v)
    return s


def to_coordinates(lines):
    coords = []
    for l in lines:
        items = l.split(" -> ")
        coords.append([(int(f[0]), int(f[1])) for f in [i.split(',') for i in items]])
    return coords


def exec():
    with open("input2.txt") as fp:
        lines = [line.strip() for line in fp if line.strip()]

    coords = to_coordinates(lines)
    scenario, source, max_row = to_scenario(coords)

    count = 0
    is_finished = False
    while not is_finished:
        #print(print_scenario(scenario))

        pos = source
        is_moving = True
        while is_moving:
            if scenario[pos[1] + 1][pos[0]] == '.':
                pos = (pos[0], pos[1] + 1)
            elif scenario[pos[1] + 1][pos[0] - 1] == '.':
                pos = (pos[0] - 1, pos[1] + 1)
            elif scenario[pos[1] + 1][pos[0] + 1] == '.':
                pos = (pos[0] + 1, pos[1] + 1)
            elif source == pos:
                is_finished = True
                count += 1
                break
            else:
                scenario[pos[1]][pos[0]] = 'o'
                count += 1
                is_moving = False
    print(count)


if __name__ == '__main__':
    exec()
