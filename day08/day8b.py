def score_l(h, i, j, matrix):
    count = 0
    for x in reversed(range(0, i)):
        count = count + 1
        if matrix[x][j] >= h:
            break
    return count


def score_d(h, i, j, matrix, ysize):
    count = 0
    for x in range(j + 1, ysize):
        count = count + 1
        if matrix[i][x] >= h:
            break
    return count


def score_u(h, i, j, matrix):
    count = 0
    for x in reversed(range(0, j)):
        count = count + 1
        if matrix[i][x] >= h:
            break
    return count


def score_r(h, i, j, matrix, xsize):
    count = 0
    for x in range(i + 1, xsize):
        count = count + 1
        if matrix[x][j] >= h:
            break
    return count


def score(i, j, h, matrix, track=False):
    xsize = len(matrix)
    ysize = len(matrix[0])

    l = score_l(h, i, j, matrix)
    r = score_r(h, i, j, matrix, xsize)
    u = score_u(h, i, j, matrix)
    d = score_d(h, i, j, matrix, ysize)
    if track:
        print(f'{l} {r} {u} {d}')

    return l*r*u*d


def exec():
    with open("input2.txt") as fp:
        matrix = [[int(i) for i in list(line.strip())] for line in fp]

    max_score = 0

    xsize = len(matrix)
    ysize = len(matrix[0])

    for i in range(1, xsize - 1):
        for j in range(1, ysize - 1):
            h = matrix[i][j]
            s = score(i, j, h, matrix)
            if s > max_score:
                print(f'{i} - {j} - {h}')
                score(i, j, h, matrix, True)
                max_score = s

    print(max_score)


if __name__ == '__main__':
    exec()
