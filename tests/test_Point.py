import unittest
from src.models.Point import Point


class Test_Point(unittest.TestCase):

    def setUp(self) -> None:
        
        self.p1 = Point(0,1,3)
        self.p2 = Point(1,4,6)
        self.p3 = Point(3,5,8)
        self.data = [self.p1,self.p2, self.p3]

    def tearDown(self):
        pass

    def test_createpoint(self):
        self.p4 = Point(12,56,48)
        self.assertTrue(self.p4.getT() == 12)
        self.assertTrue(self.p4.getX() == 56)
        self.assertTrue(self.p4.getY() == 48)
        
    def test_editpoint(self):
        self.p1.setT(10)
        self.p1.setX(2)
        self.p1.setY(4)
        self.assertTrue(self.p1.getT() == 10)
        self.assertTrue(self.p1.getX() == 2)
        self.assertTrue(self.p1.getY() == 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)