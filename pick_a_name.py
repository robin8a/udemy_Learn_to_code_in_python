import random

number = random.randint(0,7)

print ("Type eight names")

list_names = []

while len(list_names) < 8:
    list_names.append( input("Type a new name: ") )

print ( "Ramdom name in list: ", list_names[number] )
