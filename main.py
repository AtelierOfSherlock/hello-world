#Ragnar is the Earl of Scandinavia

x = 5
print (type(x))
y = "Ragnar"
z = "Floki"
if 5 >= x :
    print(y)
else :
    print("Floki")
""" Ragnar tried to build a boat 
with Floki
who was obsessed with trees """
print ("Rollo is also known as Rolf")
print (y,"and",z,"are going to Valhalla")

# type casting 
x = str(3)
print (x)

# Type function prints the datatype of the variable 
print (type(x))
print (type(y))

# variable names are case sensitive

a, b, c = "Lagertha", "Aslaug", "Thyri"
print ("Who's the hottest fo them all?",a,b,c)

a1 = b1 = c1 = "Odin"
print(a1,"is the true god")
print(b1,"is the true god")
print(c1,"is the true god")

#unpacking values from list to variables

gods = ["Odin ", "Thor ", "Freya "]
a1, b1, c1 = gods
print ("Hail to God",a1)
print ("Hail to God",b1)
print ("Hail to God",c1)
#Ragnar is the Earl of Scandinavia

x = 5
print (type(x))
y = "Ragnar"
z = "Floki"
if 5 >= x :
    print(y)
else :
    print("Floki")
""" Ragnar tried to build a boat 
with Floki
who was obsessed with trees """
print ("Rollo is also known as Rolf")
print (y,"and",z,"are going to Valhalla")

# type casting 
x = str(3)
print (x)

# Type function prints the datatype of the variable 
print (type(x))
print (type(y))

# variable names are case sensitive

a, b, c = "Lagertha", "Aslaug", "Thyri"
print ("Who's the hottest fo them all?",a,b,c)

a1 = b1 = c1 = "Odin"
print(a1,"is the true god")
print(b1,"is the true god")
print(c1,"is the true god")

#unpacking values from list to variables

gods = ["Odin ", "Thor ", "Freya "]
a1, b1, c1 = gods
print ("Hail to God",a1)
print ("Hail to God",b1)
print ("Hail to God",c1)

d1 = a1+b1+c1
print("Hail to the Gods " + d1)
d2 = 1 
print (a1+b1+c1+"reside in the Halls of Valhalla")

# variables that are created outside of a fucntion are known as global variables and can go as far as the west

def Valhalla():
    global thor
    thor = "thunder"
    print ("The true god is : "+a1)
Valhalla()

#global keyword can also be used to change the value of a global variable inside a function 

"""" data types
Text Type:  str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:  set, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
"""
a = """"
Example	Data Type	
x = str("Hello World")		
x = int(20)		
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = bytearray(5)		
x = memoryview(bytes(5))		
"""
print (a)


# Random number 
import random
print (random.randrange(1,100))

#Python Casting
#Casting in python is done using constructor functions
#int()
#float()
# str()
print(int (2.99)) # truncates the decimal part, no ceil or floor

# 'hello' is the same as "hello" -- both are strings
a = "Ragnar"
print(a)


#Strings are arrays

a = "Ragnar Lothbrok"
print (a[0])

for x in "Ragnarok" :
    print(x)

a = "Bjorn is the son of Rollo"
print (len(a))

war = "You cannot warm up a dead man"
#print ("dead" in war)
rollo = "dead" in war
print (rollo)
check = bool(print ("dead" in war))
print (check)

print (type(check))

if "dead" in war:
    mt=print("Yes, Valhalla awaits")
    print(type(mt))

obj = None
print(type(obj))

XO = 'x'
print(XO.upper())
