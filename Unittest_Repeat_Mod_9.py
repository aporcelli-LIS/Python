import itertools
import operator
import copy

Pets={"Cassanova", "Foxy Fenny", "Lightning"}
#pet names
for i in itertools.repeat(Pets,5):
    print(i)   


import unittest
import copy

class TestCopy(unittest.TestCase):

    def test_copy(self):
        self.assertEqual(Pets,5)

if __name__ == '__main__':
    unittest.main()