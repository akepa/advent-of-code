def parse(line):
    f = line.split(" ")
    return f if len(f) == 1 else (f[0], int(f[1]))


def exec():
    with open("input2.txt") as fp:
        intructions = list(reversed([parse(line.strip()) for line in fp]))

    r = 1
    t = 0
    i = ()

    for y in range(0, 6):
        for x in range(0, 40):
            c = y*40+x + 1

            if t == 0:
                if len(i) == 2:
                    r = r + i[1]
                i = intructions.pop()
                t = len(i)
            t = t - 1

            if r-1 <= x <= r+1:
                print("#", end='')
            else:
                print(".", end='')


            #print(f'{c} - {r}')
        print("")

if __name__ == '__main__':
    exec()
