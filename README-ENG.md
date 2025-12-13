# Bank Account System with Inheritance in Python (OOP)

Educational and 100% functional example of **Object-Oriented Programming** that simulates two types of bank accounts using **inheritance and method overriding**.

### What this code does exactly

* **Parent class `Account`**
  Represents a basic bank account:

  * Stores balance, number of deposits, and withdrawals
  * Allows depositing and withdrawing money
  * Displays the balance and statistics

* **Child class `SavingsAccount`** (inherits from `Account`)
  Simulates a real savings account (as in Colombia):

  * Only **active if the balance is greater than $10,000**
  * **Does not allow deposits or withdrawals** if the account is inactive
  * Automatically updates its status
  * Overrides `deposit()`, `withdraw()`, and `print()`
