import itertools
import operator
import copy

foster_pets = {'Squeak', 'Siracha', 'Tilly', 'Andy'}
#2020 pets fostered from SPCA

foster_mouse = copy.deepcopy(foster_pets) 
#Deep copy to ensure foster_pets remains unchanged

foster_mouse.add('Mary')
#Add foster mouse 'Mary' to original foster_pets list

print(foster_mouse)
print(foster_pets)

foster_pocketpets= copy.copy(foster_pets)
#Soft copy to alter original foster_pets list

foster_pocketpets.remove('Tilly')
#Remove 'Tilly' from the original foster_pet list
print(foster_pocketpets)


print(foster_pocketpets)
print(foster_pets) 


foster_pets = (['Squeak'], ['Siracha'], ['Tilly'], ['Andy'])
#2020 pets fostered from SPCA
r = copy.copy(foster_pets) 
x = copy.copy(foster_pets)

r= (foster_pets(3)) = "45"
#Remove 'Tilly' from the original foster_pet list
print(r)
print(foster_pets)

x [0] = "Mary"
print(x)
print(foster_pets) 
