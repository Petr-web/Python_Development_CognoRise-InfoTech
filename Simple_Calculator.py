# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to input the operation choice
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = int(input("Enter your choice: \n1:\n2: \n3: \n4: \n"))

# Perform the calculation based on the operation choice
if choice == 1:
    result = num1 + num2
    operation = "+"
elif choice == 2:
    result = num1 - num2
    operation = "-"
elif choice == 3:
    result = num1 * num2
    operation = "*"
elif choice == 4:
    result = num1 / num2
    operation = "/"
else:
    print("Invalid choice!")
    exit()

# Display the result
print("\nResult: {} {} {} = {}".format(num1, operation, num2, result))