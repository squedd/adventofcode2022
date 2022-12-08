file = 'day1.txt'

def process_file(file):
    with open(file) as f:
        output = sorted([sum(map(int, calories.split('\n'))) for calories in f.read().split('\n\n')], reverse=True)
    return output

def part1(file):
    reindeer_calories = process_file(file)
    return reindeer_calories[0]

def part2(file):
    top_three = 3
    reindeer_calories = process_file(file)
    return sum(reindeer_calories[:top_three])

print("Part 1:", part1(file))
print("Part 2:", part2(file))