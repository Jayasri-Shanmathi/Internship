#CALCULATOR
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    if b==0:
        print("Division by zero is invalid")
    else:
        return (a/b)
#MAIN PROGRAM
print("--------CALCULATOR--------")
num1=int(input("Enter first number:")) 
num2=int(input("Enter second number:"))         
print("OPERATIONS IN CALCULATOR")
print("Addition: '+'")
print("Subtraction: '-'")
print("Multiplication: '*'")
print("Division: '/'")
op=input("Enter symbol of required operation:")
if op=='+':
    print(add(num1,num2))
elif op=='-':
    print(sub(num1,num2))
elif op=='*':
    print(mul(num1,num2))
elif op=='/':
    print(div(num1,num2))
else:
    print("Wrong choice entered...")
print("PROGRAM ENDS")                    