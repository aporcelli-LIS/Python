import itertools
import operator

# A Set of names
names = {"Steve", "Rick", "Negan"}
names2 = names

# adding a new element in the new set
names2.add("Glenn")

# removing an element from the old set
names.remove("Negan")
print(names)
print(names2)


# A Set of names
names = {"Steve", "Rick", "Negan"}

# copying using the copy() method
names2 = names.copy()

# adding "Glenn" to the new set
names2.add("Glenn")

# removing "Negan" from the old set
names.remove("Negan")

# displaying both the sets
print("Old Set is:", names)
print("New Set is:", names2)