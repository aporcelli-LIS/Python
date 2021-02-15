<<<<<<< Updated upstream
from typing import Tuple


def insert_string_middle(str,word):
    return str[:2] + word + str[2:] 
print("Enter foster name")
x=input()
print(x)
y=input('Enter lenght of time')
print(y)
print(insert_string_middle('',x))
print(insert_string_middle('','will be fostered for'))
print(insert_string_middle('',y))
=======
def insert_string_middle(str,word):
    return str[:2] + word + str[2:] 
print("Enter foster name")
x=input()
print(x)
y=input('Enter length of time')
print(y)
print(insert_string_middle('',x),'will be fostered for',y )
>>>>>>> Stashed changes
