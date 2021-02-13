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

def calculator():
  num1 = float(input("What's the first number? \n"))
  nextCalculation = True
  for i in opperators:
    print (i)

  while nextCalculation:
    operator = input("Pick an operation from the line above: ")

    if operator not in opperators:
      nextCalculation = False
      print("Your entry was invalid")
      calculator()
    num2 = float(input("What's the next number? \n"))
    operation = opperators[operator]
    result = operation(num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

    continueCalculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'e' to exit. \n").lower()
    if continueCalculation == "y":
      num1 = result
    elif continueCalculation == "n":
      nextCalculation = False
      calculator()
    elif continueCalculation == "e":
      nextCalculation = False
    else:
      print("Invalid Entry")
      nextCalculation = False

calculator()