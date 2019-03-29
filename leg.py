import constants as c

from legPart import LEG_PART

class LEG():

    def __init__(self,robotType,legIndex):

        self.legParts = {}

        self.legParts[c.upperLeg] = LEG_PART(robotType,legIndex,c.upperLeg)

        self.legParts[c.lowerLeg] = LEG_PART(robotType,legIndex,c.lowerLeg)

    def Send_To(self,simulator):

        for legPart in self.legParts:

            self.legParts[legPart].Send_To(simulator)

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

