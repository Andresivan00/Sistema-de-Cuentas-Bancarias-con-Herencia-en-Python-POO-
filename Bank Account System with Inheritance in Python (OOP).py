class Account:
    def __init__(self, balance):
        self._balance = balance      # Initial account balance
        self._num_deposits = 0       # Deposit counter
        self._num_withdrawals = 0    # Withdrawal counter

    def deposit(self, amount):
        self._balance += amount      # Add amount to balance
        self._num_deposits += 1      # Increase deposit counter

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount  # Subtract amount
            self._num_withdrawals += 1  # Increase withdrawal counter

    def get_balance(self):
        return self._balance         # Return current balance

    def print_info(self):
        return f"""Balance: {self._balance}
Number of deposits: {self._num_deposits}
Number of withdrawals: {self._num_withdrawals}"""


# CORRECTED CHILD CLASS
class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        # A savings account is active only if it has more than 10,000
        if self._balance > 10000:
            self._active = True
            print("Savings account created and ACTIVE")
        else:
            self._active = False
            print("Savings account created but INACTIVE (balance less than 10,000)")

    # Method to check if active (updates status each time)
    def is_active(self):
        if self._balance > 10000:    # Typical Colombian savings account rule
            self._active = True
        else:
            self._active = False
        return self._active

    # OVERRIDING deposit
    def deposit(self, amount):
        if self.is_active():              # Only allows deposit if active
            super().deposit(amount)       # Now it ADDS! (before it subtracted)
            print(f"Successful deposit of {amount}")
        else:
            print("Inactive account → cannot deposit")

    # OVERRIDING withdraw
    def withdraw(self, amount):
        if self.is_active():              # Only allows withdrawal if active
            super().withdraw(amount)      # Calls parent's withdraw method
            print(f"Successful withdrawal of {amount}")
        else:
            print("Inactive account → cannot withdraw")

    # Show complete information
    def print_info(self):
        status = "YES" if self._active else "NO"
        return f"""Account active? {status}
{super().print_info()}"""


# ===== CORRECT TEST =====
print("=== Testing normal Account class ===")
c = Account(9000000)
print(c.print_info())
c.deposit(500000)
print("New balance:", c.get_balance())      # Now with parentheses!
c.withdraw(500000)
print("New balance:", c.get_balance())
print(c.print_info())

print("\n=== Testing SavingsAccount ===")
sa = SavingsAccount(15000)       # More than 10,000 → active
print(sa.print_info())
sa.deposit(5000)
sa.withdraw(3000)
print(sa.print_info())

print("\n=== Inactive account ===")
sa2 = SavingsAccount(5000)       # Less than 10,000 → inactive
sa2.deposit(10000)               # Will try to deposit but won't allow

sa2.withdraw(2000)               # Won't allow withdrawal
