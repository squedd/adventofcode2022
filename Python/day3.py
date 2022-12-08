import string
priority_values = " " + string.ascii_lowercase + string.ascii_uppercase

def process_file(file='day3.txt'):
    return [line.strip() for line in open(file)]


def part1():
    priorities_sum = 0

    for rucksack in process_file():
        number_of_compartments = len(rucksack) // 2
        compartment_one, compartment_two = rucksack[:number_of_compartments], rucksack[number_of_compartments:]
        compartment_one, compartment_two = set(compartment_one), set(compartment_two)
        common_item = compartment_one.intersection(compartment_two).pop()
        priorities_sum += priority_values.index(common_item)
  
    return priorities_sum

def part2():
    group_size = 3
    rucksacks = process_file()

    priorities_sum = 0
    for rucksack_group_index in range(0, len(rucksacks), group_size):
        rucksack_group = [set(rucksack) for rucksack in rucksacks[rucksack_group_index:rucksack_group_index+group_size]]
        item_in_all_rucksacks = set.intersection(*rucksack_group).pop()
        priorities_sum += priority_values.index(item_in_all_rucksacks)
        
    return priorities_sum


def solution():
    print("Part 1:", part1())
    print("Part 2:", part2())

solution()