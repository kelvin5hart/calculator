import art

print(art.logo)

#Calculator Functions
#Addition
def add (n1, n2):
  return n1 + n2

#Subtraction 
def substract (n1, n2):
  return n1 - n2

#Multiplication
def multiply (n1, n2):
  return n1 * n2

#Division
def divide(n1, n2):
  return n1 / n2

opperators = {
  "+": add, 
  "-":substract, 
  "*": multiply, 
  "/": divide
}

num1 = int(input("What's the first number? \n"))
num2 = int(input("What's the second number? \n"))

for i in opperators:
  print (i)
operator = input("Pick an operation from the line above: ")

operation = opperators[operator]
result = operation(num1, num2)

print(f"{num1} {operator} {num2} = {result}")