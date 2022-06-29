# Python Simple Command Line Calculator

#This is calculation function
def calculation(cal, num1, num2):
    myList = []
    if cal == '1':
        myList.append('+')
        myList.append(num1 + num2)
    elif cal == '2':
        myList.append('-')
        myList.append(num1 - num2)
    elif cal == '3':
        myList.append('*')
        myList.append(num1 * num2)
    elif cal == '4':
        myList.append('/')
        myList.append(num1 / num2)

    return myList
    



print("#############################")
print("     PYTHON CALCULATOR")
print("#############################")
print("")
print("Select Operation")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("")
print("#############################")


while True:
    # Take the user input
    print("")
    operation = input("Enter Operation(1/2/3/4): ")

    # Check if choice is one of the four Operation
    if operation in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        result = calculation(operation, number1, number2)

        print(number1, result[0], number2, " = " , result[1])
        
        # Check if user wants to do another calculation
        # Break the loop if answer is 'n'
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("")
        print("Invalid Input")
