# Function changing char at given index of string
def replace(old_string, new_char, char_index):
    return old_string[: char_index] + new_char + old_string[char_index + 1:]


# Win detector function
def check_win(modified_possible_wins, player_move, player):
    counter = -1

    # Modifying possible_wins list with player's choice
    for position in modified_possible_wins:
        counter += 1
        if player_move == position:
            modified_possible_wins[counter] = player

    # Looking for three repetitions of X or O in a row, if there is such, return that player has won
    for position in range(len(modified_possible_wins) - 2):
        # Third requirement divides list into chunks of 3
        if modified_possible_wins[position] == modified_possible_wins[position + 1] and \
           modified_possible_wins[position] == modified_possible_wins[position + 2] and\
           (position + 3) % 3 == 0:
            return True


# String containing ascii tic tac toe art
table = """  
    A     B     C
      |     |     
1  ~  |  ~  |  ~  
 _____|_____|_____
      |     |     
2  ~  |  ~  |  ~  
 _____|_____|_____
      |     |     
3  ~  |  ~  |  ~  
      |     | """

# Indexes in string of squares able to fill found by :
# indexes = [index for index, sign in enumerate(table) if sign == "~"]


positions_to_fill = {
    "A1": 43,
    "A2": 100,
    "A3": 157,
    "B1": 49,
    "B2": 106,
    "B3": 163,
    "C1": 55,
    "C2": 112,
    "C3": 169,
}

# All win possibilities
win_scenarios = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], ["A1", "B1", "C1"],
                 ["A2", "B2", "C2"], ["A3", "B3", "C3"], ["A1", "B2", "C3"], ["A3", "B2", "C1"]]


#        ___Gameplay___

# Player1 being X or O
player1 = input("Pick X or O : ")
player1 = player1.capitalize()

# Check if input is valid: X or O
if player1 != "X" and player1 != "O":
    raise TypeError("Wrong pick")

# Player2 becomes opposite to player one
if player1 == "X":
    player2 = "O"
else:
    player2 = "X"

# Creating auxiliary list to keep player moves in record
auxiliary_list = []
for scenario in win_scenarios:
    for element in scenario:
        auxiliary_list.append(element)


# Looping while nobody won
win = False
current_player = player1

while not win:
    # Show current table state to current_player and ask for next move
    print(table)
    move = input(f"Where would you like to put {current_player} :")

    # Reformatting input by capitalizing first letter
    move = replace(move, move[0].capitalize(), 0)

    # Checking if move is valid choice
    if move in positions_to_fill:

        # Updating table with current_player's choice
        table = replace(table, current_player, positions_to_fill[move])

        # Remove used position from positions_to_fill
        positions_to_fill.pop(move)

        # Win detection
        if check_win(auxiliary_list, move, current_player):
            print(table)
            print(f"\nGAME WON BY {current_player}")
            break

        # End of the move - change of current_player for next loop
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1