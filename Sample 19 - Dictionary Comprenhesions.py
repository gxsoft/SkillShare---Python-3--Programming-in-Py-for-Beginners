import sys

def farenheit(celcius):
   return (celcius * 9/5) + 32
# farenheit(celcius)
def celcius(farenheit):
   return (farenheit -32) / 1.8
   #return (farenheit / (9/5)) - 32
# celcius(farenheit)




"""
Sample 19 - Dictionary Comprenhesions.py
"""
names       = ["Gabriel","Silvia","Merlina","Luis","Machi","Fran"]
numes       = [1, 2, 3, 4, 5, 6]
grads       = {'t0':0, 't1':5, 't2':10, 't3':14, 't4':20, 't5':28}

# ---- Dictionary comprenhensions ----------
"""
namesLen    = {
   Key : value
} """

namesLen    = {name : len(name)
               for name in names 
}
# Normal way
namesLen    = {name : len(name) for name in names}

print(namesLen)

namesLen    = {name : len(name)
               for name in names
               if name.startswith("L")
}
print(namesLen)
""" With NUMBERS """
numesPot    = {nume : nume*nume for nume in numes}

print(numesPot)

numesPot2   = {nume : nume * (nume)
               for nume in numes
               if (nume % 2) == 0
}
print(numesPot2)
numesPot3   = {nume : nume * (nume)
               for nume in range(1,500)
               if nume >30
               if nume <35
}
print(numesPot3)
""" With TEMPERATURE to Farenheit """
print(" With TEMPERATURE to Farenheit ")
tfarenheit  = { key : [celcius, farenheit(celcius)] 

                for key,celcius in grads.items() 
                }
print(tfarenheit)
print("")
print("")
print(" Temperaturas en grados Centígrdos(celcius) y Fanrenheit)")
print("")
print("Cº","  Fº", "Cº" )
for temp in range(101):
   print(temp,"  ",farenheit(temp),celcius(farenheit(temp)))
   
