import chess
from stockfish import Stockfish
import os, time
import cfs

# chess board
board = chess.Board()
fen = board.fen()

# split the fen into its components
split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number = cfs.setup_board(fen) 


board_grid = {
    "a": {1: split_locations[0][0], 2: split_locations[0][1], 3: split_locations[0][2], 4: split_locations[0][3], 5: split_locations[0][4], 6: split_locations[0][5], 7: split_locations[0][6], 8: split_locations[0][7]},
    "b": {1: split_locations[1][0], 2: split_locations[1][1], 3: split_locations[1][2], 4: split_locations[1][3], 5: split_locations[1][4], 6: split_locations[1][5], 7: split_locations[1][6], 8: split_locations[1][7]},
    "c": {1: split_locations[2][0], 2: split_locations[2][1], 3: split_locations[2][2], 4: split_locations[2][3], 5: split_locations[2][4], 6: split_locations[2][5], 7: split_locations[2][6], 8: split_locations[2][7]},
    "d": {1: split_locations[3][0], 2: split_locations[3][1], 3: split_locations[3][2], 4: split_locations[3][3], 5: split_locations[3][4], 6: split_locations[3][5], 7: split_locations[3][6], 8: split_locations[3][7]},
    "e": {1: split_locations[4][0], 2: split_locations[4][1], 3: split_locations[4][2], 4: split_locations[4][3], 5: split_locations[4][4], 6: split_locations[4][5], 7: split_locations[4][6], 8: split_locations[4][7]},
    "f": {1: split_locations[5][0], 2: split_locations[5][1], 3: split_locations[5][2], 4: split_locations[5][3], 5: split_locations[5][4], 6: split_locations[5][5], 7: split_locations[5][6], 8: split_locations[5][7]},
    "g": {1: split_locations[6][0], 2: split_locations[6][1], 3: split_locations[6][2], 4: split_locations[6][3], 5: split_locations[6][4], 6: split_locations[6][5], 7: split_locations[6][6], 8: split_locations[6][7]},
    "h": {1: split_locations[7][0], 2: split_locations[7][1], 3: split_locations[7][2], 4: split_locations[7][3], 5: split_locations[7][4], 6: split_locations[7][5], 7: split_locations[7][6], 8: split_locations[7][7]}
}



print(board_grid)