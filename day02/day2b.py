D_POINTS_RESULT = {'X': 0, 'Y': 3, 'Z': 6}
D_POINTS_ME = {'A': 1, 'B': 2, 'C': 3}

# R P S
D_WIN = {'A': 'B', 'B': 'C', 'C': 'A'}
D_LOSS = {'A': 'C', 'B': 'A', 'C': 'B'}
D_DRAW = {'A': 'A', 'B': 'B', 'C': 'C'}

D_RESULT = {'X': D_LOSS, 'Y': D_DRAW, 'Z': D_WIN}


def compute_points(he, result):
    p =  D_POINTS_RESULT[result] + D_POINTS_ME[D_RESULT[result][he]]
    return p

def exec():
    count = 0
    with open("input2.txt") as fp:
        for line in fp:
            if line.strip():
                rnd = line.strip().split(" ")
                count = count + compute_points(rnd[0], rnd[1])
    print(count)


if __name__ == '__main__':
    exec()
