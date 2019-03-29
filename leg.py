from legPart import LEG_PART

import constants as c

import copy

import math

class LEG():

    def __init__(self,robotType,index):

        self.lowerLeg = LEG_PART(robotType,index,c.lower)

        self.upperLeg = LEG_PART(robotType,index,c.upper)

        exit()

        self.robotType = robotType

        self.index = index

        self.Set_Angle()

        self.Set_Color()

        self.Set_Position()

        self.Set_Orientation()

    def Send_To(self,simulator):

        simulator.send_cylinder( \

            position = self.position ,

            orientation = self.orientation ,

            length = c.legLength , 

            radius = c.legRadius ,

            color = self.color )

# -------------- Private methods ---------------

    def Set_Angle(self):

        self.angle         = c.legAnglesInRadians[self.index]

    def Set_Color(self):

        self.color         = c.colors[self.type]

    def Set_Orientation(self):

        self.orientation = [0,0,0]

        self.orientation[c.x] = math.sin(self.angle)

        self.orientation[c.y] = math.cos(self.angle)

    def Set_Position(self):

        self.position      = copy.deepcopy( c.offsets[self.type] )

        self.position[c.x] = self.position[c.x] + c.legLength * math.sin(self.angle)

        self.position[c.y] = self.position[c.y] + c.legLength * math.cos(self.angle) 

        self.position[c.z] = self.position[c.z] + c.legRadius + c.legLength

