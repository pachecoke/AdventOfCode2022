import unittest
from main import *
from node import Node


class Day7Tests(unittest.TestCase):
    def test_build_graph_with_root(self):
        output = ["$ cd /"]
        expected_node = Node('/')
        expected_node.values = []
        expected_node.children = []

        actual_node = build_graph(output)
        self.assertEqual(expected_node, actual_node)

    def test_build_graph_with_dir(self):
        output = ["$ cd /", "$ ls", "dir a"]
        expected_node = Node('/')
        expected_node.children = [Node('a')]
        actual_node = build_graph(output)
        self.assertEqual(expected_node, actual_node)

    def test_build_graph_with_file(self):
        output = ["$ cd /", "$ ls", "dir a", "500 b.txt"]
        expected_node = Node('/')
        expected_node.add_child(Node('a'))
        expected_node.add_leaf("500 b.txt")
        actual_node = build_graph(output)
        self.assertEqual(expected_node, actual_node,
                         f"{str(expected_node)} != {str(actual_node)}")

    def test_build_graph_with_two_nodes(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "$ cd a", "$ ls", "dir e"]
        expected_node = Node('/')
        node_a = Node('a')
        node_e = Node('e')
        expected_node.add_child(node_a)
        node_a.add_child(node_e)
        expected_node.add_leaf("500 b.txt")

        actual_node = build_graph(output)
        self.assertEqual(expected_node, actual_node,
                         f"{str(expected_node)} != {str(actual_node)}")

    def test_build_graph_with_backtrack(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "$ cd a", "$ ls", "dir e", "$ cd ..", "$ ls", "100 a.txt"]
        expected_node = Node('/')
        node_a = Node('a')
        node_e = Node('e')
        expected_node.add_leaf("500 b.txt")
        expected_node.add_leaf("100 a.txt")
        expected_node.add_child(node_a)
        node_a.add_child(node_e)

        actual_node = build_graph(output)
        self.assertEqual(expected_node, actual_node,
                         f"{str(expected_node)} != {str(actual_node)}")

    def test_get_all_leaf_nodes(self):
        expected_leaf_nodes = ["500 a.txt",
                               "400 b1.txt", "300 b2.txt", "200 c.txt"]
        root_node = Node('/')
        node_a = Node('a')
        node_a.add_leaf("500 a.txt")

        node_b = Node('b')
        node_b.add_leaf("400 b1.txt")
        node_b.add_leaf("300 b2.txt")

        node_c = Node('c')
        node_c.add_leaf("200 c.txt")

        root_node.add_child(node_a)
        root_node.add_child(node_b)
        node_a.add_child(node_c)

        actual_leaf_nodes = get_leaf_nodes(root_node, [])
        self.assertEqual(set(expected_leaf_nodes), set(actual_leaf_nodes))

    def test_get_file_size(self):
        file_data = "500 b.txt"
        size = get_file_size(file_data)
        self.assertEqual(500, size)

    def test_get_directory_size(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "$ cd a", "$ ls", "dir e", "$ cd ..", "$ ls", "100 a.txt"]
        root_node = build_graph(output)
        actual_size = get_directory_size(root_node)
        self.assertEqual(600, actual_size)

    def test_get_at_most_directory_sizes(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "200 f", "$ cd a", "$ ls", "dir e", "100 a.txt", "$ cd ..", "$ ls", "100 h.txt"]
        root_node = build_graph(output)
        actual_file_sizes = get_at_most_directory_sizes(root_node, 200, [])
        self.assertEqual([('a', 100), ('e', 0)], actual_file_sizes)

    def test_get_at_least_directory_sizes(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "200 f", "$ cd a", "$ ls", "dir e", "200 a.txt", "$ cd ..", "$ ls", "100 h.txt"]
        root_node = build_graph(output)
        actual_file_sizes = get_at_least_directory_sizes(root_node, 200, [])
        self.assertEqual([('/', 1000), ('a', 200)], actual_file_sizes)

    def test_read_input(self):
        expected_text = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k\n"
        text = read_input("test_input")
        self.assertEqual(expected_text, text)

    def test_get_terminal_output(self):
        text = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat"
        expected_output = ["$ cd /", "$ ls", "dir a",
                           "14848514 b.txt", "8504156 c.dat"]
        actual_output = get_terminal_output(text)
        self.assertEqual(expected_output, actual_output)

    def test_solve_puzzle_part_1(self):
        file_size_sum = solve_puzzle_part_1("test_input")
        self.assertEqual(95437, file_size_sum)

    def test_get_dirs_with_small_files(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "400 f", "$ cd a", "$ ls", "dir e", "100 e", "$ cd e", "$ ls", "100 a.txt"]
        root_node = build_graph(output)
        directory_sizes = get_at_most_directory_sizes(root_node, 200, [])
        actual_size = get_sum_sizes(directory_sizes)
        self.assertEqual(300, actual_size)

    def test_get_free_space(self):
        output = ["$ cd /", "$ ls", "dir a",
                  "500 b.txt", "400 f", "$ cd a", "$ ls", "dir e", "100 e", "$ cd e", "$ ls", "100 a.txt"]
        root_node = build_graph(output)
        total_space = 2_000
        free_space = get_free_space(root_node, total_space)
        self.assertEqual(900, free_space)

    def test_get_smallest_size(self):
        directory_sizes = [('a', 100), ('b', 200), ('c', 50), ('d', 200)]
        smallest = get_smallest_directory(directory_sizes)
        self.assertEqual(50, smallest)

    def test_solve_puzzle_part_2(self):
        smallest_dir = solve_puzzle_part_2("test_input")
        self.assertEqual(24933642, smallest_dir)
