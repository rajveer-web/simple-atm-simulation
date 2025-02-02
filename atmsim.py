import sys

# Dummy data (for simulation purposes)
users = {
    '123456': {'pin': '1234', 'balance': 1000.0, 'transactions': []}
}

def sign_in():
    print("Enter your account number:")
    account_number = input().strip()
    
    if account_number not in users:
        print("Account not found!")
        return None

    print("Enter your PIN:")
    pin = input().strip()

    if users[account_number]['pin'] == pin:
        print("Sign-in successful!")
        return account_number
    else:
        print("Invalid PIN!")
        return None

def account_statement(account_number):
    user_data = users[account_number]
    print("\n--- Account Statement ---")
    print(f"Balance: ${user_data['balance']:.2f}")
    print("Transactions:")
    if not user_data['transactions']:
        print("No transactions yet.")
    else:
        for trans in user_data['transactions']:
            print(trans)
    print("--------------------------\n")

def withdraw(account_number):
    user_data = users[account_number]
    print("Enter amount to withdraw:")
    try:
        amount = float(input().strip())
    except ValueError:
        print("Invalid input!")
        return
    
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if amount > user_data['balance']:
        print("Insufficient balance.")
        return

    user_data['balance'] -= amount
    user_data['transactions'].append(f"Withdrew ${amount:.2f}")
    print(f"Withdrawal of ${amount:.2f} successful!")

def lodge(account_number):
    user_data = users[account_number]
    print("Enter amount to lodge:")
    try:
        amount = float(input().strip())
    except ValueError:
        print("Invalid input!")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    user_data['balance'] += amount
    user_data['transactions'].append(f"Lodged ${amount:.2f}")
    print(f"Lodgement of ${amount:.2f} successful!")

def change_pin(account_number):
    user_data = users[account_number]
    print("Enter new PIN:")
    new_pin = input().strip()

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be a 4-digit number.")
        return

    user_data['pin'] = new_pin
    print("PIN successfully changed!")

def main():
    print("Welcome to the ATM")
    
    account_number = sign_in()
    
    if account_number is None:
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. View Account Statement")
        print("2. Withdraw Amount")
        print("3. Lodge Amount")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("Please choose an option (1-5): ").strip()

        if choice == '1':
            account_statement(account_number)
        elif choice == '2':
            withdraw(account_number)
        elif choice == '3':
            lodge(account_number)
        elif choice == '4':
            change_pin(account_number)
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
