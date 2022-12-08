D_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
D_HE_TO_ME = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def is_draw(he, me):
    return he == me


def is_win(he, me):
    return (me == 'X' and he == 'Z') or (me == 'Y' and he == 'X') or (me == 'Z' and he == 'Y')


# R P S
def compute_points(he, me):
    p = D_POINTS[me]
    if is_win(he, me):
        return 6 + p
    elif is_draw(he, me):
        return 3 + p
    else:
        return p

def exec():
    count = 0
    with open("input2.txt") as fp:
        for line in fp:
            if line.strip():
                rnd = line.strip().split(" ")
                count = count + compute_points(D_HE_TO_ME[rnd[0]], rnd[1])
    print(count)


if __name__ == '__main__':
    exec()
