import requests


def get_github_repos_by_username(username):
    url = ('https://api.github.com/users/{}'
           '/repos'.format(username))
    repos = requests.get(url).json()
    return [repo['name'] for repo in repos]