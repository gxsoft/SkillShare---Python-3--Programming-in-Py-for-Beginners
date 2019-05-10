
#enum - enumeratio - list of elemets that are enumerated (numbered)
from enum import Enum
from enum import IntEnum

stringDays     = 'Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday'

"""
type(Enum('DayOfWeek', stringDays))
<class 'enum.EnumMeta'>
"""
class_enum_EnumMeta =   Enum('DayOfWeek', stringDays)
print("print(class_enum_EnumMeta):")
print(class_enum_EnumMeta)

print("print(stringDays)")
print(stringDays)



print(Enum('DayOfWeek', stringDays))
print(Enum('DayOfWeek', stringDays))
print("-------------------------")
print(list(Enum('DayOfWeek', stringDays)))
print("-------------------------")
print(type(Enum('DayOfWeek', stringDays)))
      
print("-------------------------")


ListaEnum   = list(Enum('DayOfWeek', stringDays))
print("print(ListaEnum):")
print(ListaEnum)
print("-------------------------")
print("print(list(ListaEnum))")
print(list(ListaEnum))
print("-------------------------")

i     = 0
for day in ListaEnum:
   i     += 1
   print(i,day,day.value)
print('-'*50)
for day in ListaEnum:
   i     += 1
   print(i,day,'day.value:',day.value,'day.name:',day.name)
