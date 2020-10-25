import os
import csv
from datetime import date, datetime
from werkzeug.security import generate_password_hash

from CS235Flix.repository.abstract_repository import AbstractRepository, RepositoryException
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.review import Review



class MemoryRepository(AbstractRepository):
    # id is assumed unique across all fields
    # username is assumed unique

    def __init__(self):
        self._media = []
        self._actors = set()
        self._directors = set()
        self._genres = set()
        self._users = []
        self._reviews = []


    def add_user(self, user):
        if type(user) is not User:
            raise TypeError("add_user() passed non-user parameter")

        if user not in self._users:
            self._users.append(user)
            return True
        return False


    def get_user(self, username):
        if type(username) is not str:
            raise TypeError("get_user(username) takes a string as parameter")

        if not username:
            raise ValueError("get_user(username) given an empty string")

        username = username.lower()
        for user in self._users:
            if user.username == username:
                return user
        return None


    def get_user_by_id(self, user_id):
        if type(user_id) is not int:
            raise TypeError("get_media passed non-int")

        if not (user_id > 0 and user_id <= len(self._users)):
            raise ValueError("get_user_by_id passed an illegal id")

        return self._users[user_id - 1]


    def add_media(self, media):
        if type(media) is not Movie:
            raise TypeError("attempted to add non-media to media repository")

        if media not in self._media:
            self._media.append(media)
            self._directors.add(media.director)
            self._genres |= set(media.genres)
            self._actors |= set(media.actors)
            return True
        return False


    def get_media(self, media_id):
        if type(media_id) is not int:
            raise TypeError("get_media passed non-int")

        if not (media_id > 0 and media_id <= len(self._media)):
            raise ValueError("get_media passed an illegal id")

        return self._media[media_id - 1]


    def get_media_by_title(self, title):
        if type(title) is not str:
            raise TypeError("get_media_by_title requires a string as input")

        if not title:
            return []

        media_found = []
        for media in self._media:
            if media.title == title:
                media_found.append(media)

        return media_found


    def get_media_count(self):
        return len(self._media)


    def get_media_by_actor(self, actor):
        if type(actor) is not Actor:
            raise TypeError("get_media_by_actor requires a string as input")

        media_found = []
        for media in self._media:
            if actor in media.actors:
                media_found.append(media)

        return media_found


    def get_media_by_genre(self, genre):
        if type(genre) is not Genre:
            raise TypeError("get_media_by_genre passed a non-genre argument")

        media_found = []
        for media in self._media:
            if genre in media.genres:
                media_found.append(media)

        return media_found


    def get_media_by_director(self, director):
        if type(director) is not Director:
            raise TypeError("get_media_by_director passed a non-director argument")

        media_found = []
        for media in self._media:
            if media.director == director:
                media_found.append(media)

        return media_found


    def get_media_by_year(self, year):
        if type(year) is not int:
            raise TypeError("get_media_by_year requires an int argument")

        if year < 1900:
            return []

        media_found = []
        for media in self._media:
            if media.release_year == year:
                media_found.append(media)

        return media_found


    def get_media_since_year(self, year):
        if type(year) is not int:
            raise TypeError("get_media_since_year requires an int argument")

        if year < 1900:
            return self._media

        if year >= 2021:
            return []

        media_found = []
        for media in self._media:
            if media.release_year >= year:
                media_found.append(media)

        return media_found


    def add_review(self, review):
        if type(review) is not Review:
            raise TypeError("cannot add non-Review object as a review")

        self._reviews.append(review)


    def remove_review(self, review):
        if type(review) is not Review:
            raise TypeError("cannot delete a non-Review object")

        if review in self._reviews:
            self._reviews.remove(review)


    def get_reviews_by_media(self, media):
        if type(media) is not Movie:
            raise TypeError("get_reviews_by_media must be passed Media")

        reviews_found = []
        for review in self._reviews:
            if review.movie == media:
                reviews_found.append(review)
        return reviews_found


    def get_reviews_by_user(self, user):
        if type(user) is not User:
            raise TypeError("get_reviews_by_user requires a User type argument")
        return user.reviews


def load_movies(data_path, repo):
    filename = os.path.join(data_path, "movies.csv")
    with open(filename, mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            media_id = row["Id"]
            title = row['Title']
            release_year = int(row['Year'])
            description = row["Description"]
            runtime_minutes = row["Runtime (Minutes)"]
            director = Director(row["Director"])
            genres = set([Genre(x) for x in row["Genre"].split(',')])
            actors = set([Actor(x) for x in row["Actors"].split(',')])

            movie = Movie(title, release_year)
            movie.description = description
            movie.runtime_minutes = runtime_minutes
            movie.director = director
            movie.media_id = media_id

            for genre in genres:
                movie.add_genre(genre)

            for actor in actors:
                movie.add_actor(actor)

            repo.add_media(movie)


def load_users(data_path, repo):
    filename = os.path.join(data_path, "users.csv")
    with open(filename, mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            if not any(row.values()):
                break

            user = User(row["username"], generate_password_hash(row["password"])
            )

            for media_id in row["movies"].split(";"):
                media = repo.get_media(int(media_id))
                user.watch_movie(media)

            repo.add_user(user)


def load_reviews(data_path, repo):
    filename = os.path.join(data_path, "reviews.csv")
    with open(filename, mode='r') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            if not any(row.values()):
                break

            media = repo.get_media(int(row["media-id"]))
            user = repo.get_user_by_id(int(row["user-id"]))

            review = Review(media, user, row["text"], int(row["rating"]))
            review.__timestamp = datetime.strptime(row["timestamp"],
                                                 "%d/%m/%Y %H:%M")

            user.add_review(review)
            repo.add_review(review)


def populate(data_path, repo):
    load_movies(data_path, repo)
    load_users(data_path, repo)
    load_reviews(data_path, repo)
