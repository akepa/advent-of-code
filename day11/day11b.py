from sympy.ntheory import factorint
import time
MEM = {}


def parse(line):
    f = line.split(" ")
    return f if len(f) == 1 else (f[0], int(f[1]))


def find_prime_factors(n):
    if n in MEM:
        return MEM[n]
    orig = n
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            u = factors.get(i,0)
            factors[i] = u+1
            n //= i
            if n in MEM:
                m = MEM[n]
                merged = merge_prime_factors(factors, m)
                MEM[orig] = merged
                return merged
    if n > 1:
        u = factors.get(n, 0)
        factors[n] = u + 1

    MEM[orig] = factors
    return factors


def to_prime_factors(number):
   return find_prime_factors(number)

def to_number(prime_factor_d):
    n = 1
    for k, v in prime_factor_d.items():
        n = n * pow(k, v)
    return n


def parse_items(items_l):
    f = items_l.split(":")
    return [to_prime_factors(int(i)) for i in f[1].split(",")]


def merge_prime_factors(pf1, pf2):
    for k, v in pf2.items():
        p = pf1.get(k, 0)
        pf1[k] = p + v
    return pf1


def dupe_prime_factors(pf):
    return {k: 2 * v for k, v in pf.items()}


def apply_sum(pf, n):
    last_key = list(pf)[-1]
    last_value = pf[last_key]
    if last_value == 1:
        del pf[last_key]
    else:
        pf[last_key] = last_value - 1
    return merge_prime_factors(pf, to_prime_factors(last_key + n))


def parse_operation_function(operation_l):
    f = operation_l.split("=")
    g = f[1].split(" ")

    if g[-1].isdigit():
        n = int(g[-1])
        if g[-2] == '+':
            return lambda x: to_prime_factors(to_number(x) + n)
        else:
            return lambda x: merge_prime_factors(x, to_prime_factors(n))
    else:
        #if g[-2] == '+':
        #    return lambda x: dupe_sum(x)
        #else:
        # No existe la suma
        return lambda x: dupe_prime_factors(x)


def parse_test_function(test_cond, true_cond, false_cond):
    cond_num = int(test_cond.split(" ")[-1])
    true_cond_num = int(true_cond.split(" ")[-1])
    false_cond_num = int(false_cond.split(" ")[-1])
    return lambda prime_factor_d: true_cond_num if cond_num in prime_factor_d else false_cond_num


def exec():
    with open("input1.txt") as fp:
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

    for rnd in range(0, 10000):
        for m in range(0, num_monkeys):
            items_processed[m] = items_processed[m] + len(items[m])
            for i in items[m]:
                worry_lvl_pf = op[m](i)
                dest_monkey = test[m](worry_lvl_pf)
                items[dest_monkey].append(worry_lvl_pf)
            items[m] = []

        print(f'Round {rnd + 1} - {items_processed}')

    print(items_processed)

    s = sorted(items_processed)

    print(s[-1] * s[-2])


if __name__ == '__main__':
    exec()
