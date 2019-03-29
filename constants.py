import math


adversary = 0

defender  = 1

robotTypeNames = {

adversary : "adversary" ,

defender  : "defender"

}

bodyLength = 1

bodyRadius = 0.2 * bodyLength

legLength  = 0.5 * bodyLength

legRadius  = 0.1 * bodyLength

legAnglesInRadians = {

0: 0 , 

1: 0.5 * math.pi , 

2: 1.0 * math.pi ,

3: 1.5 * math.pi

}

numLegs = len(legAnglesInRadians)

upperLeg = 0

lowerLeg = 1

colors = {

adversary: [1,0,0] ,

defender:  [0,0,1]

}

offsets = {

adversary: [+bodyLength , 0, 0] ,

defender:  [-bodyLength , 0, 0]

}

x = 0

y = 1

z = 2

