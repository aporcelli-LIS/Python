import itertools
import operator
import copy
  

foster_pets = ['Squeak', 'Siracha', 'Tilly', 'Andy']
#2020 pets fostered from SPCA

foster_mouse = copy.deepcopy(foster_pets) 
#Deep copy to ensure changes to foster_pets does not result in changes to the deep copies

foster_pets[0]=('Mary')
#Changed the name 'Squeak' to 'Mary' in the foster_pets list

print(foster_pets)
print(foster_mouse) 

x=foster_mouse 
#Test to ensure deep copy properties
print(x)