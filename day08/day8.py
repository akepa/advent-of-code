def is_visible_l(h, i, j, matrix):
    for x in range(0, i):
        if matrix[x][j] >= h:
            return False
    return True


def is_visible_d(h, i, j, matrix, ysize):
    for x in range(j + 1, ysize):
        if matrix[i][x] >= h:
            return False
    return True


def is_visible_u(h, i, j, matrix):
    for x in range(0, j):
        if matrix[i][x] >= h:
            return False
    return True


def is_visible_r(h, i, j, matrix, xsize):
    for x in range(i + 1, xsize):
        if matrix[x][j] >= h:
            return False
    return True


def is_visible(i, j, h, matrix):
    xsize = len(matrix)
    ysize = len(matrix[0])

    return is_visible_l(h, i, j, matrix) or \
        is_visible_r(h, i, j, matrix, xsize) or \
        is_visible_u(h, i, j, matrix) or \
        is_visible_d(h, i, j, matrix, ysize)


def exec():
    with open("input2.txt") as fp:
        matrix = [[int(i) for i in list(line.strip())] for line in fp]

    count = 0

    xsize = len(matrix)
    ysize = len(matrix[0])

    for i in range(1, xsize - 1):
        for j in range(1, ysize - 1):
            h = matrix[i][j]
            if is_visible(i, j, h, matrix):
                count = count + 1

    print(count + 2 * xsize + 2 * ysize - 4)


if __name__ == '__main__':
    exec()
