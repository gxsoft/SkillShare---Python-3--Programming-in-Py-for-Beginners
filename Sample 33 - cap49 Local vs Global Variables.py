"""
  Sample 33 - cap49 Local vs Global Variables.py
"""
program        = 'Sample 33 - cap49 Local vs Global Variables.py'
import time
import reaGab as g

def showVars():
   global y
   x     = 5 # Local to the function
   y     = 11
   print('x,y:',x,y)

g.title(program,'')


y     = 3
x     = 1
showVars()
print('x,y:',x,y)















g.title(program,'/')
g.title(" END ",'-')







