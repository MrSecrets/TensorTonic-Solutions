def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    markov = []
    states = len(values)
    for s in range(states):
        q = []
        for a in range(len(transitions[s])):
            expected = rewards[s][a]
            for s_next in range(states):
                curr = transitions[s][a][s_next]*values[s_next]
                expected += gamma*curr
            q.append(expected)
        markov.append(max(q))

    return markov