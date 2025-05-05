# banking_app.py

import random

# அனைத்து கணக்குகளையும் வைத்திருக்கும் dictionary
accounts = {}

# 🔹 1. கணக்கு உருவாக்கும் செயல்பாடு
def create_account():
    name = input("Enter account holder name: ")
    try:
        initial_balance = float(input("Enter initial balance (>= 0): "))
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Invalid input for balance.")
        return

    account_number = str(random.randint(10000, 99999))
    while account_number in accounts:
        account_number = str(random.randint(10000, 99999))

    accounts[account_number] = {
        'name': name,
        'balance': initial_balance,
        'transactions': [f"Account created with balance {initial_balance}"]
    }

    print(f"Account created successfully! Your account number is {account_number}")

# 🔹 2. பணம் சேர்க்கும் செயல்பாடு
def deposit_money():
    acc = input("Enter account number: ")
    if acc not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
    except ValueError:
        print("Invalid input for amount.")
        return

    accounts[acc]['balance'] += amount
    accounts[acc]['transactions'].append(f"Deposited {amount}")
    print("Deposit successful.")

# 🔹 3. பணம் எடுக்கும் செயல்பாடு
def withdraw_money():
    acc = input("Enter account number: ")
    if acc not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
    except ValueError:
        print("Invalid input for amount.")
        return

    if amount > accounts[acc]['balance']:
        print("Insufficient balance.")
        return

    accounts[acc]['balance'] -= amount
    accounts[acc]['transactions'].append(f"Withdrew {amount}")
    print("Withdrawal successful.")

# 🔹 4. இருப்பு நிலை பார்வை
def check_balance():
    acc = input("Enter account number: ")
    if acc in accounts:
        print(f"Current balance: {accounts[acc]['balance']}")
    else:
        print("Account not found.")

# 🔹 5. பரிவர்த்தனை வரலாறு
def show_transaction_history():
    acc = input("Enter account number: ")
    if acc in accounts:
        print("Transaction History:")
        for txn in accounts[acc]['transactions']:
            print(f" - {txn}")
    else:
        print("Account not found.")

# 🔹 மெனு இயக்கும் மெஷின்
def main():
    while True:
        print("\n=== Bank Menu ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            show_transaction_history()
        elif choice == '6':
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid choice. Please select between 1-6.")

# நிரல் இயக்கும் இடம்
if __name__ == "__main__":
    main()
