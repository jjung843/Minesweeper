def initialise_board():
    '''
    initialise_board initialises the minesweeper grid

    Arguments:
        N/A

    Returns:
        board (list): the minesweeper board

    Notes:
        Postcondition 1: board is a list of length 25.
        Postcondition 2: Each element in board is a string and is 'O'.
    '''
    # Initialise a list of 25 characters
    board = ["O"] * 25
    return board
def display_board(board):
    '''
    display_board displays the board (list) to screen as a 5 × 5 grid.

    Arguments:
        board (list): the minesweeper board

    Returns:
        N/A

    Notes:
        Precondition 1: board is a list of length 25.
        Precondition 2: Each element in board is a string and is 'O'.
        Postcondition 1: The displayed output shout be a list arranged into a 5 by 5 grid.
    '''
    # Arrange the 1D list into a 5 by 5
    for i in range(0, 24, 5):
        print(board[i:i+5])
def insert_mines(board, positions):
    '''
    insert_mines inserts mines to the board at the specified positions.

    Arguments:
       board (list): the minesweeper board
       positions (list): the location of each mine

    Returns:
       mine_board (list): the minesweeper board updated with mines marked 'X'

    Notes:
        Precondition 1: board is a list of length 25.
        Precondition 2: positions is a list of mine coordinates(list).
        Postcondition 1: mine elements should be denoted with a string 'X'.
    '''
   #Iterate through the mine positions list and obtain mine coordinates
    for i in range(len(positions)):
        mine = positions[i]
        row = mine[0]
        col = mine[1]
        # Formula to translate 2D coordinates onto 1D list position
        mine_pos = (row * 5) + col
        # Print 'X' in mine positions
        board[mine_pos] = 'X'
    return board
def count_adjacent_mines(board, row, col):
    '''
    count_adjacent_mines counts the number of mines adjacent to the selected position.

    Arguments:
       board (list): the minesweeper board
       row (int): the row of the square being checked for adjacent mines
       col (int): the column of the square being checked for adjacent mines

    Returns:
       count (int): the number of adjacent mines

    Notes:
        Precondition 1: board is a list of length 25, and represents an 5 by 5 minesweeper board.
        Precondition 2: row and col are integers in range 0 to 4, representing valid indices of the minesweeper grid.
        Postcondition 1: Returns an integer representing the number of adjacent mines.
        Postcondition 2: This function only examines the squares above, below, left and right of the chosen
                        position(row, col).

    '''
    count = 0
    guess_pos = (row * 5) + col
    # Check adjacency for row above
    if row > 0 and board[guess_pos - 5] == 'X':
        count += 1

    # Check adjacency for row below
    if row != 4:
        if row < len(board) - 1 and board[guess_pos + 5] == 'X':
            count += 1

    # Check adjacency for column left
    if col > 0 and board[guess_pos - 1] == 'X':
        count += 1

    # Check adjacency for column right
    if col < len(board)/5 - 1 and board[guess_pos + 1] == 'X' and ((guess_pos + 1) % 5 != 0):
        count += 1

    return count
def play_turn(board, row, col):
    '''
    play_turn plays a turn using the provided row and column on the minesweeper board.

    Arguments:
       board (list): the minesweeper board
       row (int): the row (0-4) of the position being selected
       col (int): the column (0-4) of the position being selected

    Returns:
       new_board (list): the updated board with the turn added
       found (bool): a value True if a mine was selected and False otherwise

    Notes:
        Precondition 1: board is a list of length 25, and represents an 5 by 5 minesweeper board.
        Precondition 2: row and col are integers in range 0 to 4, representing valid indices of the minesweeper grid
        Precondition 3: The count_adjacent_mines function is defined and accessible. This function is responsible for
                        counting the number of mines adjacent to the given position.
        Postcondition 1: The function returns the found value along with the updated game board new_board.
    '''
    if row < 5 and col < 5:
        turn_pos = (row * 5) + col
        # Display '#' if there is a mine in the turn position
        if board[turn_pos] == 'X':
            new_board = board
            board[turn_pos] = '#'
            # Return True since mine is found
            return True, new_board
        # When the chosen position has no mines
        else:
            # Call the function that counts the adjacent mines
            count = count_adjacent_mines(board, row, col)
            if count > 0:
                new_board = board
                new_board[turn_pos] = str(count)
            else:
                new_board = board
                new_board[turn_pos] = ' '
            # Return False since mine is not found
            return False, new_board

def check_win(board):
    '''
    check_win determines if the player has won the game

    Arguments:
       board (list): the minesweeper board

    Returns:
       win (bool): if the game has been won (True) or has not been won (False)

    Notes:
        Precondition 1: board is a list of length 25, and represents an 5 by 5 minesweeper board.
        Precondition 2: 'O' denotes cells that have not been selected yet. Other characters can represent cells that
                        have been revealed, contain mines ('X'), or show numbers indicating the count of adjacent mines.
        Postcondition 1: The function determines the win condition based solely on the current state of the game board.
    '''
    # Initialise the count for unselected positions on the grid
    unselected = 0
    # Iterate through the board to check for positions yet to be selected
    for i in range(len(board)):
        if board[i] == 'O':
            # Add count for unselected positions for each 'O' in grid
            unselected += 1
            # Determine whether the game is won using the final outcome for the unselected positions
    if unselected == 0:
        return True
    else:
        return False
def play_game(positions):
    '''
    play_game allows the user to play the game from the start to finish

    Arguments:
        positions (list): the positions of the mines placed in the minesweeper board

    Returns:
        N/A

    Notes:
        Precondition 1: board is a list of length 25, and represents an 5 by 5 minesweeper board.
        Precondition 2: positions is a list of tuples representing the positions of the mines. Each position is expected
                        to be a coordinate within the minesweeper grid indices.
        Precondition 3: the user input is expected to be two integers each representing the row and column of the turn.
        Postcondition 1: The function play_game is designed to run the game loop and does not return any value.
        Postcondition 2: This function displays the finish message according to the user's interaction.
    '''
    # Initialise the board and insert mines at positions accordingly
    board = initialise_board()
    mine_board = insert_mines(board, positions)
    # The player will see an empty board, separate from the mine board
    player_board = initialise_board()
    display_board(player_board)

    # Initialise game status
    game_done = False

    # While the game has not ended
    while not game_done:
        # Ask for user input
        user_input = input("Please enter your row and column to play (e.g 1 3): ")
        row = int((user_input.split())[0])
        col = int((user_input.split())[1])
        # Play the turn on the mine board
        mine_found, mine_board = play_turn(board, row, col)

        if not mine_found:
            game_done = check_win(mine_board)
            if not game_done:
                # Translate the turn onto the player's board
                turn_pos = (row * 5) + col
                player_board[turn_pos] = mine_board[turn_pos]
                display_board(player_board)
        # If a mine is found in the turn, end game displaying a losing message
        if mine_found:
            turn_pos = (row * 5) + col
            player_board[turn_pos] = mine_board[turn_pos]
            display_board(player_board)
            print("Unlucky, You lost!")
            return
    # If a game is finished without hitting a mine, end game displaying a winning message
    if game_done:
        turn_pos = (row * 5) + col
        player_board[turn_pos] = mine_board[turn_pos]
        display_board(player_board)
        print("Congrats, You won!")
        return