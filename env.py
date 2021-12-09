import numpy as np

class Env:
    def __init__(self, size, cliff, start, goal):
        """
        Parameters:
            - size ((x: int, y: int) tuple): area of environment
            - cliff (((x: int, y: int), (x: int, y: int)) tuple of rect coords)
                region of cliff
            - start ((x: int, y: int) tuple): initial position
            - goal ((x: int, y: int) tuple): goal position
        """
        self.start = start
        self.end = False
        self.size = size
        self.cliff = cliff
        self.goal = goal

        self.pos = start
        
        self.playSpace = np.zeros(size[0],size[1])          #Creating playspace , cliff denoted as -1
        for i in range(cliff[0][0], cliff[1][0]):
            for j in range (cliff[0][1], cliff[1][1]):
                self.playSpace[i,j] = -1

        # TODO: Create datastructure to hold env
    
    def get_actions(self, p):
        """
        Get possible actions for a given position (p)
        """
        return ["up", "down", "left", "right"]
        

    def transition(self, a):
        """
        Get updated position from taking given action (a)
        """
        if a == "left":
            nextPosition = (self.pos[0] - 1, self.pos[1])
        elif a == "right":
            nextPosition = (self.pos[0] + 1, self.pos[1])
        elif a == "up":
            nextPosition = (self.pos[0], self.pos[1] + 1)
        else:
            nextPosition = (self.pos[0], self.pos[1] - 1)
        
        if nextPosition[0] >= 0 and nextPosition[0] < self.size[0]:
            if nextPosition[1] >= 0 and nextPosition[0] < self.size[1]:
                self.pos = nextPosition
        
        if self.playSpace[self.pos] == -1:
            self.pos = self.start
        
        if self.pos == self.goal:
            self.end = True

        return self.pos

    def reward(self, p):
        """
        Get reward for moving to given position (p)
        """
        if self.pos == self.goal or self.playSpace[self.pos] == 0:
            return -1
        return -100