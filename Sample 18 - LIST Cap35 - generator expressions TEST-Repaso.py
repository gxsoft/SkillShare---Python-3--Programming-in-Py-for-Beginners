import sys

"""
Sample 18 - LIST - generator expressions.py
"""
evenNumbers = [item
              for item in range(101)
              if (item %2 == 0)
              ]
evenNumbersGenerator = (item
                       for item in range(101)
                       if (item %2 == 0)
                       )

print(evenNumbers)
print("--------")
print("--- print(evenNumbersGenerator) -----")
print(evenNumbersGenerator)


print(next(evenNumbersGenerator))
print(next(evenNumbersGenerator))
print(next(evenNumbersGenerator))


evenNumbersGenerator = (item
                       for item in range(101)
                       if (item %2 == 0)
                       )

for odd in evenNumbersGenerator:
   print(odd)




   
