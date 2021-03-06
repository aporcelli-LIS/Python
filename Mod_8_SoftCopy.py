import copy 

foster_pets = [['Squeak', 'Siracha'], ['Tilly', 'Andy']]
#2020 pets fostered from SPCA

foster_pocketpets= copy.copy(foster_pets)
#Soft copy of original foster_pets list

foster_pets[1][1] = ['Bun Bun']
#Replace the name 'Andy' to 'Bun Bun' in the original foster_pet list

print(foster_pets)
print(foster_pocketpets) 

x=foster_pocketpets
#Test to ensure soft copy properties
print(x) 