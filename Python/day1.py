def process_file(file="../Inputs/day1.txt"):
    with open(file) as f:
        output = sorted([sum(map(int, calories.split('\n'))) for calories in f.read().split('\n\n')], reverse=True)
    return output

def part1():
    reindeer_calories = process_file()
    return reindeer_calories[0]

def part2():
    top_three = 3
    reindeer_calories = process_file()
    return sum(reindeer_calories[:top_three])

def solution():
    print("Day 1: Calorie Counting")
    print("Part 1:", part1())
    print("Part 2:", part2())
    
solution()