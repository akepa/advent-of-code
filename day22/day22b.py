FACINGS = [0, 1, 2, 3]
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

N = 50

ADJ = {
    '1': [None, None, ('5', LEFT), ('6', LEFT)],
    '2': [('4', RIGHT), ('3', RIGHT), None, ('6', DOWN)],
    '3': [('2', DOWN), None, ('5', UP), None],
    '4': [('2', RIGHT), ('6', RIGHT), None, None],
    '5': [None, None, ('1', LEFT), ('3', LEFT)],
    '6': [('4', DOWN), ('2', UP), ('1', UP), None],
}

MAPPING_FUNCS = {
    RIGHT: {
        RIGHT: lambda x, y: (N - 1, N - y - 1),
        DOWN: lambda x, y: (y, N - 1)
    },
    DOWN: {
        RIGHT: lambda x, y: (N - 1, x),
        UP: lambda x, y: (x, 0),
    },
    LEFT: {
        LEFT: lambda x, y: (0, N - y - 1),
        UP: lambda x, y: (y, 0),
    },
    UP: {
        LEFT: lambda x, y: (0, x),
        DOWN: lambda x, y: (x, N - 1),
    },
}


def opposite(enter_side):
    if enter_side == LEFT:
        return RIGHT
    elif enter_side == RIGHT:
        return LEFT
    elif enter_side == UP:
        return DOWN
    else:
        return UP


def map_next_coordinate(node, dir, map_by_col):
    colour = node["colour"]
    x = node["x"]
    y = node["y"]
    try:
        next_col, enter_side = ADJ[colour][dir]
        new_dir = opposite(enter_side)

        new_x, new_y = MAPPING_FUNCS[dir][enter_side](x, y)

        new_coords = map_by_col[next_col][new_y][new_x]

        return new_coords, new_dir
    except:
        print()


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


def find_down(map, r, c, num_rows, map_by_col, node):
    for i in range(r + 1, num_rows):
        if map[i][c] == '.' or map[i][c] == '#':
            return (c + 1, i + 1), DOWN

    new_coords, new_dir = map_next_coordinate(node, DOWN, map_by_col)

    return new_coords, new_dir


def find_up(map, r, c, num_rows, map_by_col, node):
    for i in range(r - 1, -1, -1):
        if map[i][c] == '.' or map[i][c] == '#':
            return (c + 1, i + 1), UP
    new_coords, new_dir = map_next_coordinate(node, UP, map_by_col)

    return new_coords, new_dir


def find_right(map, r, c, num_cols, map_by_col, node):
    for i in range(c + 1, num_cols):
        if map[r][i] == '.' or map[r][i] == '#':
            return (i + 1, r + 1), RIGHT
    new_coords, new_dir = map_next_coordinate(node, RIGHT, map_by_col)

    return new_coords, new_dir


def find_left(map, r, c, num_cols, map_by_col, node):
    for i in range(c - 1, -1, -1):
        if map[r][i] == '.' or map[r][i] == '#':
            return (i + 1, r + 1), LEFT
    new_coords, new_dir = map_next_coordinate(node, LEFT, map_by_col)

    return new_coords, new_dir


def to_map_by_col(coords_by_col, graph):
    map_by_col = {}
    for col, coords in coords_by_col.items():
        m = []
        count = 0

        for r in range(0, N):
            row = []
            m.append(row)
            for c in range(0, N):
                coord_item = coords[count]
                node = graph[coord_item]

                node["x"] = c
                node["y"] = r

                row.append(coord_item)
                count += 1
        map_by_col[col] = m
    return map_by_col


def build_graph(map, colmap):
    num_rows = len(map)
    num_cols = len(map[0])

    graph = {}
    coords_by_col = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': []}
    for r in range(0, num_rows):
        for c in range(0, num_cols):
            if map[r][c] == '.' or map[r][c] == '#':
                colour = colmap[r][c]

                id = (c + 1, r + 1)
                is_wall = map[r][c] == '#'
                graph[id] = {"id": id, "is_wall": is_wall, "colour": colour}
                coords_by_col[colour].append(id)

    map_by_col = to_map_by_col(coords_by_col, graph)

    for r in range(0, num_rows):
        for c in range(0, num_cols):
            if map[r][c] == '.' or map[r][c] == '#':
                id = (c + 1, r + 1)
                node = graph[id]

                left = find_left(map, r, c, num_cols, map_by_col, node)
                right = find_right(map, r, c, num_cols, map_by_col, node)
                up = find_up(map, r, c, num_rows, map_by_col, node)
                down = find_down(map, r, c, num_rows, map_by_col, node)

                node["adj"] = [right, down, left, up]

    return graph


def exec():
    with open("input2.txt") as fp:
        lines = [line for line in fp if line.strip()]
    with open("input2col.txt") as fp:
        colours = [line for line in fp if line.strip()]

    map_lines = lines[:-1]
    path_line = lines[-1]

    path = parse_path(path_line)
    map = parse_map(map_lines)
    colmap = parse_map(colours)

    graph = build_graph(map, colmap)

    pos = list(graph.values())[0]
    facing = RIGHT

    for dir, n in path:
        for i in range(0, n):
            next_id, next_facing = pos["adj"][facing]
            next_node = graph[next_id]

            if next_node["is_wall"]:
                break
            else:
                pos = next_node
                facing = next_facing
        facing = (facing + dir) % 4

    print(pos)
    print(facing)
    print(1000 * pos['id'][1] + 4 * pos['id'][0] + facing)


if __name__ == '__main__':
    exec()
