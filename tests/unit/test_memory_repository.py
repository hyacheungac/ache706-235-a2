import pytest
from datetime import date, datetime

from CS235Flix.repository.abstract_repository import RepositoryException
from CS235Flix.domainmodel.media import Media
from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.review import Review

def test_repo_media_count(in_memory_repo):
    assert in_memory_repo.get_media_count() == 5


def test_repo_get_media(in_memory_repo):
    media = in_memory_repo.get_media(1)
    assert media == Media("Guardians of the Galaxy", 2014)


def test_repo_get_different_media(in_memory_repo):
    media = in_memory_repo.get_media(2)
    assert media == Media("Prometheus", 2012)


def test_repo_get_not_existing_media(in_memory_repo):
    with pytest.raises(ValueError):
        in_memory_repo.get_media(6)


def test_repo_get_media_not_id(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_media("test")


def test_repo_get_media_by_title(in_memory_repo):
    media = in_memory_repo.get_media_by_title("Prometheus")
    assert media == [Media("Prometheus", 2012)]


def test_repo_get_media_by_second_title(in_memory_repo):
    media = in_memory_repo.get_media_by_title("Split")
    assert media == [Media("Split", 2016)]


def test_repo_get_media_by_duplicate_title(in_memory_repo):
    media = in_memory_repo.get_media_by_title("Guardians of the Galaxy")
    assert media == [Media("Guardians of the Galaxy", 2014),
                     Media("Guardians of the Galaxy", 2011)]


def test_repo_get_media_by_bad_title(in_memory_repo):
    media = in_memory_repo.get_media_by_title("Galaxy Gaurdians")
    assert media == []


def test_repo_get_media_by_actor(in_memory_repo):
    media = in_memory_repo.get_media_by_actor(Actor("Matthew McConaughey"))
    assert media == [Media("Sing", 2016)]

def test_repo_get_media_by_different_actor(in_memory_repo):
    media = in_memory_repo.get_media_by_actor(Actor("Charlize Theron"))
    assert media == [Media("Guardians of the Galaxy", 2014),
                     Media("Prometheus", 2012),
                     Media("Guardians of the Galaxy", 2011)]


def test_repo_get_media_by_fake_actor(in_memory_repo):
    media = in_memory_repo.get_media_by_actor(Actor("Richard Dean Anderson"))
    assert media == []


def test_repo_get_media_by_non_actor(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_media_by_actor("text")


def test_repo_get_media_by_genre(in_memory_repo):
    media = in_memory_repo.get_media_by_genre(Genre("Horror"))
    assert media == [Media("Split", 2016)]


def test_repo_get_media_by_different_genre(in_memory_repo):
    media = in_memory_repo.get_media_by_genre(Genre("Sci-Fi"))
    assert media == [Media("Guardians of the Galaxy", 2014),
                     Media("Prometheus", 2012)]


def test_repo_get_media_by_fake_genre(in_memory_repo):
    media = in_memory_repo.get_media_by_genre(Genre("zzzz"))
    assert media == []


def test_repo_get_media_by_non_genre(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_media_by_genre("text")


def test_repo_get_media_by_director(in_memory_repo):
    media = in_memory_repo.get_media_by_director(Director("Ridley Scott"))
    assert media == [Media("Prometheus", 2012)]


def test_repo_get_media_by_different_director(in_memory_repo):
    media = in_memory_repo.get_media_by_director(Director("James Gunn"))
    assert media == [Media("Guardians of the Galaxy", 2014),
                     Media("Guardians of the Galaxy", 2011)]


def test_repo_get_media_by_fake_director(in_memory_repo):
    media = in_memory_repo.get_media_by_director(Director("fake"))
    assert media == []


def test_repo_get_media_by_non_director(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_media_by_director("text")


def test_repo_get_media_by_year(in_memory_repo):
    media = in_memory_repo.get_media_by_year(2014)
    assert media == [Media("Guardians of the Galaxy", 2014)]


def test_repo_get_media_by_different_year(in_memory_repo):
    media = in_memory_repo.get_media_by_year(2016)
    assert media == [Media("Split", 2016),
                     Media("Sing", 2016)]


def test_repo_get_media_by_bad_year(in_memory_repo):
    media = in_memory_repo.get_media_by_year(1900)
    assert media == []


def test_repo_get_media_by_string_year(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_media_by_year("text")


def test_repo_get_media_since_year(in_memory_repo):
    media = in_memory_repo.get_media_since_year(2016)
    assert media == [Media("Split", 2016),
                     Media("Sing", 2016)]


def test_repo_get_media_since_different_year(in_memory_repo):
    media = in_memory_repo.get_media_since_year(2014)
    assert media == [Media("Guardians of the Galaxy", 2014),
                     Media("Split", 2016),
                     Media("Sing", 2016)]


def test_repo_get_media_since_bad_year(in_memory_repo):
    media = in_memory_repo.get_media_since_year(2021)
    assert media == []


def test_repo_get_media_since_str_year(in_memory_repo):
    with pytest.raises(TypeError):
        in_memory_repo.get_media_since_year("text")


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


def test_repo_retrieve_media_review(in_memory_repo):
    media = in_memory_repo.get_media(1)
    reviews = in_memory_repo.get_reviews_by_media(media)
    assert len(reviews) == 2


def test_repo_retrieve_different_media_review(in_memory_repo):
    media = in_memory_repo.get_media(2)
    reviews = in_memory_repo.get_reviews_by_media(media)
    assert len(reviews) == 1


def test_repo_retrieve_fake_media_review(in_memory_repo):
    media = in_memory_repo.get_media(3)
    reviews = in_memory_repo.get_reviews_by_media(media)
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
    media = in_memory_repo.get_media(3)
    review = Review(media, user, "review text", 2)
    user.add_review(review)

    in_memory_repo.add_review(review)

    assert in_memory_repo.get_reviews_by_media(media)[-1] is review
    assert in_memory_repo.get_reviews_by_user(user)[-1] is review

