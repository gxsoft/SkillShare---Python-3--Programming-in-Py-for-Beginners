"""
Sample 09 - Break LOOP.py
# ------------------------------------------
# break (leaves loop enterely)
# continue (leaves current interation (repetition of loop) and CONTINUE)
# ------------------------------------------
result   = 0
for i in range(3):
   x        = int(input("Enter a positive number: "))
   if (x > 0):
      result      += x
   print("Current addition result = ", result)
"""

"""
result   = 0  
for i in range(3):
   x        = int(input("Enter a positive number: "))
   if (x > 0):
      result      += x
   else:
      print("I expected positive number, you gave a negative number, you are a bad boy")
      break
   print("Current addition result = ", result)


result   = 0  
for i in range(3):
   x        = int(input("Enter a positive number: "))
   if (x > 0):
      result      += x
   else:
      print("I expected positive number, you gave a negative number, you are a bad boy")
      continue
   print("Current addition result = ", result)
"""

#CONTINUE makes sense in this CASE
result   = 0
i        = 0
while i < 3:
   x        = int(input("Enter a positive number: "))
   if (x > 0):
      result      += x
   else:
      print("I expected positive number, you gave a negative number, you are a bad boy")
      continue
   print("Current addition result = ", result)
   i        += 1
