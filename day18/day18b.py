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
    count = 0
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


def compute_visible_sizes(x, y, z, m, max_dims, bubbles):
    count = 0
    if x == 0 or (not m[x - 1][y][z] and (x - 1, y, z) not in bubbles):
        count += 1
    if y == 0 or (not m[x][y - 1][z] and (x, y - 1, z) not in bubbles):
        count += 1
    if z == 0 or (not m[x][y][z - 1] and (x, y, z - 1) not in bubbles):
        count += 1

    if x == (max_dims["x"] - 1) or (not m[x + 1][y][z] and (x + 1, y, z) not in bubbles):
        count += 1
    if y == (max_dims["y"] - 1) or (not m[x][y + 1][z] and (x, y + 1, z) not in bubbles):
        count += 1
    if z == (max_dims["z"] - 1) or (not m[x][y][z + 1] and (x, y, z + 1) not in bubbles):
        count += 1
    return count


def fill_matrix(m, coords):
    for x, y, z in coords:
        m[x][y][z] = True


def merge(elem1, elem2, node_to_colour, colour_to_nodes):
    c1 = node_to_colour[elem1]
    c2 = node_to_colour[elem2]
    if c1 < c2:
        for i in colour_to_nodes[c2]:
            node_to_colour[i] = c1
        colour_to_nodes[c1].extend(colour_to_nodes[c2])
        del colour_to_nodes[c2]
    elif c2 > c1:
        for i in colour_to_nodes[c1]:
            node_to_colour[i] = c2
        colour_to_nodes[c2].extend(colour_to_nodes[c1])
        del colour_to_nodes[c1]


def build_node_to_colour(max_dims):
    d = {}
    count = 0
    for x in range(0, max_dims["x"]):
        for y in range(0, max_dims["y"]):
            for z in range(0, max_dims["z"]):
                d[(x, y, z)] = count
                count += 1
    return d


def build_colour_to_node(max_dims):
    d = {}
    count = 0
    for x in range(0, max_dims["x"]):
        for y in range(0, max_dims["y"]):
            for z in range(0, max_dims["z"]):
                d[count] = [(x, y, z)]
                count += 1
    return d


def find_bubbles(m, max_dims):
    checked = set()
    q = [(0, 0, 0)]
    node_to_colour = build_node_to_colour(max_dims)
    colour_to_nodes = build_colour_to_node(max_dims)
    while len(q) > 0:
        x, y, z = q[0]
        q = q[1:]

        if x + 1 < max_dims["x"]:
            cand = (x + 1, y, z)
            if m[x][y][z] == m[x + 1][y][z]:
                merge((x, y, z), cand, node_to_colour, colour_to_nodes)
            if cand not in checked:
                checked.add(cand)
                q.append(cand)

        if y + 1 < max_dims["y"]:
            cand = (x, y + 1, z)
            if m[x][y][z] == m[x][y + 1][z]:
                merge((x, y, z), cand, node_to_colour, colour_to_nodes)
            if cand not in checked:
                checked.add(cand)
                q.append(cand)

        if z + 1 < max_dims["z"]:
            cand = (x, y, z + 1)
            if m[x][y][z] == m[x][y][z + 1]:
                merge((x, y, z), cand, node_to_colour, colour_to_nodes)
            if cand not in checked:
                checked.add(cand)
                q.append(cand)

        if x - 1 >= 0:
            cand = (x - 1, y, z)
            if m[x][y][z] == m[x - 1][y][z]:
                merge((x, y, z), cand, node_to_colour, colour_to_nodes)

        if y - 1 >= 0:
            cand = (x, y - 1, z)
            if m[x][y][z] == m[x][y - 1][z]:
                merge((x, y, z), cand, node_to_colour, colour_to_nodes)

        if z - 1 >= 0:
            cand = (x, y, z - 1)
            if m[x][y][z] == m[x][y][z - 1]:
                merge((x, y, z), cand, node_to_colour, colour_to_nodes)

    bubbles = set()
    for k, v in colour_to_nodes.items():
        is_bubble = True
        for x, y, z in v:
            if m[x][y][z] or x == 0 or y == 0 or z == 0 or x + 1 == max_dims["x"] or y + 1 == max_dims["y"] or z + 1 == \
                    max_dims["z"]:
                is_bubble = False
                break
        if is_bubble:
            bubbles.update(v)
    return bubbles


def exec():
    with open("input2.txt") as fp:
        coords = [parse_line(line.strip()) for line in fp if line.strip()]

    max_dims = find_limit(coords)
    print(max_dims)

    m = init_matrix(max_dims)
    fill_matrix(m, coords)

    bubbles = find_bubbles(m, max_dims)
    print(bubbles)

    count = 0
    for x, y, z in coords:
        visible_sizes = compute_visible_sizes(x, y, z, m, max_dims, bubbles)
        # print(f'{x},{y},{z} -> {visible_sizes}')
        count += visible_sizes

    print(count)


if __name__ == '__main__':
    exec()
