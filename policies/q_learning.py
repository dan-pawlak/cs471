from .policy import Policy

class QLearning(Policy):
    def __init__(self, start, alpha, epsilon, gamma, n_states, n_actions):
        super().__init__(start, alpha, epsilon, gamma, n_states, n_actions)
    
    def update(self, s_0, a, r, s_1):
        #TODO: implement
        pass