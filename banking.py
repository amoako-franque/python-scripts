# Banking program

def show_balance(balance):
    print(f"Your remaining balance is ${balance:.2f}")


def deposit():
    print("*****************************")
    amount = float(input("Enter an amount to deposit: "))
    print("*****************************")
    if amount < 0:
        print("*****************************")
        print("Amount must be greater than 0")
        print("*****************************")
        return 0
    else:
        print("*****************************")
        # global balance
        # balance += amount
        # print(f"Your new balance is ${balance:.2f}")
        return amount


def withdraw(balance):
    print("*****************************")
    amount = float(input("Enter amount to withdraw: "))
    print("*****************************")

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        # global balance
        return amount


# balance -= amount
# print(f"Your new balance is ${balance:.2f}")
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************************")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************************")

        choice = input("Select your banking choice (1 - 4 ): ")

        if choice == "1":
            print("*****************************")
            show_balance(balance)
            print("*****************************")
        elif choice == "2":
            print("*****************************")
            balance += deposit()
            print("*****************************")
        elif choice == "3":
            print("*****************************")
            balance -= withdraw(balance)
            print("*****************************")
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice")


print("Thank you for banking with us. Have a nice day!")  # empty line for better readability

if __name__ == "__main__":
    main()
