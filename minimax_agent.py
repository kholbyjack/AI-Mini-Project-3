import game
counter = 0

def minimax(state):
    # Return the best move for the current player.
    if state.current_player == 1:
        best_value = float('-inf')
        best_move = None
        for move in state.get_legal_moves():
            child = state.make_move(move)
            value = min_value(child)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move
    else:
        # TODO: implement the symmetric case
        # for MIN.
        worst_value = float('inf')
        worst_move = None
        for move in state.get_legal_moves():
            child = state.make_move(move)
            value = max_value(child)
            if value < worst_value:
                worst_value = value
                worst_move = move
        return worst_move

def max_value(state):
    global counter 
    counter += 1
    # base case: the game is over
    if state.is_terminal():
        return state.utility()
    v = float('-inf')
    for move in state.get_legal_moves():
        child = state.make_move(move)
        v = max(v, min_value(child))
    return v
    
def min_value(state):
    # minimizing 
    global counter 
    counter += 1
    # base case: the game is over
    if state.is_terminal():
        return state.utility()
    v = float('inf')
    for move in state.get_legal_moves():
        child = state.make_move(move)
        v = min(v, max_value(child))
    return v


def play_game_mini(agent_x):
    games = game.TicTacToe()
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
    games = game.TicTacToe()
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

def mini_v_mini(agent_x, agent_o):
    games = game.TicTacToe()
    while not games.is_terminal():
        if games.current_player == 1:
            move = agent_x(games)
            games = games.make_move(move)
        else:
            move = agent_o(games)
            games = games.make_move(move)
            
    games.display()

    return games.utility()


def main():
    state = game.TicTacToe()

    # ----- TESTING -----
    print("\nFrom empty board:")
    move = minimax(state)
    new_state = state.make_move(move)
    new_state.display()
    print(f"Mini-max chosen move: {move}")
    
    print("\nSecond Condition:")
    state = state.make_move(4)
    state = state.make_move(2)
    best = minimax(state)
    print(f"Mini-max chosen move: {move}")
    state = state.make_move(best)
    state.display()
    print(f"Count results: {counter}")

    print("MiniMax vs. MiniMax:")
    result = mini_v_mini(minimax, minimax)
    print("Results from Mini vs. Mini:")
    if result == 1:
        print("X won")
    elif result == -1:
        print("O won")
    else:
        print("Draw.")

    print("Play as X or O?")
    user_choice = input()

    if user_choice == "X" or user_choice == "x":
        results_userX = play_game_user(minimax)
        if results_userX == 1:
            print("Congratulations! You won.")
        elif results_userX == -1:
            print("Minimax won.")
        else:
            print("Draw.")
    elif user_choice == "O" or user_choice == "o":
        result1 = play_game_mini(minimax)
        if result1 == 1:
            print("Minimax won.")
        elif result1 == -1:
            print("Congratulations! You won.")
        else:
            print("Draw.")

    


    # TESTING
    # print(counter)
    # state = state.make_move(4)
    # state = state.make_move(2)
    # best = minimax(state)
    # print(best)
    # print(counter)
    # state = state.make_move(best)
    # state.display()
    # print(counter)

    # best = minimax(state)
    # state = state.make_move(best)
    # state.display()
    # print(counter)
    

if __name__ == "__main__":
    main()