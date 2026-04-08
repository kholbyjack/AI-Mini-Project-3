# allows the user to play against one of three agents
from tournament import play_game_agent, play_game_user
from minimax_agent import  minimax
from mcts_agent import mcts
import minimax_agent_ab


def main():
    # 
    print("Choose your opponent (minimax, minimax with AB pruning, or MCTS)")
    user_opponent_choice = input()

    print("Choose your piece (X or O)")
    user_piece_choice = input()

    if user_opponent_choice == "minimax" or user_opponent_choice == "MM":
        if user_piece_choice == "X" or user_piece_choice == "x":
            results_userX = play_game_user(minimax)
            if results_userX == 1:
                print("Congratulations! You won.")
            elif results_userX == -1:
                print("Minimax won.")
            else:
                print("Draw.")
        elif user_piece_choice == "O" or user_piece_choice == "o":
            result1 = play_game_agent(minimax)
            if result1 == 1:
                print("Minimax won.")
            elif result1 == -1:
                print("Congratulations! You won.")
            else:
                print("Draw.")

    elif user_opponent_choice == "minimaxab" or user_opponent_choice == "MMAB":
        if user_piece_choice == "X" or user_piece_choice == "x":
            results_userX = play_game_user(minimax_agent_ab.minimax)
            if results_userX == 1:
                print("Congratulations! You won.")
            elif results_userX == -1:
                print("Minimax won.")
            else:
                print("Draw.")
        elif user_piece_choice == "O" or user_piece_choice == "o":
            result1 = play_game_agent(minimax_agent_ab.minimax)
            if result1 == 1:
                print("Minimax won.")
            elif result1 == -1:
                print("Congratulations! You won.")
            else:
                print("Draw.")

    elif user_opponent_choice == "MCTS":
        if user_piece_choice == "X" or user_piece_choice == "x":
            result = play_game_user(mcts)
            if result == 1:
                print("Congratulations! You won.")
            elif result == -1:
                print("MCTS won.")
            else:
                print("Draw.")
        elif user_piece_choice == "O" or user_piece_choice =="o":
            user_result = play_game_agent(mcts)
            if user_result == 1:
                print("MCTS won.")
            elif user_result == -1:
                print("Congratulations! You won.")
            else:
                print("Draw.")


if __name__ == "__main__":
    main()