import pytest

from flask import session

def test_no_query(client):
    response = client.get("/search")
    assert response.status_code == 302

def test_basic_query_one_result(client):
    response = client.get("/search?q=Ridley+Scott")
    assert response.status_code == 200
    assert b'1 result ' in response.data

def test_basic_query_multiple_results(client):
    response = client.get("/search?q=James+Gunn")
    assert response.status_code == 200
    assert b'2 results ' in response.data

def test_basic_query_multiple_results2(client):
    response = client.get("/search?q=Chris")
    assert response.status_code == 200
    assert b'4 results ' in response.data

def test_filter_results_title(client):
    response = client.get("/search?q=Chris&filter=title")
    assert response.status_code == 200
    assert b'0 results ' in response.data

def test_filter_results_genre(client):
    response = client.get("/search?q=Chris&filter=genre")
    assert response.status_code == 200
    assert b'0 results ' in response.data

def test_filter_results_actor(client):
    response = client.get("/search?q=Chris&filter=actor")
    assert response.status_code == 200
    assert b'3 results ' in response.data

def test_filter_results_director(client):
    response = client.get("/search?q=Chris&filter=director")
    assert response.status_code == 200
    print(response.data)
    assert b'1 result ' in response.data

def test_page_one(client):
    response = client.get("/search?q=e")
    assert response.status_code == 200
    print(response.data)
    assert b'page 1 of 2' in response.data
    assert b'Previous' not in response.data
    assert b'Next' in response.data

def test_page_two(client):
    response = client.get("/search?q=e&n=1")
    assert response.status_code == 200
    print(response.data)
    assert b'page 2 of 2' in response.data
    assert b'Previous' in response.data
    assert b'Next' not in response.data

