"""
Sample 15 -DATA Structures (Nested Types (SDT)).py

"""

name     = "Gabriel"
age      = 58
sex      = "man"

name2    = "Jessica"
age2     = 25
sex2     = "woman"

name3    = "John"
age3     = 32
sex3     = "man"

person1  = ["Gabriel", 58, "man"]
person2  = ["Jessica", 25, "woman"]
person3  = ["John", 32, "man"]

guestList =[
               ["Gabriel", 58, "man"],
               ["Jessica", 25, "woman"],
               ["John", 32, "man"]
           ]
print('-------------- Nested List ---------')

print('guestList =[\n\
               ["Gabriel", 58, "man"],\n\
               ["Jessica", 25, "woman"],\n\
               ["John", 32, "man"]\n\
           ]')
print(guestList)
print('-------------- SubIndication ---------')
print('print(guestList[0])')
print(guestList[0])
print('-')
print('print(guestList[0][0])')
print(guestList[0][0])
print('print(guestList[1][2])')
print(guestList[1][2])
guestList.append(["Spphie", 12, "woman"])
print(guestList)
