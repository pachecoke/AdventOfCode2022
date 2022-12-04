import unittest
from main import *


class Day3Tests(unittest.TestCase):
    def assert_get_compartments(self, input, expected_compartments):
        compartments = get_compartments(input)
        self.assertEqual(expected_compartments, compartments)

    def test_get_compartments_1(self):
        expected_compartments = ["abc", "Def"]
        self.assert_get_compartments("abcDef", expected_compartments)

    def test_get_compartments_2(self):
        expected_compartments = ["Def", "abc"]
        self.assert_get_compartments("Defabc", expected_compartments)

    def test_get_compartments_3(self):
        expected_compartments = ["vJrwpWtwJgWr", "hcsFMMfFFhFp"]
        self.assert_get_compartments(
            "vJrwpWtwJgWrhcsFMMfFFhFp", expected_compartments)

    def test_get_common_item_g(self):
        compartments = ["abcg", "gDef"]
        common_item = get_common_item(compartments)
        self.assertEqual('g', common_item)

    def test_get_common_item_D(self):
        compartments = ["Def", "abD"]
        common_item = get_common_item(compartments)
        self.assertEqual('D', common_item)

    def test_get_item_priority_a(self):
        priority = get_item_priority('a')
        self.assertEqual(1, priority)

    def test_get_item_priority_p(self):
        priority = get_item_priority('p')
        self.assertEqual(16, priority)

    def test_get_item_priority_A(self):
        priority = get_item_priority('A')
        self.assertEqual(27, priority)

    def test_read_input(self):
        expected_text = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
        text = read_input("test_input")
        self.assertEqual(expected_text, text)

    def test_create_items(self):
        expected_items = ["abc", "def", "hij"]
        items = create_rucksacks("abc\ndef\nhij")
        self.assertEqual(expected_items, items)

    def test_get_total_priority(self):
        rucksacks = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        priority = get_total_priority(rucksacks)
        self.assertEqual(157, priority)

    def test_solve_puzzle_part_1(self):
        total_priority = solve_puzzle_part_1("test_input")
        self.assertEqual(157, total_priority)

    def test_get_badge_c(self):
        group = ["abc", "dec", "hic"]
        badge = get_badge(group)
        self.assertEqual('c', badge)

    def test_get_badge_r(self):
        group = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
        badge = get_badge(group)
        self.assertEqual('r', badge)

    def test_get_badge_priority(self):
        group = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
        badge_priority = get_badge_priority(group)
        self.assertEqual(18, badge_priority)

    def test_get_total_badge_priority(self):
        group1 = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
        group2 = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        badge_priority = get_total_badge_priority([group1, group2])
        self.assertEqual(70, badge_priority)

    def test_create_groups(self):
        rucksacks = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        groups = create_groups(rucksacks)
        group1 = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
        group2 = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        expected_groups = [group1, group2]
        self.assertEqual(expected_groups, groups)

    def test_solve_puzzle_part_2(self):
        total_priority = solve_puzzle_part_2("test_input")
        self.assertEqual(70, total_priority)
