"""
Sample 16 -Add new Definition Search Existent Definition or Delete.py

Dictionary
1- Add new Definition
2- Search Existent Definition or
3- Delete.py
"""

dictionary     = {"1": "Uno", "2":"Dos", "3":"Tres"}
print("Dictionary:", dictionary)
print("")
print("------------- Dictionary TASK ---------------")
print("1: Add Definition")
print("2: Search Definition")
print("3: Remove Definition")
print("!: Show Dictionary")
print("?: Show Menu")
print("4: End")
choice         = ""
while choice != "4":
   choice         = input("What do you want to do?")
   if (choice =="1"):
      key            = input("Enter the word [key] to define: ")
      definition     = input("enter dedinition: ")
      dictionary[key]= definition
      print("Definition added successfully")
   elif (choice == "2"):
      key            = input("What are you searching for? ")
      if key in dictionary:
         print(dictionary[key])
      else:
         print("definition of Key [",key,"] has been not found")
   elif (choice == "3"):
      key            = input("What definition do you want to remove:? ")
      if key in dictionary:
         del dictionary[key]
      else:
         print("definition of Key [",key,"] has been not found")
   elif (choice == "!"):
      print("Dictionary:", dictionary)
      print("")
   elif (choice == "?"):
      print("------------- Dictionary TASK ---------------")
      print("1: Add Definition")
      print("2: Search Definition")
      print("3: Remove Definition")
      print("!: Show Dictionary")
      print("?: Show Menu")
      print("4: End")
   
