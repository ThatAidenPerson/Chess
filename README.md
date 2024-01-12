This is me learning how to use the libraries chess and stockfish, which are both going to eventually be used to make a chess game
The reason I am making this is because in my college chess is blocked by the firewall, and because I enjoy chess, I want to play it, so I am going to make it in python using pygame.

I am learning the two libraries in two different files, and once I know the syntax and generally how to use it, I will try to use it together to make an ascii game of chess, which after I will put it together in pygame to be able to play chess well.

First thing to know is how the Forsyth–Edwards Notation (FEN) works, bellow is how the fields work.

A FEN record contains six fields, each separated by a space. The fields are as follows:

    Piece placement data: Each rank is described, starting with rank 8 and ending with rank 1, with a "/" between each one; within each rank, the contents of the squares are described in order from the a-file to the h-file. Each piece is identified by a single letter taken from the standard English names in algebraic notation (pawn = "P", knight = "N", bishop = "B", rook = "R", queen = "Q" and king = "K"). White pieces are designated using uppercase letters ("PNBRQK"), while black pieces use lowercase letters ("pnbrqk"). A set of one or more consecutive empty squares within a rank is denoted by a digit from "1" to "8", corresponding to the number of squares.
    
    Active color: "w" means that White is to move; "b" means that Black is to move.
    
    Castling availability: If neither side has the ability to castle, this field uses the character "-". Otherwise, this field contains one or more letters: "K" if White can castle kingside, "Q" if White can castle queenside, "k" if Black can castle kingside, and "q" if Black can castle queenside. A situation that temporarily prevents castling does not prevent the use of this notation.
    
    En passant target square: This is a square over which a pawn has just passed while moving two squares; it is given in algebraic notation. If there is no en passant target square, this field uses the character "-". This is recorded regardless of whether there is a pawn in position to capture en passant. An updated version of the spec has since made it so the target square is recorded only if a legal en passant capture is possible, but the old version of the standard is the one most commonly used.

    Halfmove clock: The number of halfmoves since the last capture or pawn advance, used for the fifty-move rule.
    
    Fullmove number: The number of the full moves. It starts at 1 and is incremented after Black's move.