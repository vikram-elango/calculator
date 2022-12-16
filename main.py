def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


#keys are the symbols , values are the fucntions

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("What the first number?"))
for i in operations:
    print(i)
cont='y'
while cont=='y':

    operations_symbol = input("Pick an operation:")

    num2=int(input("Whats the next number?"))
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1}{operations_symbol}{num2}={answer}")
    cont = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit")

    if cont=='y':
        num1=answer
    else:
        cont='n'



