class Vehicle:
    def __init__(self, model, rate):
        self.model = model
        self.rate = rate

    def calculate_rental(self, days):
        return self.rate * days


class Car(Vehicle):
    def __init__(self, model, rate, seats):
        Vehicle.__init__(self, model, rate)
        self.seats = seats

    def calculate_rental(self, days):
        return self.rate * days


class Bike(Vehicle):
    def __init__(self, model, rate, cc):
        Vehicle.__init__(self, model, rate)
        self.cc = cc

    def calculate_rental(self, days):
        return self.rate * days


class Truck(Vehicle):
    def __init__(self, model, rate, load):
        Vehicle.__init__(self, model, rate)
        self.load = load

    def calculate_rental(self, days):
        return (self.rate * days) + 500


print("1. Car")
print("2. Bike")
print("3. Truck")

choice = int(input("Enter vehicle type: "))
model = input("Enter model: ")
rate = float(input("Enter rent per day: "))
days = int(input("Enter number of days: "))

if choice == 1:
    seats = int(input("Enter seats: "))
    v = Car(model, rate, seats)

elif choice == 2:
    cc = int(input("Enter engine cc: "))
    v = Bike(model, rate, cc)

elif choice == 3:
    load = float(input("Enter load capacity: "))
    v = Truck(model, rate, load)

else:
    print("Invalid choice")
    exit()

print("Total Rent:", v.calculate_rental(days))