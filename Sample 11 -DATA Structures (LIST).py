"""
Sample 11 - DATA Structures (LIST).py
# ------------------------------------------
# Whats is list?
# HoW to with Lists...
# ------------------------------------------
Is a GROUP of Elements...
String, numbers, and so on
"""
names    = ["Ruben","Gabriel", "Ana", "Santiago", "MariaEmilia"]
number   = [1,2,3,4,5]
z        = 0
for i in names:
    print (number[z],i)
    z       += 1

print (names[-1]) # Last Element of one list is [-1]


# Whats is list?
# in
# not in
# operation on list
# ---------------------

print('---------------')
print('"Gabriel" in names: ')
print("Gabriel"in names)


# Function for LISTs
# len() - lenght
# .append - adding at the end single element
# .extend - extending list by another list 
# .insert(index, what) - put in
# .index(what] - return index of what
# sort(reverse=false) - sort ascending
# max()
# min()
# .count() - how many occurences (how many times it shows up)
# .pop - pop last element (remove)
# .remove - remove first occurrence (first time it shows up)
# .clear - cleart entire list
# .reverse - change the order
# ---------------------
print('---------------')
print('# Function for LISTs')
print('---------------')

list1    = [1,2,3,4,5,7,8,9]
list2    = ["Ruben","Gabriel", "Ana", "Santiago", "MariaEmilia"]


print(len(list1))
list1.append(10)
print(len(list1))
print(list1)
#list1.extend(list2)
#print(list1)

print(list1 + list2) # Very MUCH LOWER THAN EXTEND

list1.insert(0,0)
print(list1)

print(list2.index("Gabriel"))

list1.sort(reverse=True)
list2.sort()
print(list1)
print(list2)
print(max(list1),min(list2))
#
#
#

print("print(list1.count(4)):",list1.count(4))

