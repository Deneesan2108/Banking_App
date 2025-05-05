import random

Accounts = {}

def Create_Account():
    global Current_Account_Number  # To use it outside the function
    Name = input("Welcome! Please enter your account name: ")
    
    try:
        Initial_Balance = float(input("Please enter initial balance: "))
        if Initial_Balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Please enter the balance in numbers only.")
        return

    Account_Number = str(random.randint(10000, 99999))
    Current_Account_Number = Account_Number  # Store for later use

    Accounts[Account_Number] = {
        "Name": Name,
        "Balance": Initial_Balance,
        "Transactions": [f"Account created with balance {Initial_Balance}"]
    }

    print(f"Account created successfully! Your account number is {Account_Number}")

def Deposite_Account():
    Account_number = input("Please enter your account number: ")

    if Account_number in Accounts:
        try:
            Deposite_Money = float(input("Please enter the amount to deposit: "))
            if Deposite_Money < 0:
                print("Deposit amount must be positive.")
                return
        except ValueError:
            print("Deposit amount must be a number.")
            return

        Accounts[Account_number]["Balance"] += Deposite_Money
        Accounts[Account_number]["Transactions"].append(f"Deposited {Deposite_Money}")
        print("Deposit successful.")
    else:
        print("Account number not found. Please check again.")

# Run the functions
Create_Account()
Deposite_Account()


def Deposite_Account():
    Account_number = input("Please enter your account number: ")

    if Account_number in Accounts:
        try:
            Deposite_Money = float(input("Please enter the amount to deposit: "))
            if Deposite_Money < 0:
                print("Deposit amount must be positive.")
                return
        except ValueError:
            print("Deposit amount must be a number.")
            return

        # Add deposit to the account balance
        Accounts[Account_number]["Balance"] += Deposite_Money
        
        # Log the transaction
        Accounts[Account_number]["Transactions"].append(f"Deposited {Deposite_Money}")
        
        print("Deposit successful.")
    else:
        print("Account number not found. Please check again.")
