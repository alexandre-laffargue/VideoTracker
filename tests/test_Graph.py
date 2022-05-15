import unittest
from src.models.Graph import Graph
from src.models.Point import Point

class Test_Point(unittest.TestCase):

    def setUp(self) -> None:
        self.p1 = Point(0,1,3)
        self.p2 = Point(1,4,6)
        self.p3 = Point(3,5,8)
        self.data = [self.p1,self.p2, self.p3]
        self.coef = 3
        self.graph = Graph(None, self.data, self.coef, None)

    def tearDown(self):
        pass

    def test_splitcoord(self):
        self.graph.createtab()
        self.assertTrue(self.data[0].getT() == self.graph.t[0])
        self.assertTrue(self.data[1].getX()*self.coef  == self.graph.x[1])
        self.assertTrue(self.data[2].getY()*self.coef == self.graph.y[2])


if __name__ == '__main__':
    unittest.main(verbosity=2)