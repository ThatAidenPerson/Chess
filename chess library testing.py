import chess
from stockfish import Stockfish

# Initializes an empty chess board
board = chess.Board()
stockfish = Stockfish(r"C:\stockfish\stockfish-windows-x86-64-avx2.exe")
fen = board.fen() 

while board.is_checkmate() == False:
    print(board)
    print("-----------------")
    print("A B C D E F G H")
    print(fen)
    move = input("Enter a move: ").lower()

    if chess.Move.from_uci(move) in board.legal_moves:
        board.push_uci(move)
        fen = board.fen()
    else:
        print("Invalid move. Try again.")
        continue
    
    
    stockfish.set_fen_position(fen)
    best_move = stockfish.get_best_move()
    board.push_uci(best_move)
    
if board.is_checkmate() == True:
    print("Checkmate!")

    
# TODO: Add a way to not crash the game when the user enters an invalid number next to the letter






