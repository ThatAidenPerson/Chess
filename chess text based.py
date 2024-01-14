import chess
from stockfish import Stockfish
import os, time

# Initializes an empty chess board
board = chess.Board()
stockfish = Stockfish(r"C:\stockfish\stockfish-windows-x86-64-avx2.exe")
fen = board.fen() 

# variables for other things
forfiet = ["forfiet", "quit", "exit", "surrender", "give up", "resign"]
player_name = input("What is your name? ").title()


def print_board():
    print(board)
    print("-----------------")
    print("A B C D E F G H")
    print("It is " + who_turn +"'s turn.")

def game_with_bot():    
    while board.is_checkmate() == False:
        turn = board.turn
        who_turn = player_name

        print_board()
        move = input("Enter a move: ").lower()

        if move.strip() == "":
            print("Invalid move. Try again.")
            continue
        elif move in forfiet:
            print("You have forfieted the game. Bot wins!")
            break
        elif chess.Move.from_uci(move) in board.legal_moves:
            board.push_uci(move)
            fen = board.fen()
            turn = board.turn
            os.system("cls")
        else:
            print("Invalid move. Try again.")
            continue
        
        print("It is the bot's turn...")
        time.sleep(1)

        stockfish.set_fen_position(fen)
        best_move = stockfish.get_best_move()
        board.push_uci(best_move)
        
        if board.is_checkmate() == True:
            if turn == True:
                print("Checkmate, Bot wins!")
            else:
                print("Checkmate, you win!")
            break
        
game_with_bot()

    







