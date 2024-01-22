import chess

board = chess.Board("rnbqk2r/ppp2ppp/3p1n2/4p3/1bP1P3/2N3P1/PP1P1P1P/R1BQKBNR w KQkq - 0 5")
fen = board.fen()

split_fen = fen.split()

print(fen)
print(split_fen)

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

        
for l in split_locations:
    print(l)
