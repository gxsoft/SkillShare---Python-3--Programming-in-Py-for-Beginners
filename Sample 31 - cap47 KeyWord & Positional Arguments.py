"""
  Sample 31 - cap47 KeyWord & Positional Arguments.py

  Named(keyword) and unnamed (positional) arguments

  keyword - key=value
  positional - where the sequence (position) matters
"""

def greet(name, message):
   print(message, name)


greet('Arkadiusz', 'Hello')

greet(name='gab', message='Hola')

greet( message='Hola', name='Luis')


print("Uno", "Dos", "Tres", "Cuatro", sep=' - ')
print("Uno", "Dos", "Tres", "Cuatro", sep='/')
print("Uno", "Dos", "Tres", "Cuatro", sep='\n')
print("-"*50)
print("Uno", "Dos", "Tres", "Cuatro"," Cinco"," Seis", sep="")
