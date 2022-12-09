def process_file(file='../Inputs/day5.txt'):
    with open(file) as f:
        ship, instructions = f.read().split("\n\n")

        ship = ship.split("\n")[:-1]
        number_of_stacks = ship[-1].count("[")
        stacks = [[] for _ in range(number_of_stacks)]
        for ship_cargo_line in ship:
            for stack_number in range(len(stacks)):
                cargo = ship_cargo_line[stack_number*4+1]
                if cargo.isalpha():
                    stacks[stack_number].append(cargo)
        
        instructions = instructions.split("\n")
        crane_instructions = list()
        for instruction_line in instructions:
            instruction_line_components = instruction_line.split(" ")
            cargo_to_move = int(instruction_line_components[1])
            target_stack = int(instruction_line_components[3])
            destination_stack = int(instruction_line_components[-1])
            crane_instruction = (cargo_to_move, target_stack, destination_stack)
            crane_instructions.append(crane_instruction)
        
        return stacks, crane_instructions

def part1():
    cargo_stacks, crane_instructions = process_file()
    for crane_instruction in crane_instructions:
        cargo_to_move = crane_instruction[0]
        target_stack = cargo_stacks[crane_instruction[1]-1]
        destination_stack = cargo_stacks[crane_instruction[2]-1]
        for cargo_move in range(cargo_to_move):
            destination_stack.insert(0, target_stack.pop(0))
    top_of_each_stack = "".join([stack[0] for stack in cargo_stacks])
    return top_of_each_stack


def part2():
    cargo_stacks, crane_instructions = process_file()
    for crane_instruction in crane_instructions:
        cargo_to_move = crane_instruction[0]
        target_stack_number = crane_instruction[1]-1
        destination_stack_number = crane_instruction[2]-1
        target_stack = cargo_stacks[target_stack_number]
        destination_stack = cargo_stacks[destination_stack_number]
        new_destination_stack = target_stack[:cargo_to_move] + destination_stack
        new_target_stack = target_stack[cargo_to_move:]
        cargo_stacks[target_stack_number] = new_target_stack
        cargo_stacks[destination_stack_number] = new_destination_stack

    top_of_each_stack = "".join([stack[0] for stack in cargo_stacks])
    return top_of_each_stack

def solution():
    print("Part 1:", part1())
    print("Part 2:", part2())

solution()