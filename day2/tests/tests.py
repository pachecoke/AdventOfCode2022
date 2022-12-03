import unittest
from main import *


class Day2Tests(unittest.TestCase):
    def assert_game_result(self, opponent, player, expected_outcome, outcomes):
        game_result = get_game_result(opponent, player, outcomes)
        self.assertEqual(expected_outcome, game_result)

    def assert_move_score(self, move, expected_score):
        score = get_move_score(move)
        self.assertEqual(expected_score, score)

    def assert_win_score(self, opponent, player, expected_score, outcomes):
        game_result = get_game_result(opponent, player, outcomes)
        score = get_win_score(game_result)
        self.assertEqual(expected_score, score)

    def assert_game_score(self, opponent, player, expected_score, outcomes):
        score = get_game_score(opponent, player, outcomes)
        self.assertEqual(expected_score, score)

    def test_did_player_win_A_Y(self):
        outcomes = get_outcomes()
        self.assert_game_result('A', 'Y', 1, outcomes)

    def test_did_player_win_B_X(self):
        outcomes = get_outcomes()
        self.assert_game_result('B', 'X', -1, outcomes)

    def test_did_player_win_C_Z(self):
        outcomes = get_outcomes()
        self.assert_game_result('C', 'Z', 0, outcomes)

    def test_did_player_win_A_X(self):
        outcomes = get_outcomes()
        self.assert_game_result('A', 'X', 0, outcomes)

    def test_get_move_score_Y(self):
        self.assert_move_score("paper", 2)

    def test_get_move_score_X(self):
        self.assert_move_score("rock", 1)

    def test_get_move_score_Z(self):
        self.assert_move_score("scissors", 3)

    def test_get_win_score_A_Y(self):
        outcomes = get_outcomes()
        self.assert_win_score('A', 'Y', 6, outcomes)

    def test_get_win_score_B_X(self):
        outcomes = get_outcomes()
        self.assert_win_score('B', 'X', 0, outcomes)

    def test_get_win_score_C_Z(self):
        outcomes = get_outcomes()
        self.assert_win_score('C', 'Z', 3, outcomes)

    def test_get_game_score_A_Y(self):
        outcomes = get_outcomes()
        self.assert_game_score('A', 'Y', 8, outcomes)

    def test_get_game_score_B_X(self):
        outcomes = get_outcomes()
        self.assert_game_score('B', 'X', 1, outcomes)

    def test_get_game_score_C_Z(self):
        outcomes = get_outcomes()
        self.assert_game_score('C', 'Z', 6, outcomes)

    def test_get_total_score(self):
        games = [['A', 'X'], ['B', 'X']]
        outcomes = get_outcomes()
        score = get_total_score(games, outcomes)
        self.assertEqual(5, score)

    def test_read_input_file(self):
        text = read_games_input("test_input")
        expected_text = "A Y\nB X\nC Z"
        self.assertEqual(expected_text, text)

    def test_group_games(self):
        input_text = "A Y\nB X\nC Z"
        games = group_games(input_text)
        expected_groups = ["A Y", "B X", "C Z"]
        self.assertEqual(expected_groups, games)

    def test_create_games(self):
        groups = ["A Y", "B X", "C Z"]
        games = create_games(groups)
        expected_games = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
        self.assertEqual(expected_games, games)

    def test_solve_puzzle_part_1(self):
        score = solve_puzzle_part_1("test_input")
        self.assertEqual(15, score)

    def test_get_real_win_score_A_Y(self):
        outcomes = get_real_outcomes()
        self.assert_win_score('A', 'Y', 3, outcomes)

    def test_get_real_win_score_B_X(self):
        outcomes = get_real_outcomes()
        self.assert_win_score('B', 'X', 0, outcomes)

    def test_get_real_win_score_C_Z(self):
        outcomes = get_real_outcomes()
        self.assert_win_score('C', 'Z', 6, outcomes)

    def test_get_real_game_score_A_Y(self):
        outcomes = get_real_outcomes()
        self.assert_game_score('A', 'Y', 4, outcomes)

    def test_solve_puzzle_part_2(self):
        score = solve_puzzle_part_2("test_input")
        self.assertEqual(12, score)
