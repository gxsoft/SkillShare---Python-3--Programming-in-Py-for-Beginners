"""
   Sample 28 - cap44 Arithmetic Sequence.py

   Write program, that will count the sum of all numbers from 1 to X, that was entered by user
"""

title       = 'Program, that will count the sum of all numbers from 1 to X'
line        = '-'*len(title)
print('',line,'\n',title,'\n',line)
x           = int(input(' Enter X: '))

geneX       = (item
               for item in range(1,x+1)
               )

listX       = [item 
               for item in range(1,x+1)
               ]
print(listX)
print('The sum of all number of 1 to [',x,'] is:',sum(listX))

i           = 0
suma        = 0
for item in listX:
   suma        = suma + item
   i           = i + 1
   print(i,':',suma)


def sumUp1(end):
   sum      = 0
   for num in range(1, end+1):
      sum      = sum + num
   return sum

def sumUp2(end):
   return sum([num for num in range(1,end+1)])
   
def sumUp3(end):
   return sum({num for num in range(1,end+1)})

def sumUp4(end):
   return sum((num for num in range(1,end+1)))

def sumUp5(end):
   return (1 + end) / 2 * end



print(sumUp1(125))
print(sumUp2(125))
print(sumUp3(125))
print(sumUp4(125))
print(sumUp5(125))

