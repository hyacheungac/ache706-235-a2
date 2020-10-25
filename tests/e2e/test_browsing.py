import pytest

from flask import session

def test_start(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"class=\"movie\"" in response.data
    assert b'<button>Previous</button>' not in response.data
    assert b'<button>Next</button>' in response.data

def test_next_page(client):
    response = client.get("/?n=1")
    assert response.status_code == 200
    assert b"class=\"movie\"" in response.data
    assert b'<button>Previous</button>' in response.data
    assert b'<button>Next</button>' not in response.data

def test_page_number_over_limit(client):
    response = client.get("/?n=100")
    assert response.status_code == 302

def test_page_number_under_limit(client):
    response = client.get("/?n=-1")
    assert response.status_code == 302

def test_movie_with_reviews(client):
    response = client.get("/movie/2")
    assert response.status_code == 200
    assert b"know which movie this is" in response.data
    assert b"not received any reviews yet" not in response.data

def test_movie_with_no_reviews(client):
    response = client.get("/movie/3")
    assert response.status_code == 200
    assert b"2020" not in response.data
    assert b"not received any reviews yet" in response.data

