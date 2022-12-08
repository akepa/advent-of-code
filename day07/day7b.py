def to_path(cursor):
    return '/'.join(cursor)


def get_chd_cursor(cursor, node):
    cpy = cursor.copy()
    cpy.append(node)
    return cpy


def find_total_sizes(total_sizes, fs, cursor):
    path = to_path(cursor)
    if path in total_sizes:
        return total_sizes[path]

    chd_sizes = sum([find_total_sizes(total_sizes, fs, c) for c in fs[path]['chd']])
    total_sizes[path] = fs[path].get('fs', 0) + chd_sizes
    return total_sizes[path]


def exec():
    with open("input2.txt") as fp:
        lines = [line.rstrip() for line in fp]

    fs = {}
    cursor = []

    for i, l in enumerate(lines):
        if l.startswith('$'):
            tokens = l.split(' ')
            if tokens[1] == 'cd':
                if tokens[2] == '/':
                    cursor = ['/']
                elif tokens[2] == '..':
                    cursor = cursor[:-1]
                else:
                    cursor.append(tokens[2])
            elif tokens[1] == 'ls':
                files_size = 0
                children = []
                for j in lines[i + 1:]:
                    if j.startswith('$'):
                        break
                    tokens = j.split(' ')
                    if tokens[0].isdigit():
                        # Is file
                        files_size = files_size + int(tokens[0])
                    else:
                        # Is directory
                        children.append(get_chd_cursor(cursor, tokens[1]))
                fs[to_path(cursor)] = {'fs': files_size, 'chd': children}

            else:
                raise Exception("Algo raro ha pasado")

    ## Compute total size
    total_sizes = {}
    find_total_sizes(total_sizes, fs, ['/'])
    print(total_sizes)

    # Compute result
    unused_space = 70000000 - total_sizes['/']
    missing_space = 30000000 - unused_space
    best_candidate = total_sizes['/']
    for v in total_sizes.values():
        if v > missing_space and v < best_candidate:
            best_candidate = v
    print(best_candidate)


if __name__ == '__main__':
    exec()
