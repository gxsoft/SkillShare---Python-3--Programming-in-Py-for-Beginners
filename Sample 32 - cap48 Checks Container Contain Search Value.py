"""
  Sample 32 - cap48 Checks Container Contain Search Value.py

  Check if Container contains a searched VALUE
atters
"""

import time
import reaGab as rg
import reaGab as g


"""
# Begin gab routines // IMPORT reaGab.py
def title(text,aste):
   width       = len(text)+4
   if len(aste)==0:
      aste        = '*'
   line        = '\n'+aste*width+'\n'
   print(line,aste,' ',text,' ',aste,line,sep='')

def line():
    dash       = '-'
    print(dash*50)   
# End gab routines
"""

program        = 'Sample 32 - cap48 Checks Container Contain Search Value.py'
def performance(func, arg, times =1):
   sum         = 0
   for i in range(0, times):
      start       = time.perf_counter()
      func(arg)
      end         = time.perf_counter()
      sum         = sum + (end-start)
   return sum


setContainer      = {i for i in range(1000)}
listContainer     = [i for i in range(1000)]

def is_value_in(value):
   if value in listContainer:
      return True
   else:
      return False

def is_value_inSet(value):
   if value in setContainer:
      return True
   else:
      return False

def is_value_in2(value):
   return True if (value in listContainer) else False



times       = 500_000   
rg.line('-')
rg.title(program,'')
rg.title('Performace 2','')
print('   1: ',performance(is_value_in2, 1,times))
print(' 500: ',performance(is_value_in2, 500,times))
print('1000: ',performance(is_value_in2, 1000,times))
print('1500: ',performance(is_value_in2, 1500,times))
rg.title('Performace 1','')
print('   1: ',performance(is_value_in, 1,times))
print(' 500: ',performance(is_value_in, 500,times))
print('1000: ',performance(is_value_in, 1000,times))
print('1500: ',performance(is_value_in, 1500,times))
rg.title('Performace 2','')
print('   1: ',performance(is_value_in2, 1,times))
print(' 500: ',performance(is_value_in2, 500,times))
print('1000: ',performance(is_value_in2, 1000,times))
print('1500: ',performance(is_value_in2, 1500,times))
rg.title('Performace inSet ','')
print('   1: ',performance(is_value_inSet, 1,times))
print(' 500: ',performance(is_value_inSet, 500,times))
print('1000: ',performance(is_value_inSet, 1000,times))
print('1500: ',performance(is_value_inSet, 1500,times))



rg.line('-')
g.title("   End   ",'')







