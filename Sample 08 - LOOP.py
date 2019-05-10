"""
Sample 08 - LOOP.py
# ------------------------------------------
# 
# ------------------------------------------
"""
number      = 0
# number   = int(input("Give me the number: "))


while number <= 5:
   print(number)
   number   += 1
   
"""
number      = 0
for i in range(4):
   print("(",i,")")
   nr      = int(input("Give me the number: "))
   number += nr

print("The result of adding numbers is: ", number)
"""

for i in [0,1,2,3,4]:
   print(i)
   
for i in range(15):
   print(i, "modulo 2 :",i%2)
   if (i%2 == 0):
      print(i," is even number")
