import unittest
from main import *


class Day4Tests(unittest.TestCase):
    def test_parse_assignment_1(self):
        assignment = parse_assignment("2-4")
        self.assertEqual({2, 3, 4}, assignment)

    def test_parse_assignment_2(self):
        assignment = parse_assignment("6-8")
        self.assertEqual({6, 7, 8}, assignment)

    def test_read_assignments_1(self):
        assignment1, assignment2 = parse_assignment_pair("2-4,6-8")
        self.assertEqual({2, 3, 4}, assignment1)
        self.assertEqual({6, 7, 8}, assignment2)

    def test_read_assignments_2(self):
        assignment1, assignment2 = parse_assignment_pair("2-3,4-5")
        self.assertEqual({2, 3}, assignment1)
        self.assertEqual({4, 5}, assignment2)

    def test_get_assignment_overlap(self):
        overlap = get_overlap({5, 7}, {7, 9})
        self.assertEqual({7}, overlap)

    def test_get_assignment_overlap_empty(self):
        overlap = get_overlap({2, 3, 4}, {6, 7, 8})
        self.assertEqual(set(), overlap)

    def test_is_full_overlap_1(self):
        is_full = is_full_overlap({2, 3, 4}, {3, 4})
        self.assertEqual(True, is_full)

    def test_is_full_overlap_2(self):
        is_full = is_full_overlap({2, 3, 4}, {3, 4, 5})
        self.assertEqual(False, is_full)

    def test_read_input(self):
        expected_text = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
        text = read_input("test_input")
        self.assertEqual(expected_text, text)

    def test_create_assignments(self):
        expected_assignments = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
        items = create_raw_assignments_pairs("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8")
        self.assertEqual(expected_assignments, items)

    def test_solve_puzzle_part_1(self):
        full_overlap_count = solve_puzzle_part_1("test_input")
        self.assertEqual(2, full_overlap_count)

    def test_get_all_overlap_count_1(self):
        assignments = ["2-4,4-6", "2-3,4-5"]
        count = get_all_overlap_count(assignments)
        self.assertEqual(1, count)

    def test_get_all_overlap_count_2(self):
        assignments = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
        count = get_all_overlap_count(assignments)
        self.assertEqual(4, count)

    def test_solve_puzzle_part_2(self):
        overlap_count = solve_puzzle_part_2("test_input")
        self.assertEqual(4, overlap_count)
