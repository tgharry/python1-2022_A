import unittest
from md5 import *

class SyllablesTest(unittest.TestCase):

    def test_1(self):
        self.assertGreater(md5("ab"), "")

    def test_2(self):
        self.assertGreater(md5("text"), "")
    def test_3(self):
        self.assertGreater(md5("reaper"), "")
    def test_4(self):
        self.assertGreater(md5("leaper"), "")
    def test_5(self):
        self.assertGreater(md5("beaper"), "")
    def test_6(self):
        self.assertGreater(md5("weater"), "")



if __name__ == '__main__':
    unittest.main()
