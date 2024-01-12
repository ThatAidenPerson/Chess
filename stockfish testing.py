from stockfish import Stockfish

# Initialize the stockfish class with the path to your Stockfish engine file
stockfish = Stockfish("C:/Users/aiden/Desktop/Chess/stockfish-10-win/Windows/stockfish_10_x64.exe")

# Set the position by using Forsyth–Edwards Notation (FEN)
stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

# Get the best move for the current board position
best_move = stockfish.get_best_move()

print(best_move)