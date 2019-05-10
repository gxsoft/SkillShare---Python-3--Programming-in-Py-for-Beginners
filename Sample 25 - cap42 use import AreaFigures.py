import AreaFiguresCAP25
#enum - enumeratio - list of elemets that are enumerated (numbered)
from enum import Enum

Enum('Menu_Figures', 'Square, Rectangle, Circle, Trapeze' )
print("print(Enum('Menu_Figures', 'Square, Rectangle, Circle, Trapeze' ))")

print(Enum('Menu_Figures', 'Square, Rectangle, Circle, Trapeze' ))
print("-------------------------")

"""
Sample 25 - cap42 use import AreaFigures.py
use My MODULE (import)
09:33
"""


choose      = input("""What figure area you want to measure?
1. Square
2. Rectangle
3. Circle
4. Triangle
5. Trapeze
""")
if (choose == "1"): # Square
    a       = float(input("Enter the size of square side: "))
    print("The area of square is equal to:", AreaFiguresCAP25.area_of_square(a))
elif (choose == "2"): # Rectangle
    a       = float(input("Enter the size of 1st side of rectangle: "))
    b       = float(input("Enter the size of 2nd side of rectangle: "))
    print("The area of rectangle is equal to:", AreaFiguresCAP25.area_of_rectangle(a,b))
elif (choose == "3"): # Circle
    r       = float(input("Enter the radius of circle: "))
    print("The area of circle is equal to:", AreaFiguresCAP25.area_of_circle(r))
elif (choose == "4"): #Triangle
    a       = float(input("Enter the side of  Triangle: "))
    h       = float(input("Enter the height of Triangle: "))
    print("The area of Triangle is equal to:", AreaFiguresCAP25.area_of_triangle(a,h))

elif (choose == "5"): #Trapeze
    a       = float(input("Enter the size of 1st side of trapeze: "))
    b       = float(input("Enter the size of 2nd side of Trapeze: "))
    h       = float(input("Enter the height of Trapeze: "))
    print("The area of trapeze is equal to:", AreaFiguresCAP25.area_of_trapeze(a,b,h))
