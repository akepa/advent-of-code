def parse(line):
    f = line.split(' ')
    return f[0], int(f[1])


def move(h, t):
    # left
    if t[0] - h[0] > 1:
        x = t[0] - 1
        y = update_second_axis(h[1], t[1])
        return x, y
    # right
    if h[0] - t[0] > 1:
        x = t[0] + 1
        y = update_second_axis(h[1], t[1])
        return x, y
        # up
    if h[1] - t[1] > 1:
        y = t[1] + 1
        x = update_second_axis(h[0], t[0])
        return x, y
    # down
    if t[1] - h[1] > 1:
        y = t[1] - 1
        x = update_second_axis(h[0], t[0])
        return x, y
    return t


def update_second_axis(h, t):
    return t if t == h else (t + 1 if h > t else t - 1)


def draw(hist):
    s = set(hist)
    for i in range(0, 26):
        for j in range(0, 20):
            if (i - 11, j - 5) in s:
                print("#", end='')
            else:
                print(".", end='')
        print('')


def draw(p):
    d = {}
    for i in reversed(range(0, 10)):
        d[p[i]] = i

    # (0,0) - (-11, 15)
    # (1,1) - (-10, 14)

    for y in range(0, 26):
        for x in range(0, 20):
            if (-11 + x, 15 - y) in d:
                print(d[(-11 + x, 15 - y)], end='')
            else:
                print(".", end='')
        print('')
    print("############################################3")


def exec():
    with open("input2.txt") as fp:
        moves = [parse(line.strip()) for line in fp]

    p = [(0, 0) for i in range(0, 10)]
    hist = [(0, 0)]

    for d, q in moves:
        #print(f"{d} {q}")
        for i in range(0, q):
            h = p[0]
            if d == 'L':
                p[0] = (h[0] - 1, h[1])
            elif d == 'R':
                p[0] = (h[0] + 1, h[1])
            elif d == 'U':
                p[0] = (h[0], h[1] + 1)
            else:
                p[0] = (h[0], h[1] - 1)
            for j in range(1, 10):
                p[j] = move(p[j - 1], p[j])
            hist.append(p[9])
            #draw(p)
            # print(p)

    #print(sorted(list(set(hist))))
    #draw(hist)

    print(len(set(hist)))


if __name__ == '__main__':
    exec()
