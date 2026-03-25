class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        Employee.__init__(self, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        Employee.__init__(self, name, 0)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


class Manager(Employee):
    def __init__(self, name, salary, allowance):
        Employee.__init__(self, name, salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.salary + self.allowance


print("1. Regular Employee")
print("2. Contract Employee")
print("3. Manager")

choice = int(input("Enter type: "))
name = input("Enter name: ")

if choice == 1:
    salary = float(input("Enter salary: "))
    bonus = float(input("Enter bonus: "))
    emp = RegularEmployee(name, salary, bonus)

elif choice == 2:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate per hour: "))
    emp = ContractEmployee(name, hours, rate)

elif choice == 3:
    salary = float(input("Enter salary: "))
    allowance = float(input("Enter allowance: "))
    emp = Manager(name, salary, allowance)

else:
    print("Invalid choice")
    exit()

print("Total Salary:", emp.calculate_salary())