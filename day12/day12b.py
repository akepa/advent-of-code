def is_reachable(x, y):
    return x + 1 >= y


def build_graph(lines):
    s_l = []
    e = None
    nodes = {}

    char_m = []
    for i, l in enumerate(lines):
        chars = list(l)
        if 'S' in chars:
            chars = [c if c != 'S' else 'a' for c in chars]
        if 'E' in chars:
            e = (i, chars.index('E'))
            chars = [c if c != 'E' else 'z' for c in chars]
        char_m.append([ord(c) for c in chars])

    clen = len(char_m[0])
    rlen = len(char_m)

    for r in range(0, rlen):
        for c in range(0, clen):
            coord = (r, c)
            reachable = []
            # left
            if c - 1 >= 0 and is_reachable(char_m[r][c], char_m[r][c - 1]):
                reachable.append((r, c - 1))
            # right
            if c + 1 < clen and is_reachable(char_m[r][c], char_m[r][c + 1]):
                reachable.append((r, c + 1))
            # up
            if r - 1 >= 0 and is_reachable(char_m[r][c], char_m[r - 1][c]):
                reachable.append((r - 1, c))
                # down
            if r + 1 < rlen and is_reachable(char_m[r][c], char_m[r + 1][c]):
                reachable.append((r + 1, c))

            nodes[coord] = {'is_reached': False, 'path_length': 0, 'reachable': reachable}

            if char_m[r][c] == ord('a'):
                s_l.append((r, c))

    return s_l, e, nodes


def exec():
    with open("input2.txt") as fp:
        lines = [line.strip() for line in fp]

    s_l, e, graph = build_graph(lines)

    min_length = 999999999

    for it, s in enumerate(s_l):

        print(f'It {it}')
        _, e, graph = build_graph(lines)

        q = []
        nxt = s
        count = 0
        while nxt != e:

            #print(f'{count}:{nxt} -> {q}')

            for r in graph[nxt]['reachable']:
                if not graph[r]['is_reached']:
                    q.append(r)
                    graph[r]['path_length'] = graph[nxt]['path_length'] + 1
                    graph[r]['is_reached'] = True

            if len(q) == 0:
                break

            nxt = q[0]
            q = q[1:]
            count += 1

        length = graph[e]['path_length']
        if length < min_length and graph[e]['is_reached']:
            min_length = length

    print(f'Min length: {min_length}')

if __name__ == '__main__':
    exec()
