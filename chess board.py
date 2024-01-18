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

# draws the board with alternating colorsches
#for x in range(0, 8): # --> for x in range(start, stop, step):
    #for y in range(0, 8):
        #color = (255, 206, 158) if (x + y) % 2 == 0 else (210, 180, 140)
        #pygame.draw.rect(board, color, (x * 100, y * 100, 100, 100))


for square, data in board_grid.items():
    position = data["position"]
    value = data["value"]
    x, y = position[0][0] - 100, position[0][1] - 100
    width, height = position[1][0], position[1][1]
    color = (255, 206, 158) if (x + y) % 2 == 0 else (210, 180, 140)
    pygame.draw.rect(board, color, (x, y, width, height))
    font = pygame.font.Font(None, 16)
    text = font.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
    board.blit(text, text_rect)


# add the board to the screen
screen.blit(board, (20, 20))

pygame.display.flip()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    