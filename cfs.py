import chess

def setup_board(starting_fen):

    # get fen by setting up a chess board using a specific fen, if the parameter is not specified, it'll use the default chess starting fen
    board = chess.Board(starting_fen) 
    fen = board.fen() # rnbqkbnr/ppppppp1/8/P7/6Pp/8/1PPPPP1P/RNBQKBNR b KQkq g3 0 3
                      # 0       1        2 3 4    5 6        7        <--- levels visualised
                      # 0                                             1 2    3  4 5 <--- split_fen index visualised

    
    split_fen = fen.split()

    split_locations = [[],[],[],[],[],[],[],[]] 
    level = 0
    turn = None
    castling = ""
    en_passant = ""
    halfmove_clock = None
    fullmove_number = None
    print
    for y in range(8):
        for i in split_fen[0]:
            #print(i)
            
            if i.isalpha() and level < 8:
                split_locations[level].append(i)
            elif i.isdigit() and level < 8: # •
                for y in range(int(i)):
                    split_locations[level].append("•")
            elif i == "/" or i == " ":
                level += 1
            else:
                pass
        if y == 1:
            turn = split_fen[1]
        elif y == 2:
            castling = split_fen[2]
        elif y == 3:
            en_passant = split_fen[3]
        elif y == 4:
            halfmove_clock = split_fen[4]
        elif y == 5:
            fullmove_number = split_fen[5]


            
        
    return split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number

def revert_fen(split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number):
    pass



split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number = setup_board("rnbqkbnr/ppppppp1/8/P7/6Pp/8/1PPPPP1P/RNBQKBNR b KQkq g3 0 3")

print(split_locations, "turn:", turn, "castling:", castling,"en_passant:", en_passant,"halfmove:", halfmove_clock,"fullmove:", fullmove_number)