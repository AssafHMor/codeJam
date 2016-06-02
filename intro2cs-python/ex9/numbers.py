WINNER_SUM = 29


def take_turn(turn_num, total_sum):
    game_won = False
    while not game_won:
        while 0 <= turn_num < 10:
            if turn_num + total_sum <= WINNER_SUM:
                print()