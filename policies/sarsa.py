from .policy import Policy

class SARSA(Policy):
    def __init__(self, start, alpha, epsilon, gamma, n_states, n_actions):
        super().__init__(start, alpha, epsilon, gamma, n_states, n_actions)

    def update(self, s_0, a_0, r, s_1, a_1):
        #TODO: implement
        pass