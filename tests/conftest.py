import os
import pytest

from CS235Flix.adapters.memory_repository import MemoryRepository, populate
from CS235Flix import create_app

test_dir = "C:/Users/85251/Downloads/COMPSCI notes (AucklandUni)/COMPSCI 235/A2/ache706-235-a2/tests"
TEST_DATA_PATH = os.path.join(test_dir, "data")
TEST_DATA_PATH2 = os.path.join(test_dir, "data2")

@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    populate(TEST_DATA_PATH, repo)
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH2,              # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()


class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username='rmaric', password='cLQ^C#oFXloS'):
        return self._client.post(
            '/login',
            data={'username': username, 'password': password}
        )

    def register(self, username, password):
        return self._client.post(
            '/register',
            data={'username': username, 'password': password}
        )


    def logout(self):
        return self._client.get('/logout')


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)