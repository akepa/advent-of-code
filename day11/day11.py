def parse(line):
    f = line.split(" ")
    return f if len(f) == 1 else (f[0], int(f[1]))


def parse_items(items_l):
    f = items_l.split(":")
    return [int(i) for i in f[1].split(",")]


def parse_operation_function(operation_l):
    f = operation_l.split("=")
    g = f[1].split(" ")

    if g[-1].isdigit():
        if g[-2] == '+':
            return lambda x: (x + int(g[-1])) // 3
        else:
            return lambda x: (x * int(g[-1])) // 3
    else:
        if g[-2] == '+':
            return lambda x: (x + x) // 3
        else:
            return lambda x: (x * x) // 3


def parse_test_function(test_cond, true_cond, false_cond):
    cond_num = int(test_cond.split(" ")[-1])
    true_cond_num = int(true_cond.split(" ")[-1])
    false_cond_num = int(false_cond.split(" ")[-1])
    return lambda x: true_cond_num if x % cond_num == 0 else false_cond_num


def exec():
    with open("input2.txt") as fp:
        lines = [l.strip() for l in fp if l.strip()]

    # Parse input
    items = []
    test = []
    op = []

    for start_line in range(0, len(lines), 6):
        items.append(parse_items(lines[start_line + 1]))
        op.append(parse_operation_function(lines[start_line + 2]))
        test.append(parse_test_function(lines[start_line + 3], lines[start_line + 4], lines[start_line + 5]))

    num_monkeys = len(items)

    # Process input
    items_processed = [0 for i in range(0, num_monkeys)]

    for rnd in range(0, 20):
        for m in range(0, num_monkeys):
            items_processed[m] = items_processed[m] + len(items[m])
            for i in items[m]:
                worry_lvl = op[m](i)
                dest_monkey = test[m](worry_lvl)
                items[dest_monkey].append(worry_lvl)
            items[m] = []

        # print(f'Round {rnd + 1}: {items}')

    print(items_processed)

    s = sorted(items_processed)

    print(s[-1] * s[-2])


if __name__ == '__main__':
    exec()
