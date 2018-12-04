import re

grid = {}

class Predition:
    def __init__(self, id, left, top, height, width):
        self.id = id
        self.left = left
        self.top = top
        self.height = height
        self.width = width


line = ("#1 @ 912,277: 27x20")


def GetPrediction(some_string):
    extracted = re.findall(r"\w+",some_string)
    id = extracted[0]
    left = extracted[1]
    top = extracted[2]
    height_and_width = re.split(r'(\d+)', extracted[3])
    height = height_and_width[1]
    width = height_and_width[3]
    return Predition(id, left, top, height, width)

def CreateSetOfCoordinatesFromPrediction(prediction):
    theXCoordinates = []
    theYCoordinates = []
    xcounter = 0
    ycounter = 0

    width_int = int(prediction.width)
    height_int = int(prediction.height)

    for x in range(width_int):
        theXCoordinates.append(int(prediction.left) + xcounter)
        xcounter += 1
    for y in range(height_int):
        theYCoordinates.append(int(prediction.top) + ycounter)
        ycounter += 1

    #acount = 0
    #bcount = 0
    #for a in range(len(theXCoordinates)):
        #acount += 1
        #for b in range (len(theYCoordinates)):
            #grid[a] = b
            #bcount += 1

    print (str(theXCoordinates))
    print (str(theYCoordinates))
    #print (grid)

pred = GetPrediction(line)
CreateSetOfCoordinatesFromPrediction(pred)
