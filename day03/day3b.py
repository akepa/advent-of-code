import string


def build_priorities():
    a = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
    b = {c: i + 27 for i, c in enumerate(string.ascii_uppercase)}
    return a | b


def to_set(str):
    return {c for c in str}


def process(group, props_d):
    item = to_set(group[0]).intersection(to_set(group[1])).intersection(to_set(group[2])).pop()
    return props_d[item]


def exec():
    props_d = build_priorities()
    score = 0
    group = []

    with open("input2.txt") as fp:
        for line in fp:
            line = line.strip()
            if line:
                group.append(line)
                if len(group) == 3:
                    score = score + process(group, props_d)
                    group = []
    print(score)


if __name__ == '__main__':
    exec()
