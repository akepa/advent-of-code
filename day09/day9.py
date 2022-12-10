def parse(line):
    f = line.split(' ')
    return f[0], int(f[1])


def move_l(h, t):
    h = (h[0] - 1, h[1])
    if t[0] - h[0] > 1:
        t = (t[0] - 1, h[1])
    return h, t


def move_r(h, t):
    h = (h[0] + 1, h[1])
    if h[0] - t[0] > 1:
        t = (t[0] + 1, h[1])
    return h, t


def move_u(h, t):
    h = (h[0], h[1] + 1)
    if h[1] - t[1] > 1:
        t = (h[0], t[1] + 1)
    return h, t


def move_d(h, t):
    h = (h[0], h[1] - 1)
    if t[1] - h[1] > 1:
        t = (h[0], t[1] - 1)
    return h, t


def exec():
    with open("input2.txt") as fp:
        moves = [parse(line.strip()) for line in fp]

    h = (0, 0)
    t = (0, 0)

    v_h = [h]
    v_t = [t]

    for d, q in moves:
        for i in range(0, q):
            if d == 'L':
                h, t = move_l(h, t)
            elif d == 'R':
                h, t = move_r(h, t)
            elif d == 'U':
                h, t = move_u(h, t)
            else:
                h, t = move_d(h, t)
            v_h.append(h)
            v_t.append(t)

    print(len(set(v_t)))


if __name__ == '__main__':
    exec()
