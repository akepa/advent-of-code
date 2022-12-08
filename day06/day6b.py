

def exec():
    with open("input_long.txt") as fp:
        line = fp.readline()
        for i in range(14, len(line)):
            token = line[i-14: i]
            s = set(list(token))
            if len(s) == 14:
                print(i)
                print(token)
                break


if __name__ == '__main__':
    exec()

