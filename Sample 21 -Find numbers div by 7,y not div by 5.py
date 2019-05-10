import sys
"""
Sample 21 -Find numbers div by 7,y not div by 5.py
Numbers from 2 to 470...

What do you use?
   1) generators expressions¬
   2) list comprenhension
   3) set comprehension
   4) dictionary comprehension

Think for a sencond and make notes:

"is the answer to above question always the same?"

"""
# numeDiv7butNotDiv5
# 1) Generator Expressions
# ------------------------
numes       = (item
               for item in range(100)
               if (item % 7) == 0
               if (item % 5) != 0
               )
print(numes)
print(next(numes))

for nume in numes:
   print(nume)
print(" GENERETORS sys.getsizeof(numes): ",sys.getsizeof(numes))
print("-"*50)
print("")
# - LIST ----
#   2) list comprenhension
# ------------------------
numes       = [item
               for item in range(100)
               if (item % 7) == 0
               if (item % 5) != 0
               ]
print(numes)
print("LIST sys.getsizeof(numes): ",sys.getsizeof(numes))
print("-"*50)
print("")

# -- SETs --------
#   3) set comprehension
# ------------------------
numes       = {item
               for item in range(100)
               if (item % 7) == 0
               if (item % 5) != 0
               }
print(numes)
print("SET sys.getsizeof(numes): ",sys.getsizeof(numes))
print("-"*50)
print("")
# -- DICTIONARYs/ies --------
#   4) dictionary comprehension
numes       = {item:item
               for item in range(100)
               if (item % 7) == 0
               if (item % 5) != 0
               }
print(numes)
print("DICTIONARY/IES sys.getsizeof(numes): ",sys.getsizeof(numes))
print("-"*50)
print("")
