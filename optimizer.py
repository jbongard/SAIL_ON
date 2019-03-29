from environments import ENVIRONMENTS

from swarm import SWARM

class OPTIMIZER():

    def __init__(self):

        self.environments = ENVIRONMENTS()

        self.swarm = SWARM()

    def Print(self):

        self.environments.Print()

        self.swarm.Print()

