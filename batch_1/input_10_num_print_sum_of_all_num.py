# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# try-except for error handling
try:
    
    # ask user to input 10 numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    num4 = int(input("Enter fourth number: "))
    num5 = int(input("Enter fifth number: "))
    num6 = int(input("Enter sixth number: "))
    num7 = int(input("Enter seventh number: "))
    num8 = int(input("Enter eighth number: "))
    num9 = int(input("Enter ninth number: "))
    num10 = int(input("Enter tenth number: "))

    # process numbers
    sum_of_all = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10

    # print result
    print(f"The sum of all numbers is {sum_of_all}")

except ValueError:
    print("Please enter a valid number")