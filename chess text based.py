import chess
from stockfish import Stockfish
import os, time

# Initializes an empty chess board
board = chess.Board()
stockfish = Stockfish(r"M:\stockfish\stockfish-windows-x86-64-avx2.exe")
fen = board.fen() 

# variables for other things
forfiet = ["forfiet", "quit", "exit", "surrender", "give up", "resign"]
vs_bot = ["bot", "computer", "ai", "stockfish", "1"]
vs_player = ["player", "human", "2"]

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
            b_or_w = input(f"Who would you like to play as white or black? (1: {player_name}, 2: {player_name2})").title()
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
            break
        elif chess.Move.from_uci(move) in board.legal_moves:
            board.push_uci(move)
            fen = board.fen()
            turn = board.turn
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
            else:
                print("Checkmate, White wins!")
            break


game()





