def parse(line):
    grp = line.split(',')
    return grp[0].split('-'), grp[1].split('-')


def does_not_overlap(a, b):
    return int(a[0]) > int(b[1]) or int(a[1]) < int(b[0])


def exec():
    count = 0

    with open("input2.txt") as fp:
        for line in fp:
            line = line.strip()
            if line:
                a, b = parse(line)
                if not does_not_overlap(a, b):
                    count = count + 1
                    print(f'{a} - {b}')
    print(count)


if __name__ == '__main__':
    exec()
