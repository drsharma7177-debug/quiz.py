balance = 1000

while True:

    print("\nWelcome to Duke Bank")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is £", balance)

    elif choice == "2":

        try:
            amount = int(input("Enter the amount you want to deposit: "))
            balance = balance + amount
            print("Your deposit is successful.")

        except ValueError:
            print("Please enter numbers only.")

    elif choice == "3":

        try:
            amount = int(input("Enter the amount you want to withdraw: "))

            if amount <= balance:
                balance = balance - amount
                print("Please collect your cash.")

            else:
                print("Insufficient balance.")

        except ValueError:
            print("Please enter numbers only.")

    elif choice == "4":
        print("Thank you for visiting Duke Bank.")
        break

    else:
        print("Invalid option.")