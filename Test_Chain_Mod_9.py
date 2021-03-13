import itertools
import operator
import copy

Chinchillas = {"Squeak","Siracha"}
Cats = {"Bean Sprout", "Chixpea","Lima","Pinto", "Cannoli", "Goblin", "Pumpkin"}
Rabbits = {"Bun Bun", "Petunia", "Tilly", "Andy"} 
Guinea_Pig = {"Gertrude"}
Mouse = {"Mary"} 

result = itertools.chain(Chinchillas,Cats,Rabbits,Guinea_Pig,Mouse)
for each in result:
    print(each) 


import unittest

class TestChainMethod(unittest.TestCase):

    def test_Variable_Assign(self):
        Mouse=object
        self.assertTrue(Mouse(),'Mary')

    def test_Variable_Assign7(self):
        Mouse=object
        self.assertTrue(Mouse(),'Rain')

    def test_Variable_Assign1(self):
        Guinea_Pig=object
        self.assertTrue(Guinea_Pig(),'Gertrude')

    def test_Variable_Assign2(self):
        Rabbits=object
        self.assertTrue(Rabbits(),"Bun Bun")

    def test_Variable_Assign3(self):
        Cats=object
        self.assertTrue(Cats(),"Bean Sprout")

    def test_Variable_Assign4(self):
        Chinchillas=object
        self.assertTrue(Chinchillas(),"Squeak")    

    def test_Chain(self):
        self.assertTrue(itertools.chain(), "Squeak")

    def test_Chain2(self):
        self.assertTrue(itertools.chain(), "Bob")
        
if __name__ == '__main__':
    unittest.main() 