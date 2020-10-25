import pytest

from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.review import Review

@pytest.fixture()
def user():
    return User('dbowie', '1234567890')

@pytest.fixture()
def movie():
    movie = Movie("Moana", 2000)
    movie.runtime_minutes = 12
    return movie


def test_user_construction(user):
    assert user.username == 'dbowie'
    assert user.password == '1234567890'
    assert user.time_spent_watching_movies_minutes == 0
    assert len(user.reviews) == 0
    assert len(user.watched_movies) == 0
    assert repr(user) == '<User dbowie>'

def test_user_watch_movie(user, movie):
    user.watch_movie(movie)
    assert user.time_spent_watching_movies_minutes == 12
    assert user.watched_movies == [movie]

def test_user_watch_duplicate_movie(user, movie):
    user.watch_movie(movie)
    user.watch_movie(movie)
    assert user.time_spent_watching_movies_minutes == 12
    assert user.watched_movies == [movie]

def test_user_add_review(user):
    review = Review(movie, user, "It's ok I guess", 6)
    user.add_review(review)
    assert user.reviews == [review]

def test_user_add_duplicate_review(user):
    review = Review(movie, user, "It's ok I guess", 6)
    user.add_review(review)
    user.add_review(review)
    assert user.reviews == [review]
