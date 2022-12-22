FACINGS = [0, 1, 2, 3]
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def parse_path(path_line):
    path_line = path_line + "N"

    p = []

    n = None
    n_start = None
    for i in range(0, len(path_line)):
        if not n:
            if not n_start:
                n_start = [i]
            if i + 1 == len(path_line) or not path_line[i + 1].isdigit():
                n = int(path_line[n_start[0]:i + 1])
        else:
            dir = path_line[i: i + 1]
            dir_number = 1 if dir == "R" else (-1 if dir == "L" else 0)
            p.append((dir_number, n))
            n = None
            n_start = None

    return p


def parse_map(map_lines):
    return [list(l)[:-1] for l in map_lines]


def find_down(map, r, c, num_rows, num_cols):
    for i in range(r + 1, num_rows):
        if map[i][c] == '.' or map[i][c] == '#':
            return (c + 1, i + 1)
    for i in range(0, r + 1):
        if map[i][c] == '.' or map[i][c] == '#':
            return (c + 1, i + 1)
    return None


def find_up(map, r, c, num_rows, num_cols):
    for i in range(r - 1, -1, -1):
        if map[i][c] == '.' or map[i][c] == '#':
            return (c + 1, i + 1)
    for i in range(num_rows - 1, r - 1, -1):
        if map[i][c] == '.' or map[i][c] == '#':
            return (c + 1, i + 1)
    return None


def find_right(map, r, c, num_rows, num_cols):
    for i in range(c + 1, num_cols):
        if map[r][i] == '.' or map[r][i] == '#':
            return (i + 1, r + 1)
    for i in range(0, c + 1):
        if map[r][i] == '.' or map[r][i] == '#':
            return (i + 1, r + 1)
    return None


def find_left(map, r, c, num_rows, num_cols):
    for i in range(c - 1, -1, -1):
        if map[r][i] == '.' or map[r][i] == '#':
            return (i + 1, r + 1)
    for i in range(num_cols - 1, c - 1, -1):
        if map[r][i] == '.' or map[r][i] == '#':
            return (i + 1, r + 1)
    return None


def build_graph(map):
    num_rows = len(map)
    num_cols = len(map[0])

    graph = {}

    for r in range(0, num_rows):
        for c in range(0, num_cols):
            if map[r][c] == '.' or map[r][c] == '#':
                id = (c + 1, r + 1)
                is_wall = map[r][c] == '#'
                left = find_left(map, r, c, num_rows, num_cols)
                right = find_right(map, r, c, num_rows, num_cols)
                up = find_up(map, r, c, num_rows, num_cols)
                down = find_down(map, r, c, num_rows, num_cols)

                graph[id] = {"id": id, "adj": [right, down, left, up], "is_wall": is_wall}

    return graph


def exec():
    with open("input2.txt") as fp:
        lines = [line for line in fp if line.strip()]

    map_lines = lines[:-1]
    path_line = lines[-1]


    path = parse_path(path_line)
    map = parse_map(map_lines)
    graph = build_graph(map)

    pos = list(graph.values())[0]
    facing = RIGHT

    for dir, n in path:
        for i in range(0, n):
            next_id = pos["adj"][facing]
            next_node = graph[next_id]

            if next_node["is_wall"]:
                break
            else:
                pos = next_node
        facing = (facing + dir) % 4


    print(pos)
    print(facing)
    print(1000 * pos['id'][1] + 4 * pos['id'][0] + facing)

if __name__ == '__main__':
    exec()
