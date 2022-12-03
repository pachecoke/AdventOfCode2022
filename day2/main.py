import sys


SCORES = {"paper": 2, "rock": 1, "scissors": 3}


def solve_puzzle_part_1(input_file_name):
    text = read_games_input(input_file_name)
    groups = group_games(text)
    games = create_games(groups)
    outcomes = get_outcomes()
    return get_total_score(games, outcomes)


def read_games_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def group_games(input):
    return input.strip().split("\n")


def create_games(groups):
    return [group.split() for group in groups]


def get_outcomes():
    return {'A': {'X': "rock", 'Y': "paper", 'Z': "scissors"},
            'B': {'X': "rock", 'Y': "paper", 'Z': "scissors"},
            'C': {'X': "rock", 'Y': "paper", 'Z': "scissors"}}


def get_real_outcomes():
    return {'A': {'X': "scissors", 'Y': "rock", 'Z': "paper"},
            'B': {'X': "rock", 'Y': "paper", 'Z': "scissors"},
            'C': {'X': "paper", 'Y': "scissors", 'Z': "rock"}}


def get_total_score(games, outcomes):
    total_score = 0
    for game in games:
        total_score += get_game_score(game[0], game[1], outcomes)
    return total_score


def get_game_score(opponent, player, outcomes):
    player_move = get_player_move(opponent, player, outcomes)
    move_score = get_move_score(player_move)
    game_result = get_game_result(opponent, player, outcomes)
    win_score = get_win_score(game_result)
    return move_score + win_score


def get_player_move(opponent, player, outcomes):
    return outcomes[opponent][player]


def get_move_score(player_move):
    return SCORES[player_move]


def get_win_score(game_result):
    if did_player_win(game_result):
        return 6

    if did_player_lose(game_result):
        return 0

    if did_player_draw(game_result):
        return 3


def get_game_result(opponent, player, outcomes):
    player_move = get_player_move(opponent, player, outcomes)
    wins = {'A': "paper", 'B': "scissors", 'C': "rock"}
    losses = {'A': "scissors", 'B': "rock", 'C': "paper"}

    if player_move == wins[opponent]:
        return 1

    if player_move == losses[opponent]:
        return -1

    return 0


def did_player_win(game_result):
    return game_result == 1


def did_player_lose(game_result):
    return game_result == -1


def did_player_draw(game_result):
    return game_result == 0


def solve_puzzle_part_2(input_file_name):
    text = read_games_input(input_file_name)
    groups = group_games(text)
    games = create_games(groups)
    outcomes = get_real_outcomes()
    return get_total_score(games, outcomes)


if __name__ == "__main__":
    file_input = sys.argv[1]
    total_score = solve_puzzle_part_1(file_input)
    print(total_score)

    total_score = solve_puzzle_part_2(file_input)
    print(total_score)
