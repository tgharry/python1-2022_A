import unittest
from solution_10_06 import encoder, decoder

class SyllablesTest(unittest.TestCase):
    def test_1(self):
        self.assertGreater(encoder("abcd"), "")

    def test_2(self):
        self.assertGreater(encoder("test"), "")

    def test_3(self):
        self.assertGreater(encoder("retry"), "")

    def test_4(self):
        self.assertEquals(decoder("ceast"), "ceast")

    def test_5(self):
        self.assertEquals(decoder("beast"), "beast")

    def test_6(self):
        self.assertEquals(decoder("least"), "least")

    def test_(self):
        self.assertEquals(decoder("toast"), "toast")

if __name__ == '__main__':
    unittest.main()
