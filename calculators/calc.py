import math

def addition(x, y):
    return x + y 

def subratction(x, y): 
    return x - y 

def multiplication(x, y): 
    return x * y 

def divison(x, y): 
    return x / y 

def power_x(x, y):
    return x**y

def square(x): 
    return math.sqrt(x)



user_input = input("""Addition : a
Subtraction : s
Multiplication : m
Divison : d
Square : sq
To the power of x: p
 """)

while user_input:
   if user_input.lower() == "a": 
      x = int(input("Add x")) 
      y = int(input("Add y"))
      value = addition(x, y)
      print(value)

   elif user_input.lower() == "s": 
       x = int(input("Add x"))
       y = int(input("Add y"))    
       value = subratction(x, y)
       print(value)

   elif user_input.lower() == "m": 
       x = int(input("Add x"))
       y = int(input("Add y"))
       value = multiplication(x, y)
       print(value)
   elif user_input.lower() == "d": 
       x = int(input("Add x"))
       y = int(input("Add y"))
       value = divison(x, y)
       print(value)

   elif user_input.lower() == "p": 
       x = int(input("Whats your base?"))
       y = int(input("Whats your exponent?"))
       value = power_x(x, y)
       print(value)

   elif user_input.lower() == "sq": 
       x = int(input("Num to square: "))
       value = square(x)
       print(value)
   else: 
      print("""Entre a valid letter!!!
       Addition : a
       Subtraction : s
       Multiplication : m
       Divison : d
       Square : sq
       To the power of x: p""")

   again = input("Continue? (yes/no)")
   if again.lower() == "yes": 
         user_input = input("""Addition : a
         Subtraction : s
         Multiplication : m
         Divison : d
         Square : sq
         Power of x: p""")
   else: 
      break

