import chess
from stockfish import Stockfish
import os, time

board = chess.Board()
stockfish = Stockfish(r"M:\stockfish\stockfish-windows-x86-64-avx2.exe")
fen = board.fen()

def print_board():
    print(board)
    print("-----------------")
    print("A B C D E F G H")
    print(board.fen())
    
    os.system("cls")

while board.is_game_over() == False:
    print_board()
    stockfish.set_fen_position(board.fen())
    move = stockfish.get_best_move()
    board.push_san(move)