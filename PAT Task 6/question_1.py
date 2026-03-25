
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Balance:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Balance:", self.__balance)
        else:
            print("Insufficient balance")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, rate):
        BankAccount.__init__(self, account_number, balance)
        self.rate = rate

    def calculate_interest(self):
        interest = self.get_balance() * self.rate / 100
        print("Interest:", interest)


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        BankAccount.__init__(self, account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.min_balance:
            BankAccount.withdraw(self, amount)
        else:
            print("Minimum balance required")



print("1. Savings Account")
print("2. Current Account")

choice = int(input("Enter account type: "))
acc_no = input("Enter account number: ")
balance = float(input("Enter balance: "))

if choice == 1:
    acc = SavingsAccount(acc_no, balance, 5)

elif choice == 2:
    acc = CurrentAccount(acc_no, balance, 1000)

else:
    print("Invalid choice")
    exit()


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    op = int(input("Enter operation: "))

    if op == 1:
        amt = float(input("Enter deposit amount: "))
        acc.deposit(amt)

    elif op == 2:
        amt = float(input("Enter withdraw amount: "))
        acc.withdraw(amt)

    elif op == 3:
        print("Balance:", acc.get_balance())

    elif op == 4:
        print("Thank you")
        break

    else:
        print("Invalid option")

    # extra for savings account
    if choice == 1:
        acc.calculate_interest()