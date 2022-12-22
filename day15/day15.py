def parse_cord_item(a):
    return int(a.split("=")[1].replace(",", "").replace(":", ""))


def parse_coord(a, b):
    return parse_cord_item(a), parse_cord_item(b)


def parse_line(l):
    f = l.split(" ")
    s = parse_coord(f[2], f[3])
    b = parse_coord(f[8], f[9])
    d = abs(s[0] - b[0]) + abs(s[1] - b[1])
    return {'s': s, 'b': b, 'd': d}


def find_bounds(coords):
    min_x = 999999999
    max_x = -1
    min_y = 999999999
    max_y = -1

    for c in coords:
        if c['s'][0] > max_x:
            max_x = c['s'][0]
        if c['s'][0] < min_x:
            min_x = c['s'][0]
        if c['s'][1] > max_y:
            max_y = c['s'][1]
        if c['s'][1] < min_y:
            min_y = c['s'][1]
        if c['b'][0] > max_x:
            max_x = c['b'][0]
        if c['b'][0] < min_x:
            min_x = c['b'][0]
        if c['b'][1] > max_y:
            max_y = c['b'][1]
        if c['b'][1] < min_y:
            min_y = c['b'][1]
    return (min_x, max_x), (min_y, max_y)


def intersects(l, d_y):
    return abs(l['s'][1] - d_y) <= l['d']


def compute_intersection(l, d_y):
    diff_y = abs(l['s'][1] - d_y)

    x_min = l['s'][0] - l['d'] + diff_y
    x_max = l['s'][0] + l['d'] - diff_y

    return (x_min, x_max) if x_min < x_max else (x_max, x_min)


def exec():
    with open("input2.txt") as fp:
        lines = [parse_line(line.strip()) for line in fp if line.strip()]

    x, y = find_bounds(lines)

    d_y = 2000000
    # d_y = 10

    v = set()

    for l in lines:
        if intersects(l, d_y):
            x_min, x_max = compute_intersection(l, d_y)
            print(f'{l} --> {x_min},{x_max}')
            for i in range(x_min, x_max + 1):
                v.add(i)
        else:
            print(f"not intersecting: {l}")
    print(f'x bounds: {x}')
    print(f'y bounds: {y}')

    # print(v)
    print(len(v))

    beacons_included = {l['b'] for l in lines if l['b'][1] == d_y and l['b'][0] in v}
    # len()
    print(len(v) - len(beacons_included))

    print(f'min: {min(v)}')
    print(f'max: {max(v)}')


if __name__ == '__main__':
    exec()
