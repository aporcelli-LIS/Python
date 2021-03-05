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