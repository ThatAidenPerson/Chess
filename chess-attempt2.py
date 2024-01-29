import chess
from stockfish import Stockfish
import os, time
import cfs

board_grid = {
    "a": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "b": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "c": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "d": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "e": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "f": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "g": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None},
    "h": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}
}

board = chess.Board()
board.fen()

print(board)