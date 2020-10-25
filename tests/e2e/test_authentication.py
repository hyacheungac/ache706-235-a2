import pytest

from flask import session

def test_login(client, auth):
    status_code = client.get('/login').status_code
    assert status_code == 200

    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['username'] == 'thorke'


def test_registration_new_user(client, auth):
    status_code = client.get('/register').status_code
    assert status_code == 200

    response = auth.register("testuser", "testpassword")
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['username'] == 'testuser'


def test_registration_existing_user(client, auth):
    status_code = client.get('/register').status_code
    assert status_code == 200

    response = auth.register("thorke", "cLQ^C#oFXloS")
    assert b"Your username is already taken" in response.data

    with client:
        client.get('/')
        assert "username" not in session

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        client.get('/')
        assert 'username' not in session

def test_cannot_review_logged_out(client, auth):
    response = client.get('/movie/3')
    assert b"Login to write your own review" in response.data

def test_can_review_logged_in(client, auth):
    auth.login()
    response = client.get('/movie/3')
    assert b"Login to write your own review" not in response.data

def test_cannot_edit_delete_others_review(client, auth):
    auth.login()
    response = client.get('/movie/1')
    assert b"footer" not in response.data

def test_can_edit_delete_own_review(client, auth):
    auth.login()
    response = client.get('/movie/2')
    assert b"footer" in response.data
