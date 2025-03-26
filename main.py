import requests
from utils.base_url import BASE_URL as BASE_URL


class estRegisterUser:
    def __init__(self):
        self.endpoint = "auth/register"
        self.header = {"Content-Type": "application/json"}

    def est_email_positive(self):
        response = requests.post(BASE_URL + self.endpoint, json={
            "email": "testzzhhhhh@test.com",
            "password": "test"
        }, headers=self.header)
        print(response.json())


estRegisterUser = estRegisterUser()
estRegisterUser.est_email_positive()
