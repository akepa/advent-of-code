from itertools import chain
MEM = {}

def parse_key_and_weight(l):
    f = l.split(" ")
    k = f[1]
    w = int(f[4].split("=")[1])
    return k, w


def parse_adjacent(l):
    f = l.split(" ")
    a = {}
    for i in f[5:]:
        n = i.replace(",", "")
        w = 1
        a[n] = w
    return a


def parse_line(l):
    f = l.split(";")
    k, w = parse_key_and_weight(f[0])
    a = parse_adjacent(f[1])
    return k, {'w': w, 'a': a}


def to_key(a, b, open_valves):
    try:
        ak = f'{a["n"]}#{a["m"]}'
        bk = f'{b["n"]}#{b["m"]}'
    except:
        print()
    return f'{",".join(sorted([ak, bk]))}-{",".join(sorted(open_valves))}'


def optimise(graph):
    optim = {}
    # Compress graph
    for k, v in graph.items():
        if len(v["a"]) == 2 and v["w"] == 0:
            l = list(v["a"].items())  # n -> w
            adj1 = l[0]
            adj2 = l[1]

            adj1_id = adj1[0]
            adj2_id = adj2[0]
            adj1_w = adj1[1]
            adj2_w = adj2[1]

            d = adj1_w + adj2_w
            graph[adj1_id]["a"][adj2_id] = d
            del graph[adj1_id]["a"][k]
            graph[adj2_id]["a"][adj1_id] = d
            del graph[adj2_id]["a"][k]
            print(f"Removing {k}")
        else:
            optim[k] = v

        # Sort adjacent
    for k, v in optim.items():
        keylist = list(v["a"].keys())
        keylist.sort(key=lambda n: optim[n]["w"], reverse=True)
        new_a = {k: v["a"][k] for k in keylist if k in v["a"]}
        v["a"] = new_a

    return optim


def update_current(d, v):
    return {"n": d, "m": v}


def sort_adjacent(d, open_valves):
    o = []
    c = []
    aa = []
    for k, v in d.items():
        if k in open_valves:
            if k == "AA":
                aa.append((k, v))
            else:
                o.append((k,v))
        else:
            c.append((k, v))

    return chain(c, aa, o)


def find_best(graph, a, b, open_valves, visited):
    if (a["m"] <= 0 and b["m"] <= 0) or len(open_valves) == len(graph):
        return 0

    key = to_key(a, b, open_valves)
    if key in MEM:
        return MEM[key]

    if a["m"] >= b["m"]:
        current = a
        other = b
    else:
        current = b
        other = a

    node = graph[current["n"]]
    visited.append(current["n"])

    best_score = 0
    best_track = []

    if node["w"] == 0:
        open_valves.add(current["n"])
    elif current["n"] not in open_valves:
        open_valves_cpy = open_valves.copy()
        open_valves_cpy.add(current["n"])
        # track_cpy = track.copy()
        # track_cpy.append((m-1, current, node['w']))
        updated = update_current(current["n"], current["m"] - 1)

        score = find_best(graph, updated, other, open_valves_cpy, visited.copy())
        best_score = score + node["w"] * (current["m"] - 1)

    to_open = sum([v["w"] for k, v in graph.items() if k not in open_valves])


    for n, w in sort_adjacent((node['a']), open_valves):
        remaining = current["m"] - w

        if current["m"] >= w and n != other["n"] and remaining * to_open > best_score:
            updated = update_current(n, remaining)
            trial_score = find_best(graph, updated, other, open_valves.copy(), visited.copy())
            if trial_score > best_score:
                best_score = trial_score

    k = to_key(a, b, open_valves)
    #print(f"{k} - {best_score} --> {visited}")
    MEM[k] = best_score
    return best_score


def exec():
    with open("input2.txt") as fp:
        graph = {k: v for k, v in [parse_line(line.strip()) for line in fp if line.strip()]}

    optimised_graph = optimise(graph)
    open_valves = set()
    visited = []
    a = {'n': "AA", 'm': 26}
    b = {'n': "AA", 'm': 26}

    max_per_turn = sum([v["w"] for v in optimised_graph.values()])
    r = find_best(optimised_graph, a, b, open_valves, visited)
    print(r)


# ORDENAR DE MENOR A MAYOR LOS NODOS POR PESO
if __name__ == '__main__':
    exec()
