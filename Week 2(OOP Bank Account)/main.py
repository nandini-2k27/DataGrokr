import pandas as pd
from datetime import datetime
import os


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_file = "transactions.csv"

        # Create CSV file if it doesn't already exist
        if not os.path.exists(self.transaction_file):
            df = pd.DataFrame(
                columns=["Date", "Type", "Amount", "Balance"]
            )
            df.to_csv(self.transaction_file, index=False)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount
        self.record_transaction("Deposit", amount)

        print(f"\n₹{amount:.2f} deposited successfully.")
        print(f"Current Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.record_transaction("Withdrawal", amount)

        print(f"\n₹{amount:.2f} withdrawn successfully.")
        print(f"Current Balance: ₹{self.balance:.2f}")

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def record_transaction(self, transaction_type, amount):
        transaction = pd.DataFrame(
            [{
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Type": transaction_type,
                "Amount": amount,
                "Balance": self.balance
            }]
        )

        transaction.to_csv(
            self.transaction_file,
            mode="a",
            header=False,
            index=False
        )

    def view_transactions(self):
        df = pd.read_csv(self.transaction_file)

        if df.empty:
            print("\nNo transactions found.")
            return

        print("\n===== TRANSACTION HISTORY =====")
        print(df.to_string(index=False))


def analyze_transactions():
    if not os.path.exists("transactions.csv"):
        print("\nNo transaction data available.")
        return

    df = pd.read_csv("transactions.csv")

    if df.empty:
        print("\nNo transactions available for analysis.")
        return

    deposits = df[df["Type"] == "Deposit"]
    withdrawals = df[df["Type"] == "Withdrawal"]

    total_deposits = deposits["Amount"].sum()
    total_withdrawals = withdrawals["Amount"].sum()

    number_of_deposits = len(deposits)
    number_of_withdrawals = len(withdrawals)

    average_transaction = df["Amount"].mean()

    print("\n" + "=" * 40)
    print("       TRANSACTION ANALYSIS")
    print("=" * 40)

    print(f"Total Deposits       : ₹{total_deposits:.2f}")
    print(f"Total Withdrawals    : ₹{total_withdrawals:.2f}")
    print(f"Number of Deposits   : {number_of_deposits}")
    print(f"Number of Withdrawals: {number_of_withdrawals}")
    print(f"Average Transaction  : ₹{average_transaction:.2f}")

    print("=" * 40)


def main():
    print("=" * 40)
    print("          OOP BANK ACCOUNT")
    print("=" * 40)

    account_holder = input("Enter account holder name: ").strip()
    account_number = input("Enter account number: ").strip()

    while True:
        try:
            initial_balance = float(input("Enter initial balance: "))

            if initial_balance >= 0:
                break

            print("Balance cannot be negative.")

        except ValueError:
            print("Please enter a valid amount.")

    account = BankAccount(
        account_number,
        account_holder,
        initial_balance
    )

    while True:
        print("\n" + "=" * 40)
        print("              MENU")
        print("=" * 40)

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Analyze Transactions")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.view_transactions()

        elif choice == "5":
            analyze_transactions()

        elif choice == "6":
            print("\nThank you for using the Bank Account System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()