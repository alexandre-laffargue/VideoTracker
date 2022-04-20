from random import randint
import sys
sys.path.append("../VideoTracker/src/models")
from Point import Point


def randomPoints(n:int)->list:
    l = []
    for i in range(n):
        pt = Point(randint(-1000,1000),randint(-1000,1000))
        l.append(pt)
    return l



t = randomPoints(4)
print(t[0].getX())
print(t[0].getY())