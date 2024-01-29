import chess

def setup_board(starting_fen):

    # get fen by setting up a chess board using a specific fen, if the parameter is not specified, it'll use the default chess starting fen
    board = chess.Board(starting_fen) 
    fen = board.fen() # rnbqkbnr/ppppppp1/8/P7/6Pp/8/1PPPPP1P/RNBQKBNR b KQkq g3 0 3
                      # 0       1        2 3 4    5 6        7        8 9   10 11 12
    
    split_fen = fen.split()

    split_locations = [[],[],[],[],[],[],[],[]] 
    level = 0
    turn = None
    castling = ""
    en_passant = ""
    halfmove_clock = None
    fullmove_number = None

    for i in split_fen[0]:
        if i.isalpha() and level < 8:
            split_locations[level].append(i)
        elif i.isdigit() and level < 8: # •
            for y in range(int(i)):
                split_locations[level].append("•")
        elif i == "/" and i == " ":
            level += 1
        elif level >= 8:
            if i == "w" or i == "b":
                turn = i
            elif i.isdigit():
                if level == 11:
                    fullmove_number = int(i)
                elif level == 12:
                    halfmove_clock = int(i)
            if turn == 10:
                en_passant += str(i)
            else:
                castling += i

        
        

    return split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number

def revert_fen(split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number):
    fen = ""



split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number = setup_board("rnbqkbnr/ppppppp1/8/P7/6Pp/8/1PPPPP1P/RNBQKBNR b KQkq g3 0 3")

print(split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number)