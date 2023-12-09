from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway_station = RailwayStation('test')

    def test_init(self):
        self.assertEqual(self.railway_station.name, 'test')
        self.assertTrue(isinstance(self.railway_station.arrival_trains, deque))
        self.assertTrue(isinstance(self.railway_station.departure_trains, deque))

    def test_name_setter_raises_val_error(self):
        with self.assertRaises(ValueError) as ex:
            self.railway_station = RailwayStation('123')
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.railway_station = RailwayStation('1')
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board_appending_info(self):
        self.railway_station.new_arrival_on_board('test info')
        self.assertEqual(self.railway_station.arrival_trains, deque(['test info']))

    def test_train_has_arrived_return_other_trains_before(self):
        self.railway_station.new_arrival_on_board('test info')
        self.railway_station.new_arrival_on_board('test')
        self.assertEqual(self.railway_station.train_has_arrived('test'),
                         "There are other trains to arrive before test.")

    def test_train_has_arrived_return_train_on_platform(self):
        self.railway_station.new_arrival_on_board('test')
        result = self.railway_station.train_has_arrived('test')
        self.assertEqual(result,"test is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.railway_station.departure_trains, deque(['test']))

    def test_train_has_left_return_true_and_trains_leaving_station(self):
        self.railway_station.departure_trains = deque(['test', 'test2'])
        result = self.railway_station.train_has_left('test')
        self.assertTrue(result)
        self.assertEqual(deque(['test2']), self.railway_station.departure_trains)
        self.railway_station.train_has_left('test2')
        self.assertEqual(deque(), self.railway_station.departure_trains)

    def test_train_has_left_return_false_when_no_departure_trains(self):
        result = self.railway_station.train_has_left('test')
        self.assertFalse(result)

    def test_train_has_left_return_false_when_wrong_departure_train(self):
        self.railway_station.departure_trains = deque(['test', 'test2'])
        result = self.railway_station.train_has_left('test2')
        self.assertFalse(result)
        self.assertEqual(self.railway_station.departure_trains, deque(['test', 'test2']))


if __name__ == '__main__':
    main()
