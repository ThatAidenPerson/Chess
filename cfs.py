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
    
    
    for i in split_fen[0]:
        print(i)
        if i.isalpha() and level < 8:
            split_locations[level].append(i)
        elif i.isdigit() and level < 8: # •
            for _ in range(int(i)):
                split_locations[level].append("•")
        elif i == "/": #and level < 7:
            level += 1
        
    turn = split_fen[1]
    castling = split_fen[2]
    en_passant = split_fen[3]
    halfmove_clock = split_fen[4]
    fullmove_number = split_fen[5]

    return split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number

def revert_fen(split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number):
    fen = ""
    for i in split_locations:
        count = 0
        for y in i:
            if y.isalpha():
                if count > 0:
                    fen += str(count)
                    count = 0
                fen += y
            elif y == "•":
                count += 1
        if count > 0:
            fen += str(count)
        fen += "/"
        
    fen = fen[:-1] + " " + turn + " " + castling + " " + en_passant + " " + halfmove_clock + " " + fullmove_number
    return fen



split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number = setup_board("rnbqkbnr/ppppppp1/8/P7/6Pp/8/1PPPPP1P/RNBQKBNR b KQkq g3 0 3")
fen = revert_fen(split_locations, turn, castling, en_passant, halfmove_clock, fullmove_number)

print(split_locations, "turn:", turn, "castling:", castling,"en_passant:", en_passant,"halfmove:", halfmove_clock,"fullmove:", fullmove_number, "fen:", fen)