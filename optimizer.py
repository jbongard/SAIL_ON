from environments import ENVIRONMENTS

from simulator import SIMULATOR

from swarm import SWARM

class OPTIMIZER():

    def __init__(self):

        self.environments = ENVIRONMENTS()

        self.swarm = SWARM()

    def Optimize(self):

        simulator = SIMULATOR()

        simulator.Add( self.swarm.Get_Robot(0) )

        simulator.Add( self.swarm.Get_Robot(1) )

        simulator.Simulate()

    def Print(self):

        self.environments.Print()

        self.swarm.Print()

