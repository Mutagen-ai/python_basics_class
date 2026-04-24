#Creating a Bank Account
# ============================================================

class Account:
    """
    Represents a bank account with deposit, withdraw,
    and balance-checking functionality.
    """

    def __init__(self, account_number: str, account_holder: str, account_balance: float = 0.0):
        """
        Constructor — runs when you create a new Account object.

        Parameters:
            account_number  (str)   : e.g. "ACC-001"
            account_holder  (str)   : e.g. "Alice Kamau"
            account_balance (float) : starting balance, defaults to 0.0
        """
        self.account_number  = account_number
        self.account_holder  = account_holder
        self.account_balance = account_balance

    # ----------------------------------------------------------
    # METHOD 1 — deposit
    # ----------------------------------------------------------
    def deposit(self, amount: float):
        """
        Adds 'amount' to the account balance.
        Only accepts positive amounts.
        """
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.account_balance += amount
        print(f"Deposited KES {amount:,.2f}. "
              f"New balance: KES {self.account_balance:,.2f}")

    # ----------------------------------------------------------
    # METHOD 2 — withdraw
    # ----------------------------------------------------------
    def withdraw(self, amount: float):
        """
        Subtracts 'amount' from the account balance,
        BUT only if the balance is >= the amount.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew KES {amount:,.2f}. "
                  f"New balance: KES {self.account_balance:,.2f}")
        else:
            print(f"Insufficient funds! "
                  f"Balance is KES {self.account_balance:,.2f}, "
                  f"but you tried to withdraw KES {amount:,.2f}.")

    # ----------------------------------------------------------
    # METHOD 3 — check_balance
    # ----------------------------------------------------------
    def check_balance(self) -> float:
        """
        Returns the current account balance and prints it.
        """
        print(f"Account [{self.account_number}] — {self.account_holder}: "
              f"KES {self.account_balance:,.2f}")
        return self.account_balance

    # ----------------------------------------------------------
    # __str__ — nice string representation of the object
    # ----------------------------------------------------------
    def __str__(self):
        return (f"Account({self.account_number}, "
                f"Holder: {self.account_holder}, "
                f"Balance: KES {self.account_balance:,.2f})")


# ==============================================================
# STEP 5 — Create an instance called "my_account"
# ==============================================================

print("=" * 55)
print("  STEP 5: Creating my_account")
print("=" * 55)

my_account = Account(
    account_number  = "ACC-001",
    account_holder  = "Alice Kamau",
    account_balance = 1000.00      # starting balance
)

print(my_account)   # uses __str__


# ==============================================================
# STEP 6 — Use the methods: deposit, withdraw, check_balance
# ==============================================================

print("\n" + "=" * 55)
print("  STEP 6: Using deposit, withdraw & check_balance")
print("=" * 55)

my_account.deposit(500)          
my_account.deposit(250.50)        
my_account.withdraw(200)          
my_account.withdraw(5000)         
my_account.withdraw(-100)         
my_account.check_balance()       


# ==============================================================
# STEP 7 — Multiple instances, different transactions
# ==============================================================

print("\n" + "=" * 55)
print("  STEP 7: Multiple Account Instances")
print("=" * 55)

# Account 2 — Bob
acc2 = Account("ACC-002", "Bob Otieno", 5000.00)
print(f"\n{acc2}")
acc2.deposit(2000)
acc2.withdraw(1500)
acc2.check_balance()

# Account 3 — Carol (starts with zero balance)
acc3 = Account("ACC-003", "Carol Wanjiku")
print(f"\n{acc3}")
acc3.deposit(100)
acc3.withdraw(150)       
acc3.withdraw(50)        
acc3.check_balance()

# Account 4 — David (edge case: withdraw exact balance)
acc4 = Account("ACC-004", "David Mwangi", 300.00)
print(f"\n{acc4}")
acc4.withdraw(300)       
acc4.check_balance()     

print("\n" + "=" * 55)
print("  All tests complete!")
print("=" * 55)