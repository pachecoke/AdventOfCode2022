import unittest
from main import *


class Day5Tests(unittest.TestCase):
    def test_move_crate(self):
        from_stack = ['Z', 'N']
        to_stack = ['M', 'C', 'D']
        new_from_stack, new_to_stack = move_crate(from_stack, to_stack)
        self.assertEqual(['Z'], new_from_stack)
        self.assertEqual(['M', 'C', 'D', 'N'], new_to_stack)

    def test_move_crates(self):
        from_stack = ['M', 'C', 'D']
        to_stack = ['Z', 'N']
        new_from_stack, new_to_stack = move_crates(from_stack, to_stack, 2)
        self.assertEqual(['M'], new_from_stack)
        self.assertEqual(['Z', 'N', 'D', 'C'], new_to_stack)

    def test_parse_stacks_to_lines(self):
        text = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 "
        stack_lines = parse_stacks_to_lines(text)
        expected_stack_lines = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
        self.assertEqual(expected_stack_lines, stack_lines)

    def test_remove_number_line(self):
        stack_lines_to_remove = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
        expected_stack_lines = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"]
        actual_stack_lines = remove_number_line(stack_lines_to_remove)
        self.assertEqual(expected_stack_lines, actual_stack_lines)

    def test_get_stack_count_1(self):
        stack_lines = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"]
        stack_count = get_stack_count(stack_lines)
        self.assertEqual(3, stack_count)

    def test_get_stack_count_2(self):
        stack_lines = ["    [D]        ", "[N] [C]        ", "[Z] [M] [P] [O]"]
        stack_count = get_stack_count(stack_lines)
        self.assertEqual(4, stack_count)

    def test_create_stacks(self):
        stack_lines = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"]
        expected_stacks = [["[Z]", "[N]"], ["[M]", "[C]", "[D]"], ["[P]"]]
        actual_transposed_stack_lines = transpose_stack_lines(stack_lines)
        self.assertEqual(expected_stacks, actual_transposed_stack_lines)

    def test_parse_move_command(self):
        command = "move 1 from 2 to 1"
        expected = [1, 2, 1]
        actual = parse_move_command(command)
        self.assertEqual(expected, actual)

    def test_apply_move(self):
        stacks = [["[Z]", "[N]"], ["[M]", "[C]", "[D]"], ["[P]"]]
        expected_stacks_after_move = [["[Z]", "[N]", "[D]", "[C]"], ["[M]"], ["[P]"]]
        move = [2, 2, 1]
        actual_stacks_after_move = apply_move(move, stacks)
        self.assertEqual(expected_stacks_after_move, actual_stacks_after_move)

    def test_read_input(self):
        expected_text = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
        text = read_input("test_input")
        self.assertEqual(expected_text, text)

    def test_split_input(self):
        text = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
        stack_lines, move_lines = split_input(text)
        expected_stack_lines = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 "
        self.assertEqual(expected_stack_lines, stack_lines)
        expected_move_lines = "move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
        self.assertEqual(expected_move_lines, move_lines)

    def test_parse_moves(self):
        move_lines = "move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
        expected_moves = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]
        actual_moves = parse_moves(move_lines)
        self.assertEqual(expected_moves, actual_moves)

    def test_get_top_crate(self):
        stack = ["[A]", "[B]", "[C]"]
        expected_top_crate = "[C]"
        actual_top_crate = get_top_crate(stack)
        self.assertEqual(expected_top_crate, actual_top_crate)

    def test_get_crate_name(self):
        crate = "[A]"
        expected_crate_name = 'A'
        actual_crate_name = get_crate_name(crate)
        self.assertEqual(expected_crate_name, actual_crate_name)

    def test_get_top_crates(self):
        stacks = [["[Z]", "[N]"], ["[M]", "[C]", "[D]"], ["[P]"]]
        expected_crates = "NDP"
        crates = get_top_crates(stacks)
        self.assertEqual(expected_crates, crates)

    def test_solve_puzzle_part_1(self):
        expected_top_crates = "CMZ"
        top_crates = solve_puzzle_part_1("test_input")
        self.assertEqual(expected_top_crates, top_crates)

    def test_move_crates_multiple(self):
        from_stack = ['M', 'C', 'D']
        to_stack = ['Z', 'N']
        new_from_stack, new_to_stack = move_crates_multiple(from_stack, to_stack, 2)
        self.assertEqual(['M'], new_from_stack)
        self.assertEqual(['Z', 'N', 'C', 'D'], new_to_stack)

    def test_solve_puzzle_part_2(self):
        expected_top_crates = "MCD"
        top_crates = solve_puzzle_part_2("test_input")
