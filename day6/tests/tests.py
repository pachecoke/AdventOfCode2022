import unittest
from main import *


class Day6Tests(unittest.TestCase):
    def test_check_has_duplicate_is_true(self):
        text = "abca"
        has_duplicate = check_has_duplicate(text)
        self.assertEqual(True, has_duplicate)

    def test_check_has_duplicate_is_false(self):
        text = "abcd"
        has_duplicate = check_has_duplicate(text)
        self.assertEqual(False, has_duplicate)

    def test_separate_by_fours_1(self):
        text = "abcde"
        expected_separation = ["abcd", "bcde"]
        actual_separation = separate_by_interval(text, 4)
        self.assertEqual(expected_separation, actual_separation)

    def test_separate_by_fours_2(self):
        text = "bvwbjplbgvb"
        expected_separation = ["bvwb", "vwbj", "wbjp",
                               "bjpl", "jplb", "plbg", "lbgv", "bgvb"]
        actual_separation = separate_by_interval(text, 4)
        self.assertEqual(expected_separation, actual_separation)

    def test_get_marker_index(self):
        separated = ["bvwb", "vwbj", "wbjp",
                     "bjpl", "jplb", "plbg", "lbgv", "bgvb"]
        marker_index = get_marker_index(separated)
        self.assertEqual(5, marker_index)

    def test_read_input(self):
        expected_text = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        text = read_input("test_input")
        self.assertEqual(expected_text, text)

    def test_solve_puzzle_part_1(self):
        total_priority = solve_puzzle_part_1("test_input")
        self.assertEqual(11, total_priority)

    def test_separate_by_fourteen(self):
        text = "mjqjpqmgbljsphdztnv"
        expected_separation = ["mjqjpqmgbljsph", "jqjpqmgbljsphd",
                               "qjpqmgbljsphdz", "jpqmgbljsphdzt", "pqmgbljsphdztn", "qmgbljsphdztnv"]
        actual_separation = separate_by_interval(text, 14)
        self.assertEqual(expected_separation, actual_separation)

    def test_solve_puzzle_part_2(self):
        total_priority = solve_puzzle_part_2("test_input")
        self.assertEqual(26, total_priority)
