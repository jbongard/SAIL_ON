import constants as c

from robot import ROBOT

class SWARM():

    def __init__(self):

        self.swarm = {}

        self.swarm[0] = self.Create_Adversary()

        self.swarm[1] = self.Create_Defender()

    def Send_To(self,simulator):

        for r in self.swarm:

            self.swarm[r].Send_To(simulator)

    def Get_Robot(self,r):

        if r in self.swarm:

            return r

        else:
            return None
 
    def Print(self):

        for r in self.swarm:

            self.swarm[r].Print()

# ----------------- Private methods ----------------------

    def Create_Adversary(self):

        return ROBOT(c.adversary)

    def Create_Defender(self):

        return ROBOT(c.defender)

