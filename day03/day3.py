import string


def to_set(str):
    return {c for c in str}


def build_priorities():
    a = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
    b = {c: i + 27 for i, c in enumerate(string.ascii_uppercase)}
    return a | b


def exec():
    props_d = build_priorities()
    score = 0

    with open("input2.txt") as fp:
        for line in fp:
            line = line.strip()
            if line:
                s = len(line) // 2
                # print(line)
                a = to_set(line[:s])
                b = to_set(line[s:])
                common = a.intersection(b).pop()
                score = score + props_d[common]
    print(score)

if __name__ == '__main__':
    exec()
