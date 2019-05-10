import sys
"""
Sample 22 - cap39 def Functions.py
def name_of_functions(parm1,parm2,parm3,...):
   instructions1
   instructions2
   instructions3
   ...
   instructionsN
   return VALUE
  

"""
def multi(par1,par2):
   value       = par1*par2
   return value

def name_last(name,last):
    return last.capitalize()+", "+name.capitalize()

def name_mister(name,last):
    return "Mr.:"+name.capitalize()+" "+last.capitalize()

def area_rectangle(side1,side2):
   return side1,side2

name        = "gab"
last        = "medina"

print(name_last(name,last))
print(name_mister(name,last))
area1       = area_rectangle(10,21)
area2       = area_rectangle(110,221)

print("Area de rectanle 1:",area1)
print("Area de rectanle 2:",area2)
