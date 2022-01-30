from time import time
# string of characters
a = "Seyyon"
print(type(a))
print(a+a)
# integer
a = 5
print(type(a))
print(a*a)
a = 10
print(a*a)

def test(a):
    print("value of a:", a)
    return a

import os

b = test(5)
print("value of b:", b)
print(os.getcwd())
print(time())
