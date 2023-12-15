import car_company
import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = car_company.Car("Toyota", "Corolla", 2020, 20000)

    def test_car_creation(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Corolla")
        self.assertEqual(self.car.year, 2020)
        self.assertEqual(self.car.price, 20000)


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = car_company.Inventory()
        self.car1 = car_company.Car("Toyota", "Corolla", 2020, 20000)
        self.car2 = car_company.Car("Honda", "Civic", 2019, 18000)
        self.inventory.add_car(self.car1)
        self.inventory.add_car(self.car2)

    def test_add_car(self):
        self.assertEqual(len(self.inventory.cars), 2)

    def test_find_car(self):
        car = self.inventory.find_car("Honda", "Civic")
        self.assertIsNotNone(car)
        self.assertEqual(car.year, 2019)

    def test_update_car(self):
        self.inventory.update_car("Honda", "Civic", 19000)
        car = self.inventory.find_car("Honda", "Civic")
        self.assertEqual(car.price, 19000)

    def test_list_cars(self):
        cars = self.inventory.list_cars()
        self.assertEqual(len(cars), 2)


if __name__ == "__main__":
    unittest.main()
