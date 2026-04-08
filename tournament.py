#Minimax vs Random, record numbers of wins for X(minimax) and O(random), and number of draws and put it on a table
from game import TicTacToe
from minimax_agent_ab import minimax
import random
import mcts_agent
import matplotlib.pyplot as plt
import numpy as np
import time


def play_game(agent_x, agent_o):
    games = TicTacToe()
    while not games.is_terminal():
        if games.current_player == 1:
            move = agent_x(games)
            games = games.make_move(move)
        else:
            move = agent_o(games)
            games = games.make_move(move)

    return games.utility()


#MTCs with 1000 iterations vs Random, record numbers of wins for X(MCTS) and O(random), and number of draws and put it on a table
def random_agent(state):
    legal_moves = state.get_legal_moves()
    return random.choice(legal_moves)


def measure_time(agent, num_moves=100):
    total_time = 0
    for _ in range(num_moves):
        start_time = time.time()
        move = agent(TicTacToe())
        total_time += time.time() - start_time
    return total_time / num_moves


def measure_time_mcts(agent, num_moves=100, iterations=1000):
    total_time = 0
    for _ in range(num_moves):
        start_time = time.time()
        move = agent(TicTacToe())
        total_time += time.time() - start_time
    return total_time / num_moves


def display_mcts_times(times, iterations):
    plt.plot(times, iterations, color = 'green',
         linestyle = 'solid', marker = 'o',
         markerfacecolor = 'red', markersize = 12)
    plt.title("Iterations vs Average Time Per Move (s)")
    plt.xlabel("Average Time per Move(s)")
    plt.ylabel("Iterations")
    plt.show()


# functions for playing against the user:
def play_game_agent(agent_x):
    games = TicTacToe()
    while not games.is_terminal():
        if games.current_player == 1:
            move = agent_x(games)
            games = games.make_move(move)
        else:
            games.display()
            print("Enter your move:")
            move = input()
            valid = False
            while not valid:
                if int(move) not in games.get_legal_moves() or int(move) < 0 or int(move) > 8:
                    print("Invalid move. Please try another value.")
                    print(games.get_legal_moves())
                    move = input()
                else:
                    valid = True

            games = games.make_move(int(move))
            
    games.display()

    return games.utility()

def play_game_user(agent_x):
    games = TicTacToe()
    while not games.is_terminal():
        if games.current_player == 1:
            games.display()
            print("Enter your move:")
            move = input()
            valid = False
            while not valid:
                if int(move) not in games.get_legal_moves() or int(move) < 0 or int(move) > 8:
                    print("Invalid move. Please try another value.")
                    print(games.get_legal_moves())
                    move = input()
                else:
                    valid = True

            games = games.make_move(int(move))
        else:
            move = agent_x(games)
            games = games.make_move(move)
            
    games.display()

    return games.utility()


def main():
    num_games = 100
    results = {'Minimax vs Random': {'X wins': 0, 'O wins': 0, 'Draws': 0},
               'MCTS vs Random': {'X wins': 0, 'O wins': 0, 'Draws': 0},
               'Minimax vs MCTS': {'X wins': 0, 'O wins': 0, 'Draws': 0},
               'MCTS vs Minimax': {'X wins': 0, 'O wins': 0, 'Draws': 0}}
    
    print("\nCompute time comparisons?")
    user_choice = input()
    if user_choice == "Y" or  user_choice == "y" or user_choice == "Yes" or user_choice =="yes":
        print("\nAverage time per move:")
        print(f"Minimax: {measure_time(minimax):.4f} seconds")
        print(f"MCTS: {measure_time(mcts_agent.mcts):.4f} seconds")
        print(f"Random: {measure_time(random_agent):.4f} seconds")

        avg_100 = measure_time_mcts(mcts_agent.mcts, iterations=100)
        avg_500 = measure_time_mcts(mcts_agent.mcts, iterations=500)
        avg_1000 = measure_time_mcts(mcts_agent.mcts, iterations=1000)
        avg_5000 = measure_time_mcts(mcts_agent.mcts, iterations=5000)
        avg_10000 = measure_time_mcts(mcts_agent.mcts, iterations=10000)
        iterations = [100, 500, 1000, 5000, 10000]
        times = [avg_100, avg_500, avg_1000, avg_5000, avg_10000]

        print("\n\nAverage time per move for various MCTS agents:")
        print(f"MCTS with 100 iterations: {avg_100:.4f} seconds")
        print(f"MCTS with 500 iterations: {avg_500:.4f} seconds")
        print(f"MCTS with 1000 iterations: {avg_1000:.4f} seconds")
        print(f"MCTS with 5000 iterations: {avg_5000:.4f} seconds")
        print(f"MCTS with 10000 iterations: {avg_10000:.4f} seconds")
        display_mcts_times(times, iterations)


    print("\nBegin tournament?")
    user_choice = input()
    if user_choice != "Y" and user_choice != "y" and user_choice != "Yes" and user_choice !="yes":
        return

    for _ in range(num_games):
        result = play_game(minimax, random_agent)
        if result == 1:
            results['Minimax vs Random']['X wins'] += 1
        elif result == -1:
            results['Minimax vs Random']['O wins'] += 1
        else:
            results['Minimax vs Random']['Draws'] += 1

    for _ in range(num_games):
        result = play_game(mcts_agent.mcts, random_agent)
        if result == 1:
            results['MCTS vs Random']['X wins'] += 1
        elif result == -1:
            results['MCTS vs Random']['O wins'] += 1
        else:
            results['MCTS vs Random']['Draws'] += 1

    for _ in range(num_games):
        result = play_game(minimax, mcts_agent.mcts)
        if result == 1:
            results['Minimax vs MCTS']['X wins'] +=1
        elif result == -1:
            results['Minimax vs MCTS']['O wins'] += 1
        else:
            results['Minimax vs MCTS']['Draws'] += 1

    for _ in range(num_games):
        result = play_game(mcts_agent.mcts, minimax)
        if result == 1:
            results['MCTS vs Minimax']['X wins'] += 1
        elif result == -1:
            results['MCTS vs Minimax']['O wins'] += 1
        else:
            results['MCTS vs Minimax']['Draws'] += 1

    # Print results in a  table format
    print(f"{'Matchup':20} {'X wins':10} {'O wins':10} {'Draws':10}")
    for matchup, stats in results.items():
        print(f"{matchup:20} {stats['X wins']:10} {stats['O wins']:10} {stats['Draws']:10}")



if __name__ == "__main__":    
    main()
