from datetime import datetime
from typing import List, Dict


class Transaction:
    """Represents a single transaction in the FamPay account."""

    def __init__(self, amount: float, transaction_type: str):
        self.amount: float = amount
        self.transaction_type: str = transaction_type  # 'Deposit' or 'Withdrawal'
        self.timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"{self.timestamp} | {self.transaction_type:<10} ₹{self.amount:.2f}"


class FamPayAccount:
    """A basic FamPay-like account simulation with deposit, withdrawal, and transaction history."""

    def __init__(self, name: str, acc_no: str, email: str, phone: str, pin: str):
        self.name: str = name
        self.acc_no: str = acc_no
        self.email: str = email
        self.phone: str = phone
        self.pin: str = pin
        self.balance: float = 0.0
        self.transactions: List[Transaction] = []

    def add_money(self, amount: float) -> str:
        """Adds money to the account balance."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, "Deposit"))
            return f"✅ ₹{amount:.2f} added successfully. New balance: ₹{self.balance:.2f}"
        return "❌ Invalid amount. Please enter a positive value."

    def withdraw_money(self, amount: float) -> str:
        """Withdraws money from the account if sufficient balance exists."""
        if amount <= 0:
            return "❌ Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "❌ Insufficient balance."
        self.balance -= amount
        self.transactions.append(Transaction(amount, "Withdrawal"))
        return f"✅ ₹{amount:.2f} withdrawn successfully. New balance: ₹{self.balance:.2f}"

    def check_balance(self) -> str:
        """Returns the current balance."""
        return f"💰 Current Balance: ₹{self.balance:.2f}"

    def view_account_details(self) -> Dict[str, str]:
        """Returns a dictionary of account details (excluding PIN)."""
        return {
            "Name": self.name,
            "Account Number": self.acc_no,
            "Email": self.email,
            "Phone": self.phone,
            "Balance": f"₹{self.balance:.2f}"
        }

    def view_transactions(self) -> str:
        """Returns a string representation of the transaction history."""
        if not self.transactions:
            return "📭 No transactions found."
        return "\n".join(str(txn) for txn in self.transactions)


# 🧪 Example Usage (for testing/demo)
if __name__ == "__main__":
    # Create a sample account (replace with user input if needed)
    account = FamPayAccount(
        name="Satyam Srivastava",
        acc_no="1234567890",
        email="sattugoat@gmail.com",
        phone="1234567890",
        pin="7676"
    )

    print("🔐 FamPay Account Manager - Demo")
    print(account.add_money(1500))
    print(account.withdraw_money(400))
    print(account.check_balance())

    print("\n👤 Account Details:")
    for key, value in account.view_account_details().items():
        print(f"{key}: {value}")

    print("\n📜 Transaction History:")
    print(account.view_transactions())
