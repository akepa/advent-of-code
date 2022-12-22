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


def intersects(l, d_y):
    return abs(l['s'][1] - d_y) <= l['d']


def compute_intersection(l, d_y):
    diff_y = abs(l['s'][1] - d_y)

    x_min = l['s'][0] - l['d'] + diff_y
    x_max = l['s'][0] + l['d'] - diff_y

    return (x_min, x_max) if x_min < x_max else (x_max, x_min)


def is_fully_covered(intervals, lim):
    intervals = sorted(intervals)

    # First interval starts in a position x > 0
    if intervals[0][0] > 0:
        return False

    covered = 0

    for i in intervals:
        if i[1] < covered:
            continue
        if i[0] > covered + 1:
            return False
        covered = max(covered, i[1])
        if covered >= lim:
            return True
    return False


def exec():
    with open("input2.txt") as fp:
        lines = [parse_line(line.strip()) for line in fp if line.strip()]

    lim = 4000000

    for y in range(0, lim + 1):
        if y % 1000 == 0:
            print(f"Checking {y}...")

        intervals = []
        for l in lines:
            if intersects(l, y):
                x_min, x_max = compute_intersection(l, y)
                intervals.append((x_min, x_max))
        if not is_fully_covered(intervals, lim):
            for x in range(0, lim + 1):
                found = False
                for interval in intervals:
                    if interval[0] <= x <= interval[1]:
                        found = True
                        break
                if not found:
                    print((x, y))
                    print(x * 4000000 + y)
                    exit(0)


if __name__ == '__main__':
    exec()
