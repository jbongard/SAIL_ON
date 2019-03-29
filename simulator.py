import pyrosim

class SIMULATOR():

    def __init__(self):

        self.sim = pyrosim.Simulator(play_paused=True)

    def Get_Simulator(self):

        return self.sim

    def Simulate(self):

        self.sim.start()

        self.sim.wait_to_finish()

