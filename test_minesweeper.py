import pytest
from functions_minesweeper import *

# Unit tests for insert_mines
def test_insert_mines_single_mines():
    board = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',]
    positions = [[0,0]]
    mine_board = insert_mines(board, positions)
    assert(mine_board == ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'])
def test_insert_mines_multiple_mines():
    board = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', ]
    positions = [[0,0], [1,0], [2,0], [3,0], [4,0]]
    mine_board = insert_mines(board, positions)
    assert (mine_board == ['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O',
                           'O', 'O', 'X', 'O', 'O', 'O', 'O'])

# Unit tests for count_adjacent_mines
def test_count_adjacent_mines_in_next_line():
    board = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',]
    count = count_adjacent_mines(board, 1, 4)
    assert(count == 0)
def test_count_adjacent_mines_in_previous_line():
    board = ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', ]
    count = count_adjacent_mines(board, 1, 0)
    assert (count == 0)

# Unit tests for play_turn
def test_play_turn_win():
    board = ['O', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    mine_found, turn1 = play_turn(board, 0, 0)
    mine_found, turn2 = play_turn(turn1, 1, 0)
    mine_found, turn3 = play_turn(turn2, 1,1)
    mine_found, turn4 = play_turn(turn3,2,0)
    mine_found, turn5 = play_turn(turn4, 3, 2)
    assert (mine_found, turn5 == False,['1', 'X', 'X', 'X', 'X', ' ', '3', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '4', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
def test_play_turn_lose():
    board = ['O', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X',
             'X', 'X', 'X', 'X']
    mine_found, turn = play_turn(board, 0, 1)
    assert(mine_found, turn == True, ['O', '#', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])

# Unit tests for check_win
def test_check_win_true():
    board = ['1', 'X', 'X', 'X', 'X', ' ', '3', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '4', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    assert(check_win(board) == True)
def test_check_win_false():
    board = ['1', 'X', 'X', 'X', 'X', ' ', '3', 'X', 'X', 'X', '1', 'X', 'X', 'X', 'X', 'X', 'X', '4', 'X', 'X', 'X',
             'X', 'X', 'X', 'O']
    assert(check_win(board) == False)