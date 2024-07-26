import pytest
from api.api_user import ApiUser


@pytest.fixture(scope='function')
def random_user():
    payload = ApiUser.create_random_user()

    yield payload

    response = ApiUser.login_user(email=payload['email'], password=payload['password'])
    token = response.json()['accessToken']
    ApiUser.delete_user(token)


@pytest.fixture(scope='function')
def get_random_user_token(random_user):
    response = ApiUser.login_user(email=random_user['email'], password=random_user['password'])
    token = response.json()['accessToken']

    yield token

    ApiUser.delete_user(token)

