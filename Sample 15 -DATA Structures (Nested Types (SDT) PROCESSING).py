"""
Sample 15 -DATA Structures (Nested Types (SDT)).py

"""

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

"""     """


guestList =[
               ["Gabriel", 58, "man", "+54 358 423 9372"],
               ["Jessica", 25, "woman", "+54 358 423 9372"],
               ["John", 32, "man", "+54 358 423 9372"]
           ]
print("Guest List:")
i        = 0
for name,age,sex,cell in guestList:
   i        += 1
   print("Guest Number (",i,")")
   print("Name....:", name)
   print("Age.....:", age)
   print("Sex.....:", sex)
   print("Sex.....:", sex)
   print("---------------")

# ---------- Dictonary with LABELS -----------------------
guestList ={
             '1': {'name': "Gabriel", 'age':58, 'sex':"man",'cell': "+54 358 423 9372"},
             '2':   {'name': "Jessica", 'age':25, 'sex':"woman",'cell': "+54 358 423 9372"},
             '3':   {'name': "John", 'age':32, 'sex':"man",'cell': "+54 358 423 9372"}
           }
print("print(guestList['1']")
print(guestList['1'])
print("---------------")
print()
print()

print()
print()



for key in guestList:
   print('Guest List(',key,'): ')
   print(guestList[key]) 
print("--------------- Secondary KEY")
print()
print()

for key in guestList:
   print('Guest List(',key,'): ')
   for key2 in guestList[key]:
      print(key2)
print()
print()

print("--------------- Element in Secondary KEY")
for key in guestList:
   print('Guest List(',key,'): ')
   for key2 in guestList[key]:
       print("   ",key2,":",guestList[key][key2])   

print("---------------")
print()
print("print(guestList.items())")
print(guestList.items())
print("---------------")
print()
print()
print("for Id, dictionary in guestList.items():")
print("   for Attribute in dictionary:")
print('       print("   ",Attribute,":",dictionary[Attribute])   for Id, dictionary in guestList.items():')
for Id, dictionary in guestList.items():
   print('Guest List(',Id,'): ')
   for Attribute in dictionary:
       print("   ",Attribute,"...:",dictionary[Attribute])   


      



       
