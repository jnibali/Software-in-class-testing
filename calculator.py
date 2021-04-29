def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


def runCalculator(x, y):
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = x
            num2 = y

            if choice == '1':
               return add(num1, num2)

            elif choice == '2':
                return subtract(num1, num2)

            elif choice == '3':
                return multiply(num1, num2)

            elif choice == '4':
               return divide(num1, num2)
            
        