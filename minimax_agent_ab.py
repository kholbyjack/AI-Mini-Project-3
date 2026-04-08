import game

node_count = 0  # counts nodes evaluated by Minimax / Alpha-Beta
pruned_count = 0  # counts nodes skipped due to alpha-beta pruned

def minimax(state):
    # Return the best move for the current player.
    if state.current_player == 1:
        best_value = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for move in state.get_legal_moves():
            child = state.make_move(move)
            value = min_value_ab(child, alpha, beta)
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
        return best_move
    
    else:
        worst_value = float('inf')
        worst_move = None
        alpha = float('-inf')
        beta = float('inf')

        for move in state.get_legal_moves():
            child = state.make_move(move)
            value = max_value_ab(child, alpha, beta)
            if value < worst_value:
                worst_value = value
                worst_move = move
            beta = min(beta, worst_value)
        return worst_move

def max_value_ab(state, alpha, beta):
    # possible moves are cut off when v>=beta
    global node_count, pruned_count
    node_count+=1 # update node counter everytime

    if state.is_terminal():
        return state.utility()
    
    v = float('-inf')
    for move in state.get_legal_moves():
        child = state.make_move(move)
        v = max(v, min_value_ab(child, alpha, beta))
        if v >= beta:
            pruned_count += len(state.get_legal_moves()) - (state.get_legal_moves().index(move) + 1)
            return v
        alpha = max(alpha, v)
    return v
    
def min_value_ab(state, alpha, beta):
    # possible moves are cut off when v<=alpha
    global node_count, pruned_count
    node_count+=1 # update node counter everytime

    if state.is_terminal():
        return state.utility()
    
    v = float('inf')
    for move in state.get_legal_moves():
        child = state.make_move(move)
        v = min(v, max_value_ab(child, alpha, beta))
        if v <= alpha:
            pruned_count += len(state.get_legal_moves()) - (state.get_legal_moves().index(move) + 1) # pruned_pct = (prune_count / prune_count + node_count) * 100
            return v
        beta = min(beta, v)
    return v


def main():
    state = game.TicTacToe()

    state = state.make_move(4)
    state = state.make_move(2)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    best = minimax(state)
    print(best)
    state = state.make_move(best)
    state.display()
    print(f"Node count: {node_count}")
    print(f"Pruned count: {pruned_count}")
    percent_pruned = (pruned_count / (node_count + pruned_count)) * 100
    print(f"Percentage pruned: {percent_pruned:.2f}%")



if __name__ == "__main__":
    main()
