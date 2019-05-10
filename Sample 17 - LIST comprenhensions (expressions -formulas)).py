"""
Sample 17 - LIST comprenhensions (expressions -formulas)).py
"""
numbers        = [1, 2, 3, 4, 5, 6]
poweredNumbers = []
for num in numbers:
   poweredNumbers.append(num**2)

evenNumbers    =[]
for num in numbers:
   if (num % 2 == 0):
      evenNumbers.append(num)
   
print("i  | Power2")
print("---|------")
for i in numbers:
      print(i," |",poweredNumbers[i-1])
         
print("---|------")
for i in evenNumbers:
      print(i," |","odd")
#--------------
print("")
print("-----  FASTED Ways! ---------")
print("")
powerNumbers2 = [num**2 for num in numbers]
print(powerNumbers2)
powerNumbers3 = [num**3
                 for num in numbers
                 if (num % 2 == 0)
                 ]
print(powerNumbers3)
"""
[Whet_to_do_on_item | for item in old_list | conditions based on intem] 
"""
powerNumbers4 = [item**2
                 for item in range(51)
                 ]
print(powerNumbers4)
