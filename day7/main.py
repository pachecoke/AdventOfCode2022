import sys
from node import Node


def build_graph(terminal_output):
    current_parent = None
    root_node = None
    for line in terminal_output:
        if line == "$ cd /":
            root_node = Node('/')
            current_parent = root_node
        elif line[:4] == "$ ls":
            continue
        elif line[:3] == "dir":
            directory = line[4:]
            node = Node(directory)
            node.parent = current_parent
            current_parent.add_child(node)
        elif line == "$ cd ..":
            current_parent = current_parent.parent
        elif line[:4] == "$ cd":
            for child in current_parent.children:
                if child.label == line[5:]:
                    current_parent = child
                    break
        else:
            current_parent.add_leaf(line)
    return root_node


def get_file_size_sum(graph, at_most_size, dirs):
    file_sizes = []
    for directory in dirs:
        files = graph.get_all_leaf_nodes(directory, [])
        for file in files:
            file_size = get_file_size(file)
            if file_size <= at_most_size:
                file_sizes.append(file_size)
    return sum(file_sizes)


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def get_terminal_output(input):
    return input.strip().split("\n")


def get_file_size(file_data):
    size, _ = file_data.split(' ')
    return int(size)


def get_leaf_nodes(root_node, leaf_nodes):
    leaf_nodes.extend(root_node.leaves)
    for child in root_node.children:
        get_leaf_nodes(child, leaf_nodes)
    return leaf_nodes


def get_directory_size(root_node):
    files = get_leaf_nodes(root_node, [])
    return sum([get_file_size(file) for file in files])


def get_at_most_directory_sizes(root_node, at_most_size, dir_sizes):
    size = get_directory_size(root_node)
    if size <= at_most_size:
        dir_sizes.append((root_node.label, size))

    for child in root_node.children:
        get_at_most_directory_sizes(child, at_most_size, dir_sizes)

    return dir_sizes


def get_at_least_directory_sizes(root_node, at_least_size, dir_sizes):
    size = get_directory_size(root_node)
    if size >= at_least_size:
        dir_sizes.append((root_node.label, size))

    for child in root_node.children:
        get_at_least_directory_sizes(child, at_least_size, dir_sizes)

    return dir_sizes


def get_sum_sizes(directory_sizes):
    return sum([value[1] for value in directory_sizes])


def get_smallest_directory(directory_sizes):
    return min(directory_sizes, key=lambda t: t[1])[1]


def solve_puzzle_part_1(file_input):
    text = read_input(file_input)
    output = get_terminal_output(text)
    root_node = build_graph(output)
    sizes = get_at_most_directory_sizes(root_node, 100000, [])
    return get_sum_sizes(sizes)


def get_free_space(root_node, total_space):
    used_space = get_directory_size(root_node)
    return total_space - used_space


def solve_puzzle_part_2(file_input):
    text = read_input(file_input)
    output = get_terminal_output(text)
    root_node = build_graph(output)
    free_space = get_free_space(root_node, 70000000)
    needed_space = 30000000 - free_space
    sizes = get_at_least_directory_sizes(root_node, needed_space, [])
    return get_smallest_directory(sizes)


if __name__ == "__main__":
    file_input = sys.argv[1]
    answer = solve_puzzle_part_1(file_input)
    print(answer)
    answer = solve_puzzle_part_2(file_input)
    print(answer)
