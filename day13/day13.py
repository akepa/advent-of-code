from ast import literal_eval


def is_right_order(a, b):
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]

    min_len = min(len(a), len(b))

    for i in range(0, min_len):
        if isinstance(a[i], list) or isinstance(b[i], list):
            r = is_right_order(a[i], b[i])
            if r != 'U':
                return r
        else:
            if a[i] < b[i]:
                return "T"
            elif a[i] > b[i]:
                return "F"
    if len(a) < len(b):
        return "T"
    elif len(a) > len(b):
        return "F"
    else:
        return "U"


def exec():
    with open("input2.txt") as fp:
        lines = [literal_eval(line.strip()) for line in fp if line.strip()]

    right_order_indexes = []
    input_idx = 1
    for i in range(0, len(lines), 2):
        a = lines[i]
        b = lines[i + 1]

        if is_right_order(a, b) == "T":
            right_order_indexes.append(input_idx)
        input_idx += 1
    print(right_order_indexes)
    print(sum(right_order_indexes))

if __name__ == '__main__':
    exec()
