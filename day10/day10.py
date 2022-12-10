def parse(line):
    f = line.split(" ")
    return f if len(f) == 1 else (f[0], int(f[1]))


def exec():
    with open("input2.txt") as fp:
        intructions = [parse(line.strip()) for line in fp]

    p = 1
    x = 1
    c = 1
    trackable = list(reversed([20, 60, 100, 140, 180, 220]))
    r = {}

    for i in intructions:
        if len(trackable) > 0 and c == trackable[-1]:
            r[trackable[-1]] = x
            trackable.pop()
        if len(trackable) > 0 and c > trackable[-1]:
            r[trackable[-1]] = p
            trackable.pop()

        c = c + len(i)
        if len(i) > 1:  # addx
            p = x
            x = x + i[1]
        #print(f'{c} - {x}')

    print(r)
    count = 0
    for k,v in r.items():
        count = count + k*v
    print(count)


if __name__ == '__main__':
    exec()
