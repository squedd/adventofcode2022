def process_file(file="../Inputs/day2.txt"):
    with open(file) as f:
        output = [game.split() for game in f.read().split('\n')]
        return output

def part1():
    WIN, DRAW, LOSS = 6, 3, 0
    P1_CODES, P2_CODES = ['A', 'B', 'C'], ['X', 'Y', 'Z']
    P1_WIN_CONDITIONS = ['Z', 'X', 'Y']
    P2_WIN_CONDITIONS = ['C', 'A', 'B']

    games = process_file()
    points = 0
    for p1, p2 in games:
        if p1 in P1_CODES and p2 in P2_CODES:
            if P2_WIN_CONDITIONS[P2_CODES.index(p2)] == p1:
                points += WIN
            elif P1_WIN_CONDITIONS[P1_CODES.index(p1)] == p2:
                points += LOSS
            else:
                points += DRAW
            points += P2_CODES.index(p2) + 1

    return points

def part2():
    CODES = ['A', 'B', 'C']
    CONDITION_CODES = ['X', 'Y', 'Z']
    CONDITIONS = {'A': ['C', 'A', 'B'], 'B': ['A', 'B', 'C'], 'C': ['B', 'C', 'A']}

    games = process_file()
    points = 0
    for p1_shape, condition in games:
        conditions = CONDITIONS[p1_shape]
        condition_index = CONDITION_CODES.index(condition)
        chosen_shape = conditions[condition_index]
        points += CODES.index(chosen_shape) + 1
        points += (condition_index * 3)

    return points
    
def solution():
    print("Day 2: Rock Paper Scissors")
    print("Part 1:", part1())
    print("Part 2:", part2())
    
solution()