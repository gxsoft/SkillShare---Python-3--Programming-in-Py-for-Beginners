

"""
Sample 20 - Set Comprenhesions EXPRESSIONS.py
"""
names       = {"gabriel","Silvia","merlina","luis","machi","fran"}

namesU      = { name.capitalize()
                for name in names
                if name[0] =="m"}
namesF      = { name[0]
                for name in names
                }
print(names)
print(namesU)
print(namesF)
