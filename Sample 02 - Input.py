name        = "john"
print(name.lower())
print(name.upper())

print("Ingresa el Nombre:")
name = input("in.Nombre: ")
print("Ingresa el Apellido:")
lastname = input("in.Apellido:")


customername = name.capitalize() + " "+ lastname.capitalize()
print("Nombre Completo: " + customername)

#Casting allows you to change ONE tyoe of variable to another type
print("Ingrese 2 numeros")
a = int(input("First number:"))
b = int(input("Second Number:"))

print("Sum of a and b is equal to:" , str(a)+ str(b))
print("Sum of a and b is equal to:" , str(a+b))
print("Sum of ", a ," and ", b ," is equal to:" , a + b)
