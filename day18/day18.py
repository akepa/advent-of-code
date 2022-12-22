def parse_line(line):
    f = line.split(",")
    return (int(f[0]), int(f[1]), int(f[2]))


def find_limit_in_axis(coords, param):
    mx = -1

    for c in coords:
        if c[param] > mx:
            mx = c[param]
    return mx


def find_limit(coords):
    return {
        'x': find_limit_in_axis(coords, 0) + 1,
        'y': find_limit_in_axis(coords, 1) + 1,
        'z': find_limit_in_axis(coords, 2) + 1,
    }


def init_matrix(max_dims):
    m = []
    for x in range(0, max_dims["x"]):
        x_a = []
        for y in range(0, max_dims["y"]):
            y_a = []
            for z in range(0, max_dims["z"]):
                y_a.append(False)
            x_a.append(y_a)
        m.append(x_a)
    return m


def fill_matrix(m, coords):
    for x, y, z in coords:
        m[x][y][z] = True


def compute_visible_sizes(x, y, z, m, max_dims):
    count = 0
    if x == 0 or not m[x - 1][y][z]:
        count += 1
    if y == 0 or not m[x][y - 1][z]:
        count += 1
    if z == 0 or not m[x][y][z - 1]:
        count += 1

    if x == (max_dims["x"] - 1) or not m[x + 1][y][z]:
        count += 1
    if y == (max_dims["y"] - 1) or not m[x][y + 1][z]:
        count += 1
    if z == (max_dims["z"] - 1) or not m[x][y][z + 1]:
        count += 1
    return count


def exec():
    with open("input2.txt") as fp:
        coords = [parse_line(line.strip()) for line in fp if line.strip()]

    max_dims = find_limit(coords)
    print(max_dims)

    m = init_matrix(max_dims)
    fill_matrix(m, coords)

    count = 0

    for x, y, z in coords:
        visible_sizes = compute_visible_sizes(x, y, z, m, max_dims)
        print(f'{x},{y},{z} -> {visible_sizes}')
        count += visible_sizes

    print(count)


if __name__ == '__main__':
    exec()
