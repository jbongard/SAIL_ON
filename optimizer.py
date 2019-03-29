from environments import ENVIRONMENTS

from simulator import SIMULATOR

from swarm import SWARM

class OPTIMIZER():

    def __init__(self):

        self.swarm = SWARM()

    def Optimize(self):

        simulator = SIMULATOR()

        self.swarm.Send_To( simulator.Get_Simulator() )

        simulator.Simulate()

    def Print(self):

        self.swarm.Print()

