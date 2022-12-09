def process_file(file="../Inputs/day6.txt"):
    with open(file) as f:
        data_stream = f.read().strip()
        return data_stream

def find_start_of_packet(distinct_chars):
    data_stream = process_file()
    for first_marker, char in enumerate(range(len(data_stream)-distinct_chars)):
        message_to_check = data_stream[first_marker:first_marker+distinct_chars]
        if len(set(message_to_check)) == distinct_chars:
            return first_marker + distinct_chars
    return -1

def part1():
    return find_start_of_packet(4)

def part2():
    return find_start_of_packet(14)

def solution():
    print("Part 1:", part1())
    print("Part 2:", part2())

solution()