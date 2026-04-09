# allows the user to play against one of three agents
from tournament import play_game_agent, play_game_user
from minimax_agent import  minimax
from mcts_agent import mcts
import minimax_agent_ab

def play_game(agent, agent_name, user_piece_choice):
     if user_piece_choice == "X" or user_piece_choice == "x":
        results_userX = play_game_user(agent)
        if results_userX == 1:
            print("Congratulations! You won.")
        elif results_userX == -1:
            print(f"{agent_name} won.")
        else:
            print("Draw.")
     elif user_piece_choice == "O" or user_piece_choice == "o":
        result1 = play_game_agent(agent)
        if result1 == 1:
            print(f"{agent_name} won.")
        elif result1 == -1:
            print("Congratulations! You won.")
        else:
            print("Draw.")

def main():
    # 
    possible_mini = ["1", "MM", "mm", "minimax", "mini max", "MiniMax", "Mini Max"]
    possible_miniAB = ["2", "MMAB", "mmab", "mini max with AB pruning", "MiniMaxAB", "minimaxab", "pruning", "Pruning"]
    possible_mcts = ["3", "MCTS", "mcts", "monte carlo", "Monte Carlo", "Monte Carlo Search Tree"]
    possible_no = ["No", "no", "N", "n", "No ", "no ", "Nah", "nah"]
    play = True

    while play:
        # getting user's opponent and position
        print("Choose your opponent from the following:")
        print("1 for minimax \n2 for minimax with AB pruning \n3 for MCTS")
        user_opponent_choice = input()

        print("Choose your piece (X or O)")
        user_piece_choice = input()

        if user_opponent_choice in possible_mini:
            play_game(minimax, "MiniMax", user_piece_choice)

        elif user_opponent_choice in possible_miniAB:
            play_game(minimax_agent_ab.minimax, "MiniMaxAB", user_piece_choice)

        elif user_opponent_choice in possible_mcts:
            play_game(mcts, "MCTS", user_piece_choice)

        print("Play again?")
        play_choice = input()

        if play_choice in possible_no:
            play = False


if __name__ == "__main__":
    main()