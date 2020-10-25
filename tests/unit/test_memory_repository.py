import pytest
from datetime import date, datetime

from CS235Flix.adapters.memory_repository import MemoryRepository, RepositoryException
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.review import Review

def test_repo_movie_count(in_memory_repo):
    assert in_memory_repo.get_movie_count() == 5


def test_repo_get_not_existing_movie(in_memory_repo):
    with pytest.raises(ValueError):
        in_memory_repo.get_movie(6)


def test_repo_get_movie_not_id(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_movie("test")


def test_repo_get_movie_by_bad_title(in_memory_repo):
    movie = in_memory_repo.get_movie_by_title("Galaxy Gaurdians")
    assert movie == []


def test_repo_get_movie_by_fake_actor(in_memory_repo):
    movie = in_memory_repo.get_movie_by_actor(Actor("Richard Dean Anderson"))
    assert movie == []


def test_repo_get_movie_by_non_actor(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_movie_by_actor("text")


def test_repo_get_movie_by_fake_genre(in_memory_repo):
    movie = in_memory_repo.get_movie_by_genre(Genre("zzzz"))
    assert movie == []


def test_repo_get_movie_by_non_genre(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_movie_by_genre("text")


def test_repo_get_movie_by_director(in_memory_repo):
    movie = in_memory_repo.get_movie_by_director(Director("Ridley Scott"))
    assert movie == [movie("Prometheus", 2012)]


def test_repo_get_movie_by_different_director(in_memory_repo):
    movie = in_memory_repo.get_movie_by_director(Director("James Gunn"))
    assert movie == [movie("Guardians of the Galaxy", 2014),
                     movie("Guardians of the Galaxy", 2011)]


def test_repo_get_movie_by_fake_director(in_memory_repo):
    movie = in_memory_repo.get_movie_by_director(Director("fake"))
    assert movie == []


def test_repo_get_movie_by_non_director(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_movie_by_director("text")


def test_repo_get_movie_by_year(in_memory_repo):
    movie = in_memory_repo.get_movie_by_year(2014)
    assert movie == [movie("Guardians of the Galaxy", 2014)]


def test_repo_get_movie_by_different_year(in_memory_repo):
    movie = in_memory_repo.get_movie_by_year(2016)
    assert movie == [movie("Split", 2016),
                     movie("Sing", 2016)]


def test_repo_get_movie_by_bad_year(in_memory_repo):
    movie = in_memory_repo.get_movie_by_year(1900)
    assert movie == []


def test_repo_get_movie_by_string_year(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_movie_by_year("text")


def test_repo_get_movie_since_year(in_memory_repo):
    movie = in_memory_repo.get_movie_since_year(2016)
    assert movie == [movie("Split", 2016),
                     movie("Sing", 2016)]


def test_repo_get_movie_since_different_year(in_memory_repo):
    movie = in_memory_repo.get_movie_since_year(2014)
    assert movie == [movie("Guardians of the Galaxy", 2014),
                     movie("Split", 2016),
                     movie("Sing", 2016)]


def test_repo_get_movie_since_bad_year(in_memory_repo):
    movie = in_memory_repo.get_movie_since_year(2021)
    assert movie == []


def test_repo_get_movie_since_str_year(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_movie_since_year("text")


def test_repo_add_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user


def test_repo_retrieve_user(in_memory_repo):
    user = in_memory_repo.get_user("admin")
    assert user == User("admin", "admin")


def test_repo_retrieve_different_user(in_memory_repo):
    user = in_memory_repo.get_user("guest")
    assert user == User("guest", "password")


def test_repo_retrieve_fake_user(in_memory_repo):
    user = in_memory_repo.get_user("fake")
    assert user is None


def test_repo_retrieve_numeric_user(in_memory_repo):
    with pytest.raises(TypeError):
        user = in_memory_repo.get_user(1)


def test_repo_retrieve_movie_review(in_memory_repo):
    movie = in_memory_repo.get_movie(1)
    reviews = in_memory_repo.get_reviews_by_movie(movie)
    assert len(reviews) == 2


def test_repo_retrieve_different_movie_review(in_memory_repo):
    movie = in_memory_repo.get_movie(2)
    reviews = in_memory_repo.get_reviews_by_movie(movie)
    assert len(reviews) == 1


def test_repo_retrieve_fake_movie_review(in_memory_repo):
    movie = in_memory_repo.get_movie(3)
    reviews = in_memory_repo.get_reviews_by_movie(movie)
    assert len(reviews) == 0


def test_repo_retrieve_user_review(in_memory_repo):
    user = in_memory_repo.get_user("guest")
    reviews = in_memory_repo.get_reviews_by_user(user)
    assert len(reviews) == 2


def test_repo_retrieve_different_user_review(in_memory_repo):
    user = in_memory_repo.get_user("admin")
    reviews = in_memory_repo.get_reviews_by_user(user)
    assert len(reviews) == 1


def test_repo_retrieve_fake_user_review(in_memory_repo):
    user = User('Dave', '123456789')
    reviews = in_memory_repo.get_reviews_by_user(user)
    assert len(reviews) == 0


def test_repo_add_review(in_memory_repo):
    user = in_memory_repo.get_user("admin")
    movie = in_memory_repo.get_movie(3)
    review = Review(movie, user, "review text", 2)
    user.add_review(review)

    in_memory_repo.add_review(review)

    assert in_memory_repo.get_reviews_by_movie(movie)[-1] is review
    assert in_memory_repo.get_reviews_by_user(user)[-1] is review

