class Env(object):
    def __init__(self, size, cliff, start, goal):
        """
        Parameters:
            - size ((x: int, y: int) tuple): area of environment
            - cliff (((x: int, y: int), (x: int, y: int)) tuple of rect coords)
                region of cliff
            - start ((x: int, y: int) tuple): initial position
            - goal ((x: int, y: int) tuple): goal position
        """

        self.size = size
        self.cliff = cliff
        self.goal = goal

        self.pos = start

        # TODO: Create datastructure to hold env
    
    def get_actions(self, p):
        """
        Get possible actions for a given position (p)
        """
        pass

    def transition(self, a):
        """
        Get updated position from taking given action (a)
        """
        pass

    def reward(self, p):
        """
        Get reward for moving to given position (p)
        """
        pass