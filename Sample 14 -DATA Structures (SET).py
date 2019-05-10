"""
Sample 14 -DATA Structures (SET).py
# ------------------------------------------
# Whats is SET? 
#
               Unique  |
LISTS            
TUPLES
DICTIONARIES
SETS

"""

A        = {40, -2, 20, 13}
B        = {4, 7, 10, 20}
print(A|B)

A.add(24)
print(A)
print(sorted(A))


A        = [40, -2, 20, 13, 40]
print(A)
A        = set([40, -2, 20, 13, 40])


""""
REMOVE, DISCARD
# A.remove(40)
""""

A.discard(-2)
print(A)
# A.remove(40)
print(A)
