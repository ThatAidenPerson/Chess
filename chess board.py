import pygame
import chess, stockfish

pygame.init()

# set up the window
size = (840, 840)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")



# set up the board
board = pygame.Surface((800, 800))
board_grid = {
    "a1": {"value": "a1", "position": [[800, 800], [100, 100]]},
    "a2": {"value": "a2", "position": [[800, 700], [100, 100]]},
    "a3": {"value": "a3", "position": [[800, 600], [100, 100]]},
    "a4": {"value": "a4", "position": [[800, 500], [100, 100]]},
    "a5": {"value": "a5", "position": [[800, 400], [100, 100]]},
    "a6": {"value": "a6", "position": [[800, 300], [100, 100]]},
    "a7": {"value": "a7", "position": [[800, 200], [100, 100]]},
    "a8": {"value": "a8", "position": [[800, 100], [100, 100]]},
    "b1": {"value": "b1", "position": [[700, 800], [100, 100]]},
    "b2": {"value": "b2", "position": [[700, 700], [100, 100]]},
    "b3": {"value": "b3", "position": [[700, 600], [100, 100]]},
    "b4": {"value": "b4", "position": [[700, 500], [100, 100]]},
    "b5": {"value": "b5", "position": [[700, 400], [100, 100]]},
    "b6": {"value": "b6", "position": [[700, 300], [100, 100]]},
    "b7": {"value": "b7", "position": [[700, 200], [100, 100]]},
    "b8": {"value": "b8", "position": [[700, 100], [100, 100]]},
    "c1": {"value": "c1", "position": [[600, 800], [100, 100]]},
    "c2": {"value": "c2", "position": [[600, 700], [100, 100]]},
    "c3": {"value": "c3", "position": [[600, 600], [100, 100]]},
    "c4": {"value": "c4", "position": [[600, 500], [100, 100]]},
    "c5": {"value": "c5", "position": [[600, 400], [100, 100]]},
    "c6": {"value": "c6", "position": [[600, 300], [100, 100]]},
    "c7": {"value": "c7", "position": [[600, 200], [100, 100]]},
    "c8": {"value": "c8", "position": [[600, 100], [100, 100]]},
    "d1": {"value": "d1", "position": [[500, 800], [100, 100]]},
    "d2": {"value": "d2", "position": [[500, 700], [100, 100]]},
    "d3": {"value": "d3", "position": [[500, 600], [100, 100]]},
    "d4": {"value": "d4", "position": [[500, 500], [100, 100]]},
    "d5": {"value": "d5", "position": [[500, 400], [100, 100]]},
    "d6": {"value": "d6", "position": [[500, 300], [100, 100]]},
    "d7": {"value": "d7", "position": [[500, 200], [100, 100]]},
    "d8": {"value": "d8", "position": [[500, 100], [100, 100]]},
    "e1": {"value": "e1", "position": [[400, 800], [100, 100]]},
    "e2": {"value": "e2", "position": [[400, 700], [100, 100]]},
    "e3": {"value": "e3", "position": [[400, 600], [100, 100]]},
    "e4": {"value": "e4", "position": [[400, 500], [100, 100]]},
    "e5": {"value": "e5", "position": [[400, 400], [100, 100]]},
    "e6": {"value": "e6", "position": [[400, 300], [100, 100]]},
    "e7": {"value": "e7", "position": [[400, 200], [100, 100]]},
    "e8": {"value": "e8", "position": [[400, 100], [100, 100]]},
    "f1": {"value": "f1", "position": [[300, 800], [100, 100]]},
    "f2": {"value": "f2", "position": [[300, 700], [100, 100]]},
    "f3": {"value": "f3", "position": [[300, 600], [100, 100]]},
    "f4": {"value": "f4", "position": [[300, 500], [100, 100]]},
    "f5": {"value": "f5", "position": [[300, 400], [100, 100]]},
    "f6": {"value": "f6", "position": [[300, 300], [100, 100]]},
    "f7": {"value": "f7", "position": [[300, 200], [100, 100]]},
    "f8": {"value": "f8", "position": [[300, 100], [100, 100]]},
    "g1": {"value": "g1", "position": [[200, 800], [100, 100]]},
    "g2": {"value": "g2", "position": [[200, 700], [100, 100]]},
    "g3": {"value": "g3", "position": [[200, 600], [100, 100]]},
    "g4": {"value": "g4", "position": [[200, 500], [100, 100]]},
    "g5": {"value": "g5", "position": [[200, 400], [100, 100]]},
    "g6": {"value": "g6", "position": [[200, 300], [100, 100]]},
    "g7": {"value": "g7", "position": [[200, 200], [100, 100]]},
    "g8": {"value": "g8", "position": [[200, 100], [100, 100]]},
    "h1": {"value": "h1", "position": [[100, 800], [100, 100]]},
    "h2": {"value": "h2", "position": [[100, 700], [100, 100]]},
    "h3": {"value": "h3", "position": [[100, 600], [100, 100]]},
    "h4": {"value": "h4", "position": [[100, 500], [100, 100]]},
    "h5": {"value": "h5", "position": [[100, 400], [100, 100]]},
    "h6": {"value": "h6", "position": [[100, 300], [100, 100]]},
    "h7": {"value": "h7", "position": [[100, 200], [100, 100]]},
    "h8": {"value": "h8", "position": [[100, 100], [100, 100]]}
}

"""uci_names = [
    "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
    "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
    "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
    "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
    "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
    "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
    "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"
             ]"""
# draws the board with alternating colours for the squares

for square, data in board_grid.items():
    position = data["position"]
    value = data["value"]
    x, y = position[0][0] - 100, position[0][1] - 100
    width, height = position[1][0], position[1][1]

    a1 = pygame.Rect(x, y, width, height)
    a2 = pygame.Rect(x, y, width, height)
    a3 = pygame.Rect(x, y, width, height)
    a4 = pygame.Rect(x, y, width, height)
    a5 = pygame.Rect(x, y, width, height)
    a6 = pygame.Rect(x, y, width, height)
    a7 = pygame.Rect(x, y, width, height)
    a8 = pygame.Rect(x, y, width, height)
    b1 = pygame.Rect(x, y, width, height)
    b2 = pygame.Rect(x, y, width, height)
    b3 = pygame.Rect(x, y, width, height)
    b4 = pygame.Rect(x, y, width, height)
    b5 = pygame.Rect(x, y, width, height)
    b6 = pygame.Rect(x, y, width, height)
    b7 = pygame.Rect(x, y, width, height)
    b8 = pygame.Rect(x, y, width, height)
    c1 = pygame.Rect(x, y, width, height)
    c2 = pygame.Rect(x, y, width, height)
    c3 = pygame.Rect(x, y, width, height)
    c4 = pygame.Rect(x, y, width, height)
    c5 = pygame.Rect(x, y, width, height)
    c6 = pygame.Rect(x, y, width, height)
    c7 = pygame.Rect(x, y, width, height)
    c8 = pygame.Rect(x, y, width, height)
    d1 = pygame.Rect(x, y, width, height)
    d2 = pygame.Rect(x, y, width, height)
    d3 = pygame.Rect(x, y, width, height)
    d4 = pygame.Rect(x, y, width, height)
    d5 = pygame.Rect(x, y, width, height)
    d6 = pygame.Rect(x, y, width, height)
    d7 = pygame.Rect(x, y, width, height)
    d8 = pygame.Rect(x, y, width, height)
    e1 = pygame.Rect(x, y, width, height)
    e2 = pygame.Rect(x, y, width, height)
    e3 = pygame.Rect(x, y, width, height)
    e4 = pygame.Rect(x, y, width, height)
    e5 = pygame.Rect(x, y, width, height)
    e6 = pygame.Rect(x, y, width, height)
    e7 = pygame.Rect(x, y, width, height)
    e8 = pygame.Rect(x, y, width, height)
    f1 = pygame.Rect(x, y, width, height)
    f2 = pygame.Rect(x, y, width, height)
    f3 = pygame.Rect(x, y, width, height)
    f4 = pygame.Rect(x, y, width, height)
    f5 = pygame.Rect(x, y, width, height)
    f6 = pygame.Rect(x, y, width, height)
    f7 = pygame.Rect(x, y, width, height)
    f8 = pygame.Rect(x, y, width, height)
    g1 = pygame.Rect(x, y, width, height)
    g2 = pygame.Rect(x, y, width, height)
    g3 = pygame.Rect(x, y, width, height)
    g4 = pygame.Rect(x, y, width, height)
    g5 = pygame.Rect(x, y, width, height)
    g6 = pygame.Rect(x, y, width, height)
    g7 = pygame.Rect(x, y, width, height)
    g8 = pygame.Rect(x, y, width, height)
    h1 = pygame.Rect(x, y, width, height)
    h2 = pygame.Rect(x, y, width, height)
    h3 = pygame.Rect(x, y, width, height)
    h4 = pygame.Rect(x, y, width, height)
    h5 = pygame.Rect(x, y, width, height)
    h6 = pygame.Rect(x, y, width, height)
    h7 = pygame.Rect(x, y, width, height)
    h8 = pygame.Rect(x, y, width, height)
    

    color = (255, 206, 158) if (x + y) % 2 == 0 else (210, 180, 140)
    pygame.draw.rect(board, color, (x, y, width, height))
    font = pygame.font.Font(None, 16)
    text = font.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
    board.blit(text, text_rect)


    




# add the board to the screen
screen.blit(board, (20, 20))
pygame.display.flip()

# setting up the pieces
pieces = {
    "white_pawn": pygame.image.load(r"Pieces/white_pawn.png"),
    "white_rook": pygame.image.load(r"Pieces/white_rook.png"),
    "white_knight": pygame.image.load(r"Pieces/white_knight.png"),
    "white_bishop": pygame.image.load(r"Pieces/white_bishop.png"),
    "white_queen": pygame.image.load(r"Pieces/white_queen.png"),
    "white_king": pygame.image.load(r"Pieces/white_king.png"),
    "black_pawn": pygame.image.load(r"Pieces/black_pawn.png"),
    "black_rook": pygame.image.load(r"Pieces/black_rook.png"),
    "black_knight": pygame.image.load(r"Pieces/black_knight.png"),
    "black_bishop": pygame.image.load(r"Pieces/black_bishop.png"),
    "black_queen": pygame.image.load(r"Pieces/black_queen.png"),
    "black_king": pygame.image.load(r"Pieces/black_king.png")
}


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    