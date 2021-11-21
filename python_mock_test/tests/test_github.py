from mock import patch
from unittest import TestCase
from python_mock_test.github import get_github_repos_by_username


class GithubTest(TestCase):
    @patch('requests.get')
    def test_fetch_repo_names(self, mock_get):
        mock_get.return_value.json.return_value = [
            {"name": "1"},
            {"name": "2"}]
        expected_names = ['1', '2']

        names = get_github_repos_by_username('username')

        self.assertEqual(expected_names, names)
