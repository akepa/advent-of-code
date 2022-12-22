from collections import deque


def to_func(op):
    if op == '+':
        return lambda x, y: x + y
    elif op == '*':
        return lambda x, y: x * y
    elif op == '/':
        return lambda x, y: x / y
    elif op == '-':
        return lambda x, y: x - y
    else:
        raise Exception("Unknown")


def to_inv_func_a(op):
    if op == '+':
        return lambda a, r: r - a
    elif op == '*':
        return lambda a, r: r / a
    elif op == '/':
        return lambda a, r: a * r
    elif op == '-':
        return lambda a, r: a - r
    else:
        raise Exception("Unknown")


def to_inv_func_b(op):
    if op == '+':
        return lambda b, r: r - b
    elif op == '*':
        return lambda b, r: r / b
    elif op == '/':
        return lambda b, r: r * b
    elif op == '-':
        return lambda b, r: r + b
    else:
        raise Exception("Unknown")


def parse_line(line):
    f = line.split(":")
    n = f[0]
    op = f[1].strip()
    if " " in op:
        f = op.split(" ")

        return n, {'a': f[0], 'b': f[2], 'op': to_func(f[1]), 'op_inv_a': to_inv_func_a(f[1]),
                   'op_inv_b': to_inv_func_b(f[1])}
    else:
        return n, {'r': int(op)}


def build_dependency_graph(graph):
    solved = deque()
    dependencies = {}

    for k, v in graph.items():
        if "r" in v:
            solved.append(k)
        else:
            d = dependencies.get(v["a"], [])
            d.append(k)
            dependencies[v["a"]] = d

            d = dependencies.get(v["b"], [])
            d.append(k)
            dependencies[v["b"]] = d

    return dependencies, solved


def exec():
    with open("input2.txt") as fp:
        graph = {k: v for k, v in [parse_line(line.strip()) for line in fp if line.strip()]}

    dependencies, solved = build_dependency_graph(graph)

    humn = graph["humn"]
    del humn["r"]
    solved.remove("humn")

    # BOTTOM UP
    while len(solved) > 0:  # "a_r" not in graph["root"] and "b_r" not in graph["root"]:
        nxt = solved.popleft()
        node_nxt = graph[nxt]
        for d in dependencies[nxt]:

            node = graph[d]
            if "a_r" in node:
                node["r"] = node["op"](node["a_r"], node_nxt["r"])
                solved.append(d)
            elif "b_r" in node:
                node["r"] = node["op"](node_nxt["r"], node["b_r"])
                solved.append(d)
            else:
                if nxt == node["a"]:
                    node["a_r"] = node_nxt["r"]
                else:
                    node["b_r"] = node_nxt["r"]

    # TOP DOWN
    solved = deque()

    root = graph["root"]
    if "a_r" in root:
        graph[root["b"]]["r"] = root["a_r"]
        solved.append(root["b"])
    else:
        graph[root["a"]]["r"] = root["b_r"]
        solved.append(root["a"])

    while "r" not in graph["humn"]:
        nxt = solved.popleft()
        node_nxt = graph[nxt]
        if "a_r" in node_nxt:
            res = node_nxt["op_inv_a"](node_nxt["a_r"], node_nxt["r"])
            b = node_nxt["b"]
            graph[b]["r"] = res
            solved.append(b)
        else:
            res = node_nxt["op_inv_b"](node_nxt["b_r"], node_nxt["r"])
            a = node_nxt["a"]
            graph[a]["r"] = res
            solved.append(a)

    print(graph["humn"]["r"])


if __name__ == '__main__':
    exec()
