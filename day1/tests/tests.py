import unittest
from main import *


class Day1Tests(unittest.TestCase):
    def test_read_calories_input(self):
        calories = read_calories_input("test_input")
        expected_calories = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
        self.assertEqual(expected_calories, calories)

    def test_group_items(self):
        input = "abc\ndef\nghi\n\njkl\n\nmno\npqr"
        expected_groups = ["abc\ndef\nghi", "jkl", "mno\npqr"]
        actual_groups = group_items(input)
        self.assertEqual(expected_groups, actual_groups)

    def test_create_list(self):
        input = ["abc\ndef\nghi", "jkl", "mno\npqr"]
        expected_list = [["abc", "def", "ghi"], ["jkl"], ["mno", "pqr"]]
        actual_list = create_list(input)
        self.assertEqual(expected_list, actual_list)

    def test_create_list_with_empty_line(self):
        input = ["abc\ndef\nghi", "jkl", "mno\npqr\n"]
        expected_list = [["abc", "def", "ghi"], ["jkl"], ["mno", "pqr"]]
        actual_list = create_list(input)
        self.assertEqual(expected_list, actual_list)

    def test_get_calories_sum(self):
        input = [[1000, 2000], [100], [3001], [100, 200]]
        expected_sum = [3000, 100, 3001, 300]
        actual_sum = get_calories_sum(input)
        self.assertEqual(expected_sum, actual_sum)

    def test_get_highest_calories(self):
        input = [[1000, 2000], [100], [3001], [100, 200]]
        expected_highest = 3001
        actual_highest = get_highest_calories(input)
        self.assertEqual(expected_highest, actual_highest)

    def test_get_highest_calories_strings(self):
        input = [["1000", "2000"], ["100"], ["3001"], ["100", "200"]]
        expected_highest = 3001
        actual_highest = get_highest_calories(input)
        self.assertEqual(expected_highest, actual_highest)

    def test_solve_puzzle_part_1(self):
        expected_highest_calories = 24000
        actual_highest_calories = solve_puzzle_part_1("test_input")
        self.assertEqual(expected_highest_calories, actual_highest_calories)

    def test_solve_puzzle_part_2(self):
        expected_top_3_calories = 45000
        actual_top_3_calories = solve_puzzle_part_2("test_input")
        self.assertEqual(expected_top_3_calories, actual_top_3_calories)
