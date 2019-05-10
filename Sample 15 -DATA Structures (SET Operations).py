"""
Sample 15 -DATA Structures (SET).py

# ------------------------------------------
# Whats is SET? 
#
               Unique  |
LISTS            
TUPLES
DICTIONARIES
SETS
#       A.remove(40)

SET Operations
        |: Union
        &: Intersection
        -: Difference
        ^: XOR exclusive OR (removing intersectcion from union)
"""

A        = {1, 2, 3, 4, 50, 80}
B        = {1, 2, 50, 60, 70, 80, 90}

print("Set A: ",A)
print("Set B: ",B)
print("=== Operations ==== ")

print("Union A|B: ",A|B)
print("Intersection A&B: ",A&B)
print("Difference A-B: ",A-B)
print("XOR A^B: ",A^B)
#
# ------------------
#
print("=== Operations FUNCTIONS () ==== ")

print("Union A|B: ",A.union(B))
print("Intersection A&B: ",A.intersection(B))
print("Difference A-B: ",A.difference(B))
print("XOR A^B: ",A.symmetric_difference(B))

