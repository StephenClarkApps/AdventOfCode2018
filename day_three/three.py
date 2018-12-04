import re
from collections import defaultdict

grid = defaultdict(int)

class Predition:
    def __init__(self, id, left, top, height, width):
        self.id = id
        self.left = left
        self.top = top
        self.height = height
        self.width = width

#line = ("#1 @ 912,277: 27x20")

def GetPrediction(some_string):
    extracted = re.findall(r"\w+",some_string)
    id = int(extracted[0])
    left = int(extracted[1])
    top = int(extracted[2])
    height_and_width = re.split(r'(\d+)', extracted[3])
    height = int(height_and_width[1])
    width = int(height_and_width[3])
    return Predition(id, left, top, height, width)


input = open('input.txt').readlines()

for row in input:
    pred = GetPrediction(row)
    for dx in range(pred.width):
        for dy in range(pred.height):
            grid[(pred.left + dy, pred.top + dx)] +=1

overlap_total = 0
for (r,c),value in grid.items():
    if value >= 2:
        overlap_total += 1

print (overlap_total)

for row in input:
    pred = GetPrediction(row)
    is_it = True
    for dx in range(pred.width):
        for dy in range(pred.height):
            if grid[(pred.left + dy, pred.top + dx)] > 1:
                is_it = False
    if is_it:
        print (pred.id)
