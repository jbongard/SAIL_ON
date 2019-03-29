import constants as c

from robot import ROBOT

class SWARM():

    def __init__(self):

        self.swarm = {}

        for r in range(0,c.populationSize):

            self.swarm[r] = ROBOT()

    def Get_Robot(self,r):

        if r in self.swarm:

            return r

        else:
            return None
 
    def Print(self):

        for r in self.swarm:

            self.swarm[r].Print()
