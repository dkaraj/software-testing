import unittest
from mock import Mock, patch
from python_mock_test.user import User


class TestUser(unittest.TestCase):
    def test_account_returns_data_by_id(self):
        user_data = {"id": "1", "name": "test"}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = user_data
        user = User(mock_data_interface)
        self.assertDictEqual(user_data, user.get_user(1))

    @patch('python_mock_test.user.requests')
    def test_get_current_user_details(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'User data'
        mock_requests.get.return_value = mock_response
        user = User(Mock())
        self.assertEqual({'status': 200, 'data': 'User data'},
                         user.get_user_details('1'))
