import unittest
from src.models.Point import Point
from src.models.FileRepo import FileRepo

class Test_filerepo(unittest.TestCase):

    def setUp(self) -> None:
        
        self.p1 = Point(0,1,3)
        self.p2 = Point(1,4,6)
        self.p3 = Point(3,5,8)
        self.data = [self.p1,self.p2, self.p3]
        self.file = FileRepo(self.data, "filetest", 1)
        self.file4 = FileRepo(self.data, "filetest", 4)

    def tearDown(self):
        pass

    def test_transform2str(self):
        csv = self.file.TransformData2CSV(self.data)
        self.assertEqual(csv, "0;1;3\n1;4;6\n3;5;8\n")

    def test_export(self):
        self.file.export2CSV(self.data,"test")
        csv = open("test.csv", "r")
        self.assertEqual(csv.read() , "0;1;3\n1;4;6\n3;5;8\n")
        csv.close()

    def test_transform2strwithscale(self):
        csv = self.file4.TransformData2CSV(self.data)
        self.assertEqual(csv, "0;4;12\n1;16;24\n3;20;32\n")

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    