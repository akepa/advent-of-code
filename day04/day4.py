def parse(line):
    grp = line.split(',')
    return grp[0].split('-'), grp[1].split('-')


def is_subrange(a, b):
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])


def exec():
    count = 0

    with open("input2.txt") as fp:
        for line in fp:
            line = line.strip()
            if line:
                a, b = parse(line)
                if is_subrange(a, b) or is_subrange(b, a):
                    count = count + 1
                    print(f'{a} - {b}')
    print(count)


if __name__ == '__main__':
    exec()
