class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price


class Inventory:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def find_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                return car
        return None

    def update_car(self, make, model, price):
        car = self.find_car(make, model)
        if car:
            car.price = price
def list_cars(self):
        return self.cars

def remove_car(self, model):
        car = self.remove_car_car(model)
        if car:
            car.model < 1995
def list_cars(self):
        return self.cars

            

# Manual testing
mycar = Car("Toyota", "Corolla", 2020, 20000)
mycar2 = Car("Honda", "Civic", 2011, 2000)

print("COmpany: ", mycar.make)
print("Build in: ", mycar.year)
print(" ---- ")
print("COmpany: ", mycar2.make)
print("Build in: ", mycar2.year)

inv = Inventory()
inv.add_car(mycar)
inv.add_car(mycar2)

inv.update_car("Honda", "Civic", 19000)
inv.remove_car(1990)
inventoryWithCars = inv.list_cars()

for car in inventoryWithCars:
    print("COmpany: ", car.make)
    print("Build in: ", car.year)
    print("Price: ", car.price)
    print(" ---- ")
