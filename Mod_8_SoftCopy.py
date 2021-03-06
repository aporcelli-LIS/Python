import copy 

foster_pets = [['Squeak', 'Siracha'], ['Tilly', 'Andy']]
#2020 pets fostered from SPCA

foster_pocketpets= copy.copy(foster_pets)
#Soft copy to alter original foster_pets list

foster_pets[1][1] = ['Bun Bun']
#Remove 'Tilly' from the original foster_pet list


print(foster_pets)
print(foster_pocketpets) 

x=foster_pocketpets
print(x)