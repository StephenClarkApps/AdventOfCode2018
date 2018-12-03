import re

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

print (GetPrediction(line).id)
