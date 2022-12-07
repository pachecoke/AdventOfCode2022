import sys


def move_crate(from_stack, to_stack):
    crate = from_stack.pop()
    to_stack.append(crate)
    return from_stack, to_stack


def move_crates(from_stack, to_stack, n_crates):
    for _ in range(n_crates):
        from_stack, to_stack = move_crate(from_stack, to_stack)
    return from_stack, to_stack


def move_crates_multiple(from_stack, to_stack, n_crates):
    crates_to_move = []
    for _ in range(n_crates):
        crates_to_move.append(from_stack.pop())
    crates_to_move.reverse()
    to_stack.extend(crates_to_move)
    return from_stack, to_stack


def parse_stacks_to_lines(text):
    stack_lines = text.split("\n")
    return stack_lines


def remove_number_line(stack_lines):
    stack_lines.pop()
    return stack_lines


def get_stack_count(stack_lines):
    return (len(stack_lines[0]) + 1) / 4


def transpose_stack_lines(stack_lines):
    horizontal_stacks = []
    for line in stack_lines:
        horizontal_stack = []
        for i in range(0, len(line), 4):
            horizontal_stack.append(line[i:i+4].strip())
        horizontal_stacks.append(horizontal_stack)

    transposed = []
    for i in range(len(horizontal_stacks[0])):
        stack = []
        for j in range(len(horizontal_stacks)):
            if horizontal_stacks[j][i] != '':
                stack.append(horizontal_stacks[j][i])
        stack.reverse()
        transposed.append(stack)

    return transposed


def parse_move_command(command):
    command_pieces = command.split(" ")
    new_command = []
    new_command.append(int(command_pieces[1]))
    new_command.append(int(command_pieces[3]))
    new_command.append(int(command_pieces[5]))
    return new_command


def apply_move(move, stacks):
    n_crates = move[0]
    from_stack_index = move[1] - 1
    to_stack_index = move[2] - 1
    from_stack, to_stack = move_crates(stacks[from_stack_index], stacks[to_stack_index], n_crates)
    stacks[from_stack_index] = from_stack
    stacks[to_stack_index] = to_stack
    return stacks


def apply_moves(moves, stacks):
    for move in moves:
        stacks = apply_move(move, stacks)
    return stacks


def apply_move_multiple(move, stacks):
    n_crates = move[0]
    from_stack_index = move[1] - 1
    to_stack_index = move[2] - 1
    from_stack, to_stack = move_crates_multiple(stacks[from_stack_index], stacks[to_stack_index], n_crates)
    stacks[from_stack_index] = from_stack
    stacks[to_stack_index] = to_stack
    return stacks


def apply_moves_multiple(moves, stacks):
    for move in moves:
        stacks = apply_move_multiple(move, stacks)
    return stacks


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def split_input(text):
    return text.split("\n\n")


def parse_moves(move_lines):
    return move_lines.strip().split("\n")


def get_top_crate(stack):
    return stack[-1]


def get_crate_name(crate):
    return crate[1:2]


def get_top_crates(stacks):
    top_crate_names = []
    for stack in stacks:
        top_crate = get_top_crate(stack)
        top_crate_names.append(get_crate_name(top_crate))
    return ''.join(top_crate_names)


def solve_puzzle_part_1(input_file_name):
    text = read_input(input_file_name)
    stack_text, move_text = split_input(text)
    stack_lines = parse_stacks_to_lines(stack_text)
    stack_lines = remove_number_line(stack_lines)
    stacks = transpose_stack_lines(stack_lines)
    move_lines = parse_moves(move_text)
    moves = [parse_move_command(move_line) for move_line in move_lines]
    stacks = apply_moves(moves, stacks)
    return get_top_crates(stacks)


def solve_puzzle_part_2(input_file_name):
    text = read_input(input_file_name)
    stack_text, move_text = split_input(text)
    stack_lines = parse_stacks_to_lines(stack_text)
    stack_lines = remove_number_line(stack_lines)
    stacks = transpose_stack_lines(stack_lines)
    move_lines = parse_moves(move_text)
    moves = [parse_move_command(move_line) for move_line in move_lines]
    stacks = apply_moves_multiple(moves, stacks)
    return get_top_crates(stacks)


if __name__ == "__main__":
    file_input = sys.argv[1]
    top_crates = solve_puzzle_part_1(file_input)
    print(top_crates)
    top_crates = solve_puzzle_part_2(file_input)
    print(top_crates)
