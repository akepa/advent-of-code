def exec():
    with open("input2.txt") as fp:
        numbers = [int(line.strip())*811589153 for line in fp if line.strip()]

    tuples = []
    for i, n in enumerate(numbers):
        tuples.append((n, i))

    original_tuples = tuples.copy()
    l = len(tuples)

    for x in range(0,10):
        for t in original_tuples:
            i = tuples.index(t)

            moves_left = t[0] < 0

            flipped = (moves_left and i + t[0] < 0) or (not moves_left and i + t[0] > l - 1)

            if flipped:
                # times = i + t[0] // l
                if moves_left:
                    new_idx = (i + t[0]) % (l - 1)
                else:
                    new_idx = (i + t[0]) % (l - 1)
            else:
                new_idx = (i + t[0]) % l

            tuples.pop(i)
            tuples.insert(new_idx, t)
            # print("*************")
            # print(f"{t}")
            # print(f"{tuples}")

    zero_idx = tuples.index((0, 3294))  # tuples.index((0,5)) # tuples.index((0,3294)) #
    a = tuples[(zero_idx + 1000) % l][0]
    b = tuples[(zero_idx + 2000) % l][0]
    c = tuples[(zero_idx + 3000) % l][0]

    print(f'{a}/{b}/{c}')
    print(sum([a, b, c]))


if __name__ == '__main__':
    exec()
