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


def merge_sort(lines):
    if len(lines) > 1:
        mid = len(lines) // 2
        l = lines[:mid]
        r = lines[mid:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            is_ord = is_right_order(l[i], r[j])
            if is_ord == 'T':
                lines[k] = l[i]
                i += 1
            elif is_ord == 'F':
                lines[k] = r[j]
                j += 1
            else:
                raise Exception("Boom")
            k += 1
        while i < len(l):
            lines[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            lines[k] = r[j]
            j += 1
            k += 1

def exec():
    with open("input2.txt") as fp:
        lines = [literal_eval(line.strip()) for line in fp if line.strip()]

    lines.append([2])
    lines.append([6])

    merge_sort(lines)

    i = lines.index([2]) + 1
    j = lines.index([6]) + 1

    print(lines)
    print(i * j)


if __name__ == '__main__':
    exec()
