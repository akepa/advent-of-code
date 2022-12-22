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


def to_key(m, current, open_valves):
    return f'{m}-{current}-{",".join(sorted(open_valves))}'
    #return f'{m}-{current}-{",".join(sorted(open_valves))}'


def optimise(graph):

    optim = {}
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
    return optim


def find_best(graph, current, open_valves, visited, m, track):
    if m <= 0 or len(open_valves) == len(graph):
        return 0, track

    key = to_key(m, current, open_valves)
    if key in MEM:
        return MEM[key]

    node = graph[current]

    visited.append(current)

    best_score = 0
    best_track = []

    if node["w"] == 0:
        open_valves.add(current)
    elif current not in open_valves:
        open_valves_cpy = open_valves.copy()
        open_valves_cpy.add(current)
        track_cpy = track.copy()
        track_cpy.append((m-1, current, node['w']))
        score, best_track = find_best(graph, current, open_valves_cpy, visited.copy(), m - 1, track_cpy)
        best_score = score + node["w"] * (m - 1)

    for n,w in node['a'].items():
        if m >= w:
            trial_score, trial_track = find_best(graph, n, open_valves.copy(), visited.copy(), m - w, track)
            if trial_score > best_score:
                best_score = trial_score
                best_track = trial_track

    k = to_key(m, current, open_valves)
    print(f"{k} - {best_score} --> {visited}")
    MEM[k] = (best_score, best_track)
    return best_score, best_track



def exec():
    with open("input2.txt") as fp:
        graph = {k: v for k, v in [parse_line(line.strip()) for line in fp if line.strip()]}

    optimised_graph = optimise(graph)
    m = 30
    open_valves = set()
    visited = []
    current = "AA"
    r, t = find_best(optimised_graph, current, open_valves, visited, m, [])
    print(r)
    print(t)


if __name__ == '__main__':
    exec()
