import requests


def admin_assert():
    session = requests.Session()
    response = session.post("https://restzilla.store/auth/login", json={
        "email": "test@test.com",
        "password": "test"
    })
    cookies = response.cookies
    response = session.get("https://restzilla.store/auth/users_all", cookies=cookies)
    session.cookies.clear()
    return response.json()
