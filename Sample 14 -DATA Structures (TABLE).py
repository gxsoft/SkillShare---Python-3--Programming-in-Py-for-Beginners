"""
Sample 13 -DATA Structures (Dictionary - TUPLE).py
# ------------------------------------------
# Whats is TUPLE? and difference with LIST
# Dictionary
# ------------------------------------------
# Similar to TUPLE is UNMUTABLE,
The TUPLE is unmutable, FASTER and TAKE LESS MEMORY than LIST[]
"""

tuple    = 1,2,3,4,5

# Differences, we don't be able to change list
# unchangable.

print(tuple)
tuple    = (1,2,3,4,5)
print(tuple)

rooms       = {49:'Gabriel Medina', 50:'Silvia Marioli'}
print(rooms[49])
print(rooms)
rooms.update({123:"Ciento Veinti Tres",1234:"MilDoscientos TreintaYCuatro"})
rooms.update({222:"Doscientos Ventidos"})
print(rooms)
del(rooms[123])
rooms.pop(222)
print(rooms)
rooms.popitem()
print(rooms)

rooms.clear()
print(rooms)











