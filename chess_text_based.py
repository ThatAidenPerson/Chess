import chess, chess.pgn
from stockfish import Stockfish
import os, time
from datetime import datetime
# Initializes an empty chess board
board = chess.Board()
game = chess.pgn.Game()
node = game
stockfish = Stockfish(r"C:\stockfish\stockfish-windows-x86-64-avx2.exe") #for college, change to M at the start, for home, change to C
fen = board.fen() 

# variables for other things
forfiet = ["forfiet", "quit", "exit", "surrender", "give up", "resign"]
vs_bot = ["bot", "computer", "ai", "stockfish", "1"]
vs_player = ["player", "human", "2"]
who_turn = []

def set_headers(winner, white, black):
    node.headers["Event"] = "Chess Game"
    node.headers["Site"] = "Aiden's PyChess Game"
    node.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
    node.headers["Round"] = "To be determined"
    node.headers["White"] = white
    node.headers["Black"] = black
    node.headers["Result"] = winner

def print_board():
    print(board)
    print("-----------------")
    print("A B C D E F G H")
    fen = board.fen()
    print(fen)
    

def game():   
    
    player_name = input("What is your name? ").title()
    
    os.system("cls")
    print("Welcome to Chess, " + player_name + ".")
    game_mode = input("""What would you like to do? 
1. Play against a bot
2. Play against another player
""").lower()
    
    who_turn = player_name
    if game_mode in vs_player:
        player_name2 = input("What is the other player's name? ").title()
        while True:
            b_or_w = input(f"Who would you like to play as white? (1: {player_name}, 2: {player_name2})").title()
            if b_or_w in ["1", player_name]:
                who_turn = [player_name, player_name2]
                break
            elif b_or_w in ["2", player_name2]:
                who_turn = [player_name2, player_name]
                break
            else:
                print("Invalid input. Try again.")
                continue
            
            
    
    while True:
        
        turn = board.turn

        print_board()
        
        if board.turn == True and not game_mode in vs_bot:
            print(f"It is {who_turn[0]}'s turn.")
        elif board.turn == True and game_mode in vs_bot:
            print(f"It is your turn.")
        else:
            print(f"It is {who_turn[1]}'s turn.")
            
        move = input("Enter a move: ").lower()

        if move.strip() == "":
            print("Invalid move. Try again.")
            continue
        elif move in forfiet:   
            print("You have forfieted the game. You lose!")
            if turn == True:
                set_headers("0-1", who_turn[1], who_turn[0])
            else:
                set_headers("1-0", who_turn[0], who_turn[1])
            break
        elif chess.Move.from_uci(move) in board.legal_moves:
            board.push_uci(move)
            fen = board.fen()
            turn = board.turn
            game = node.add_variation(chess.Move.from_uci(move))
            os.system("cls")
        else:
            print("Invalid move. Try again.")
            continue
        
        if game_mode in vs_bot:
            print("It is the bot's turn...")
            time.sleep(1)
        
            stockfish.set_fen_position(fen)
            best_move = stockfish.get_best_move()
            board.push_uci(best_move)
        
        if board.is_checkmate() == True:
            if turn == True:
                print("Checkmate, Black wins!")
                set_headers("0-1", who_turn[1], who_turn[0])
            else:
                print("Checkmate, White wins!")
                set_headers("1-0", who_turn[0], who_turn[1])
            break
    
    # Save the game to a PGN file
    with open("game.pgn", "w") as pgn_file:
        print(game, file=pgn_file)


game()


# Set up something for when the game draws


