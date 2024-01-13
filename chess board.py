import pygame
import chess, stockfish

pygame.init()

# set up the window
size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")

# set up the board
board = pygame.Surface((600, 600))
board.fill((255, 206, 158))

# draws the board with alternating colorsches
for x in range(0, 8, 2): # --> for x in range(start, stop, step):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75)) # --> pygame.draw.rect(screen, (r, g, b), (x, y, width, height))
        pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

# add the board to the screen
screen.blit(board, (20, 20))

pygame.display.flip()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    