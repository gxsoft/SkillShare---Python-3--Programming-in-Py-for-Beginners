# Se ingesa el nombre la edad, y se le dice cuanto tendra dentro de 1 año
name        = input("Name: ")
lastname    = input("Last Name:")
age         = int(input("Age: "))

fullname    = name.capitalize() + " "+ lastname.capitalize()
age1year    = age + 1
print("You(",fullname,") have ",age1year , "years old the next year")
