def try_add(l, count):
    if count > l[0]:
        l[0] = count
    return sorted(l)


def exec():
    count = 0
    l = []
    with open("input2.txt") as fp:
        for line in fp:
            if line.strip():
                count = count + int(line)
            else:
                if len(l) < 3:
                    l.append(count)
                    l = sorted(l)
                else:
                    l = try_add(l, count)
                count = 0
                print(l)
        l = try_add(l, count)
    print(sum(l))


if __name__ == '__main__':
    exec()
