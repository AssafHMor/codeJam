from computer_functions import get_computer_move, HEAPS

LOWEST_VAL = 1  # the lowest possible value the user may enter
PLACE_REFACTOR = 1  # a correction factor
ONE_PLAYER = 1  # the one player option
TWO_PLAYERS = 2  # the two players option


def print_heaps(heaps):
    """
    this method prints the current state of the heaps
    :param heaps: the current heaps to print out
    """

    for i in range(0, len(heaps)):
        print(str(i + PLACE_REFACTOR) + ':')  # print the heap number
        print((heaps[i] * "* ")[:-1])  # print the asterisks


def get_player_move(heaps, player):
    """
    this method returns a list containing the row, and how many asterisks to
    remove from that row. this method also checks if the input is valid - if
    the value of the row exist and if so it check if the row is not empty,
    if it is empty it lets the user know. it also checks if the number of
    asterisks is valid.
    :param heaps: the current heaps
    :param player: the current player
    :return: a list of size 2, where the first place in the list represents the
    row and the second place represents how many asterisk to remove
    """
    print(player + ", it's your turn:")
    move = [int(input("Row?")) - PLACE_REFACTOR]  # initiate move list

    # if the row value is not valid ask again from the user
    while any((move[0] < 0, move[0] > len(heaps) - LOWEST_VAL)):
        move[0] = int(input("Row?")) - PLACE_REFACTOR

    # if the row is empty, notify the user and ask for the row again
    while heaps[move[0]] == 0:
        print("That row is empty")
        move[0] = int(input("Row?")) - PLACE_REFACTOR

    move.append(int(input("How many?")))  # append the amount of asterisks
    # if the number of the asterisks in this row is not valid ask again
    while any((move[1] > heaps[move[0]], move[1] < LOWEST_VAL)):
        move[1] = int(input("How many?"))
    return move


def enact_move(heaps, moves):
    """
    this method gets the old heaps and removes the number of asterisks from
    the desired row and returns the modified heaps
    :param board: a list of heaps
    :param move: a list of size 2, where the first place in the list represents
    the row and the second place represents how many asterisk to remove
    :return: "heaps" the modified heaps
    """
    heaps[moves[0]] = heaps[moves[0]] - moves[1]
    return heaps


def check_for_win(heaps):
    """
    this method checks if there are no more values in the heaps
    :param heaps: the current heaps state
    :return: true if the heaps are empty and false otherwise
    """
    for i in range(0, len(heaps)):
        if heaps[i] != 0:
            return False
    return True


def player_game_roll(players, heaps):
    """
    this method prints the current heaps after the move has been made and then
    returns the modified heaps
    :param players: which human player it is
    :param heaps: the current heaps
    :return: returns the changed heaps
    """
    move = get_player_move(game_heaps, players)
    heaps = enact_move(heaps, move)
    print_heaps(heaps)
    return heaps


def comp_game_roll(heaps):
    """
    this method prints the current heaps after the move has been made,
    it also print what move the computer chose to make, and then returns the
    modified heaps
    :param heaps: the current heaps
    :return: returns the changed heaps
    """
    comp_move = get_computer_move(heaps)
    heaps = enact_move(heaps, comp_move)
    print("Computer takes", comp_move[1],"from row", comp_move[0] +
          PLACE_REFACTOR)
    print_heaps(heaps)
    return heaps


human_players = int(input("Please enter the number of human players (1 or 2):"))
if human_players == ONE_PLAYER:  # in case of computer vs. human
    player_1 = input("Please enter your name:")
    player_2 = "comp"  # the second player in this case is the computer
    last_winner = player_1  # default value of winner of the last round
    # run the game as long as the user wish to continue the game
    while True:
        print_heaps(HEAPS)
        game_heaps = list(HEAPS)
        # run the round until there is a winner
        while True:
            if last_winner == player_1:  # human gets to begin this round
                if check_for_win(player_game_roll(player_1, game_heaps)):
                    last_winner = player_1
                    print("You win")
                    break
                if check_for_win(comp_game_roll(game_heaps)):
                    last_winner = player_2
                    print("Computer wins")
                    break
            else:  # computer gets to begin this round
                if check_for_win(comp_game_roll(game_heaps)):
                    last_winner = player_2
                    print("Computer wins")
                    break
                if check_for_win(player_game_roll(player_1, game_heaps)):
                    last_winner = player_1
                    print("You win")
                    break
        game_on = input("Play again? (Y/N)")  # ask if to continue game or not
        if game_on == 'y' or game_on == 'Y':
            continue
        else:
            break

elif human_players == TWO_PLAYERS:  # in case of two human players
    player_1 = input("Name of first player:")
    player_2 = input("Name of second player:")
    last_winner = player_1  # default value of winner of the last round
    # run the game as long as the user wish to continue the game
    while True:
        print_heaps(HEAPS)
        game_heaps = list(HEAPS)
        # run the round until there is a winner
        while True:
            if last_winner == player_1:  # first player gets to begin this round
                if check_for_win(player_game_roll(player_1, game_heaps)):
                    last_winner = player_1
                    print(player_1, "wins")
                    break
                if check_for_win(player_game_roll(player_2, game_heaps)):
                    last_winner = player_2
                    print(player_2, "wins")
                    break
            else:  # second player gets to begin this round
                if check_for_win(player_game_roll(player_2, game_heaps)):
                    last_winner = player_2
                    print(player_2, "wins")
                    break
                if check_for_win(player_game_roll(player_1, game_heaps)):
                    last_winner = player_1
                    print(player_1, "wins")
                    break
        game_on = input("Play again? (Y/N)")
        if game_on == 'y' or game_on == 'Y':
            continue
        else:
            break