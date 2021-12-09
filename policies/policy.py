from abc import ABC, abstractmethod
import numpy as np

class Policy(ABC):
    def __init__(self, start, alpha, epsilon, gamma, n_states, n_actions):
        """
        Properties:
            - start (float): Inital conditions of policy
            - alpha (float): Learning rate
            - epsilon (float): Exploration factor
            - gamma (float): Discount factor
            - n_states (int): Number of potential states
            - n_actions (int): Number of potential actions
        """
        self.start = start
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.q = np.zeros((n_states, n_actions))

    @abstractmethod
    def update(self):
        """
        Update Q table using chosen policy.
        """
        raise NotImplementedError