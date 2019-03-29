import constants as c

from environment import ENVIRONMENT 

class ENVIRONMENTS():

    def __init__(self):

        self.environments = {}

        for e in range(0,c.numEnvironments):

            self.environments[e] = ENVIRONMENT()

    def Print(self):

        for e in self.environments:

            self.environments[e].Print()
