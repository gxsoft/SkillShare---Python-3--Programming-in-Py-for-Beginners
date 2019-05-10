"""
   Sample 29 - cap45 Mesure Performance of Code.py

"""
import time # include perf_counter() -> float


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

def sumUp4b(end):
   xgen   = (num for num in range(1,end+1))
   return sum(xgen)



xx          = 125
xx          = 999999
#xx          = 125

start       = time.perf_counter()
print('CASO 1: print(sumUp1(xx))',sumUp1(xx))
end         = time.perf_counter()
print(' '*5,(end - start)*1000)

start       = time.perf_counter()
print('CASO 2: print(sumUp2(xx))',sumUp2(xx))
end         = time.perf_counter()
print(' '*5,(end - start)*1000)

start       = time.perf_counter()
print('CASO 3: print(sumUp3(xx))',sumUp3(xx))
end         = time.perf_counter()
print(' '*5,(end - start)*1000)

start       = time.perf_counter()
print('CASO 4: print(sumUp1(xx))',sumUp4(xx))
end         = time.perf_counter()
print(' '*5,(end - start)*1000)

start       = time.perf_counter()
print('CASO 4B: print(sumUp1(xx))',sumUp4b(xx))
end         = time.perf_counter()

print(' '*5,(end - start)*1000)
start       = time.perf_counter()
print('CASO 5: print(sumUp1(xx))',sumUp5(xx))
end         = time.perf_counter()
print(' '*5,(end - start)*1000)




