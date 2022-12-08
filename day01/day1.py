def exec():
    count = 0
    max = 0
    with open("input2.txt") as fp:
        for line in fp:
            if line.strip():
                count = count + int(line)
            else:
                if count > max:
                    max = count
                count = 0
        if count > max:
            max = count
    print(max)


if __name__ == '__main__':
    exec()
