"""
Sample 10 - Exercise GUESS Numer.py
# ------------------------------------------
# GUESS NUMBER
#
# ------------------------------------------
"""

secretNumber   = 40
guessedNumber  = 0
print("")
print("")
print("")
while guessedNumber != secretNumber:
   guessedNumber   = int(input("Guess the secretNumber between 1 & 100: "))
   if guessedNumber > secretNumber:
      print("Nope, lower!")
   else:
      if guessedNumber != secretNumber:
         print("Nope, upper!")

print("Yes, you are RIGHT!")
