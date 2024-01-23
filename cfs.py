import chess

def setup_board(starting_fen):

    board = chess.Board(starting_fen)
    fen = board.fen()
    
    split_fen = fen.split()

    split_locations = [[],[],[],[],[],[],[],[]] 
    level = 0

    for i in split_fen[0]:
        if i.isalpha():
            split_locations[level].append(i)
        elif i.isdigit(): # •
            for y in range(int(i)):
                split_locations[level].append("•")
        elif i == "/":
            level += 1

    return board, fen, split_locations

board, fen, locations = setup_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")