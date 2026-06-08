import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    V = np.zeros(n_states)
    returns_sum, returns_count = np.zeros(n_states), np.zeros(n_states)

    for episode in episodes:
        G =0
        n = len(episode)
        returns = [0]*n
        for i in range(n-1, -1, -1):
            _, reward = episode[i]
            G = reward + gamma*G
            returns[i] = G
            
        visited = set()
        for i, (state, _) in enumerate(episode): 
            if state not in visited:
               returns_sum[state] += returns[i]
               returns_count[state] += 1
               visited.add(state)
    
    for i in range(n_states):
        if returns_count[i]>0:
            V[i] = returns_sum[i]/returns_count[i]
            
    return V
    