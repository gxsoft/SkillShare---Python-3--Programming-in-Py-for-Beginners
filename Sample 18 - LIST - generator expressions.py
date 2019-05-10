import sys

"""
Sample 18 - LIST - generator expressions.py
"""
evenNumbers = [item
              for item in range(4401)
              if (item %2 == 0)
              ]
evenNumbersGenerator = (item
                       for item in range(4401)
                       if (item %2 == 0)
                       )

print(evenNumbers)
print("--------")
print("--- print(evenNumbersGenerator) -----")
print(evenNumbersGenerator)
print("sum(evenNumbersGenerator)", sum(evenNumbersGenerator))


print("sys.getsizeof(evenNumbers):",sys.getsizeof(evenNumbers))
print("sys.getsizeof(evenNumbersGenerator):",sys.getsizeof(evenNumbersGenerator))
print("-- End version 23:03------")

#print("--- print(next(evenNumbersGenerator)) two times-----")
#print(next(evenNumbersGenerator))
#print(next(evenNumbersGenerator))




print("--------")
print("--- print IN evenNumbersGenerator  -----")
for n in evenNumbersGenerator:
   print(n)

"""
FOR EXAMPLE
When you need work with a file of  1 TeraByte of size
"""
