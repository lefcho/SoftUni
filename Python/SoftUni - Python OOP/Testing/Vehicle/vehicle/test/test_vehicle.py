from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(5, 100)

    def test_init(self):
        self.assertEqual(5, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_fuel_needed_enough(self):
        result = self.vehicle.fuel - self.vehicle.fuel_consumption * 2
        self.vehicle.drive(2)
        self.assertEqual(result, self.vehicle.fuel)

    def test_drive_fuel_not_enough_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_when_refuel_is_not_to_much(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(5)
        self.assertEqual(5, self.vehicle.fuel)

    def test_refuel_when_fuel_is_to_much_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        result = "The vehicle has 100 " \
               "horse power with 5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, str(self.vehicle))


if __name__ == '__main__':
    main()