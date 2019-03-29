import copy

import constants as c

class BASE():

    def __init__(self, type):

        self.type = type

        self.Set_Color()

        self.Set_Position()

    def Send_To(self,simulator):

        simulator.send_sphere( position = self.position ,

            color = self.color ) 

# -------------- Private methods ---------------

    def Set_Color(self):

        self.color         = c.colors[self.type]

    def Set_Position(self):

        self.position      = copy.deepcopy( c.offsets[self.type] )

        self.position[c.z] = self.position[c.z] + c.legRadius + c.legLength
