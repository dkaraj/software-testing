import requests


class User(object):
    def __init__(self, data):
        self.user = data

    def get_user(self, id):
            return self.user.get(id)

    def get_user_details(self, id):
        response = requests.get("http://some-account-uri/" + id)
        return {'status': response.status_code,
                'data': response.text}
