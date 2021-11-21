import unittest
import mock
from python_mock_test.car import Car


class TestMakina(unittest.TestCase):
    def test_makina(self):
        data = {"id": "1", "model": "Audi"}
        mock_data = mock.Mock()
        mock_data.get.return_value = data
        car_test = Car(mock_data)
        self.assertDictEqual(data, car_test.get_car_by_id(1))

    def test_model(self):
        data = {"id": "1", "model": "Audi"}
        mock_data = mock.Mock()
        mock_data.get.return_value = data
        car_test_model = Car(mock_data)
        self.assertEqual(data['model'], car_test_model.get_car_by_id(1)['model'])
