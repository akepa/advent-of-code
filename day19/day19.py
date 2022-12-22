# ORE - CLAY - OBSIDIAN - GEODE
from operator import add, sub

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

BLUEPRINT_MASKS = [[0], [0], [0, 1], [0, 2]]

MEM = {}


def parse_w_ore(sentence):
    f = sentence.split(" ")
    return [int(f[5]), 0, 0, 0]


def parse_w_ore_clay(sentence):
    f = sentence.split(" ")
    return [int(f[5]), int(f[8]), 0, 0]


def parse_w_ore_obsidian(sentence):
    f = sentence.split(" ")
    return [int(f[5]), 0, int(f[8]), 0]


def parse(line):
    f = line.split(":")[1].split(".")
    return [parse_w_ore(f[0]), parse_w_ore(f[1]), parse_w_ore_clay(f[2]), parse_w_ore_obsidian(f[3])]


def update_resources(robots, resources):
    return list(map(add, robots, resources))


def can_build(mask, blueprint_robot, resources):
    for r in mask:
        if resources[r] < blueprint_robot[r]:
            return False
    return True


def build_state_key(minutes, robots, resources):
    return f'{minutes}-{robots}-{resources}'


def is_needed(i, robots, max_required):
    return i == GEODE or robots[i] < max_required[i]


def estimate(n_robots, n_turns):
    v = 0
    for i in range(1, n_turns // 2 + 1):
        v += n_robots * 2
        n_robots += 1
    if n_turns % 2 == 1:
        v += n_robots
    return v


def can_improve(best, minutes, robots, resources):
    remaining = 24 - minutes
    estim = estimate(robots[GEODE], remaining)
    heuristic = resources[GEODE] + estim
    return heuristic > best


def evaluate(blueprint, robots, resources, minutes, max_required):
    if minutes == 24:
        if resources[GEODE] == 22:
            print(robots)
            print(resources)
        return resources[GEODE]
    key = build_state_key(minutes, robots, resources)
    if key in MEM:
        return MEM[key]
    # print(key)

    updated_resources = update_resources(robots, resources)

    best = 0

    count_can_build = 0
    for i in range(3, -1, -1):
        mask = BLUEPRINT_MASKS[i]
        blueprint_robot = blueprint[i]
        if can_build(mask, blueprint_robot, resources):
            count_can_build += 1
            if is_needed(i, robots, max_required): # and can_improve(best, minutes, robots, updated_resources):
                robots_cpy = robots.copy()
                robots_cpy[i] += 1

                resources_cpy = list(map(sub, updated_resources, blueprint_robot))
                # resources_cpy = resources.copy()
                # for r in mask:
                #    resources_cpy[r] -= blueprint_robot[r]

                candidate = evaluate(blueprint, robots_cpy, resources_cpy, minutes + 1, max_required)
                if candidate > best:
                    best = candidate

    if count_can_build < 4:
        # If we can build all the robots, it makes no sense to do nothing
        noop = evaluate(blueprint, robots.copy(), updated_resources, minutes + 1, max_required)
        if noop > best:
            best = noop

    MEM[key] = best
    return best


def compute_max_required(bp):
    return [max(a, b, c, d) for a, b, c, d in zip(bp[0], bp[1], bp[2], bp[3])]


def exec():
    with open("input2.txt") as fp:
        blueprints = [parse(line.strip()) for line in fp if line.strip()]

    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]

    minutes = 0

    results = []
    for i in range(0, len(blueprints)):
        MEM.clear()
        max_required = compute_max_required(blueprints[i])
        r = evaluate(blueprints[i], robots, resources, minutes, max_required)
        print(f'Blueprint {i+1}: {r} --> {(i+1) * r}')
        results.append((i+1)*r)
    print(f'Total: {sum(results)}')


if __name__ == '__main__':
    exec()
