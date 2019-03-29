import constants as c

from base import BASE

from leg import LEG

class ROBOT():

    def __init__(self , type):

        self.type = type

        self.Create_Base()

        self.Create_Legs()

    def Print(self):

        print("I am a " + c.robotTypeNames[self.type] + "." )

    def Send_To(self,simulator):

        self.Send_Legs_To(simulator)

        self.Send_Base_To(simulator)

# ----------- Private methods --------------

    def Create_Base(self):

        self.base = BASE( self.type )

    def Create_Legs(self):

        self.legs = {}

        for l in range(0,c.numLegs):

            self.legs[l] = LEG( self.type , l )

    def Send_Base_To(self,simulator):

        self.base.Send_To(simulator) 

    def Send_Legs_To(self,simulator):

        for l in self.legs:

            self.legs[l].Send_To(simulator)
