while True:
    print("1.Add")
    print("2.Subtract")
    print("2.Multiply")
    print("3.Divide")

    choice = input("Enter your choice (1/2/3/4):")

    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", num1 / num2)    

    else:
       print("Invalid choice")

    again = input ("Do you want to continue? (yes/no):")

    if again == "no":
        break             
