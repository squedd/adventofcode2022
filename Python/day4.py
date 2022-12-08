def process_file(file='day4.txt'):
    assignment_pairs = list()
    for line in open(file):
        section_ids_1, section_ids_2 = line.strip().split(",")
        section_ids_1 = [int(_) for _ in section_ids_1.split("-")]
        section_ids_1 = range(section_ids_1[0], section_ids_1[1] + 1)
        section_ids_2 = [int(_) for _ in section_ids_2.split("-")]
        section_ids_2 = range(section_ids_2[0], section_ids_2[1] + 1)
        assignment_pairs.append([set(section_ids_1), set(section_ids_2)])

    return assignment_pairs


def part1():
    fully_contained_pairs = 0
    for ids_1, ids_2 in process_file():
        if len(ids_1) < len(ids_2):
            ids_1, ids_2 = ids_2, ids_1
        if len(ids_1.union(ids_2)) == len(ids_1):
            fully_contained_pairs += 1
    
    return fully_contained_pairs

def part2():
    overlapped_pairs = 0
    for ids_1, ids_2 in process_file():
        if len(ids_1.intersection(ids_2)) > 0:
            overlapped_pairs += 1
    
    return overlapped_pairs

def solution():
    print("Part 1:", part1())
    print("Part 2:", part2())

solution()