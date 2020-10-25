import csv
import os
from datetime import datetime

from werkzeug.security import generate_password_hash

from CS235Flix.adapters.repository import AbstractRepository, RepositoryException
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.review import Review
from CS235Flix.domainmodel.user import User


class MemoryRepository(AbstractRepository):
    # assume rank is unique across all fields
    # assume username is unique

    def __init__(self):
        self._movie = []
        self._actors = set()
        self._directors = set()
        self._genres = set()
        self._users = []
        self._reviews = []


    def add_user(self, user):
        if type(user) is not User:
            raise TypeError("add_user() passed a non-user parameter")

        if user not in self._users:
            self._users.append(user)
            return True
        return False


    def get_user(self, username):
        if type(username) is not str:
            raise TypeError("get_user(username) passed a non-string parameter")

        if not username:
            raise ValueError("get_user(username) passed an empty string")

        username = username.lower()
        for user in self._users:
            if user.username == username:
                return user
        return None


    def get_user_by_id(self, user_id):
        if type(user_id) is not int:
            raise TypeError("get_user passed non-int")

        if not (0 < user_id <= len(self._users)):
            raise ValueError("get_user_by_id passed an illegal id")

        return self._users[user_id - 1]


    def add_movie(self, movie):
        if type(movie) is not Movie:
            raise TypeError("add_movie attempted to add non-movie to movie repository")

        if movie not in self._movie:
            self._movie.append(movie)
            self._directors.add(movie.director)
            self._genres |= set(movie.genres)
            self._actors |= set(movie.actors)
            return True
        return False


    def get_movie(self, movie_rank):
        if type(movie_rank) is not int:
            raise TypeError("get_movie passed non-int")

        if not (0 < movie_rank <= len(self._movie)):
            raise ValueError("get_movie passed an illegal rank")

        return self._movie[movie_rank - 1]


    def get_movie_by_title(self, title):
        if type(title) is not str:
            raise TypeError("get_movie_by_title requires a string as input")

        if not title:
            return []

        movie_found = []
        for movie in self._movie:
            if movie.title == title:
                movie_found.append(movie)

        return movie_found


    def get_movie_count(self):
        return len(self._movie)


    def get_movie_by_actor(self, actor):
        if type(actor) is not Actor:
            raise TypeError("get_movie_by_actor requires a string as input")

        movie_found = []
        for movie in self._movie:
            if actor in movie.actors:
                movie_found.append(movie)

        return movie_found


    def get_movie_by_genre(self, genre):
        if type(genre) is not Genre:
            raise TypeError("get_movie_by_genre passed a non-genre argument")

        movie_found = []
        for movie in self._movie:
            if genre in movie.genres:
                movie_found.append(movie)

        return movie_found


    def get_movie_by_director(self, director):
        if type(director) is not Director:
            raise TypeError("get_movie_by_director passed a non-director argument")

        movie_found = []
        for movie in self._movie:
            if movie.director == director:
                movie_found.append(movie)

        return movie_found


    def get_movie_by_year(self, year):
        if type(year) is not int:
            raise TypeError("get_movie_by_year requires an int argument")

        if year < 1900 or year >= 2021:
            return []

        movie_found = []
        for movie in self._movie:
            if movie.release_year == year:
                movie_found.append(movie)

        return movie_found


    def get_movie_since_year(self, year):
        if type(year) is not int:
            raise TypeError("get_movie_since_year requires an int argument")

        if year < 1900:
            return self._movie

        if year >= 2021:
            return []

        movie_found = []
        for movie in self._movie:
            if movie.release_year >= year:
                movie_found.append(movie)

        return movie_found


    def add_review(self, review):
        if type(review) is not Review:
            raise TypeError("cannot add non-Review object as a review")

        self._reviews.append(review)


    def remove_review(self, review):
        if type(review) is not Review:
            raise TypeError("cannot delete a non-Review object")

        if review in self._reviews:
            self._reviews.remove(review)


    def get_reviews_by_movie(self, movie):
        if type(movie) is not Movie:
            raise TypeError("get_reviews_by_movie must be passed movie")

        reviews_found = []
        for review in self._reviews:
            if review.movie == movie:
                reviews_found.append(review)
        return reviews_found


    def get_reviews_by_user(self, user):
        if type(user) is not User:
            raise TypeError("get_reviews_by_user requires a User type argument")
        return user.reviews


def load_movies(data_path, repo):
    filename = os.path.join(data_path, "Data1000Movies.csv")
    with open(filename, mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            movie_rank = int(row["Rank"])
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
            movie.rank = movie_rank

            for genre in genres:
                movie.add_genre(genre)

            for actor in actors:
                movie.add_actor(actor)

            repo.add_movie(movie)


def load_users(data_path, repo):
    filename = os.path.join(data_path, "users.csv")
    with open(filename, mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            if not any(row.values()):
                break

            user = User(row["username"], generate_password_hash(row["password"]))

            for movie_rank in row["movies"].split(";"):
                movie = repo.get_movie(int(movie_rank))
                user.watch_movie(movie)

            repo.add_user(user)


def load_reviews(data_path, repo):
    filename = os.path.join(data_path, "reviews.csv")
    with open(filename, mode='r') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            if not any(row.values()):
                break

            movie = repo.get_movie(int(row["movie-rank"]))
            user = repo.get_user_by_id(int(row["user-id"]))

            review = Review(movie, user, row["text"], int(row["rating"]))
            review.__timestamp = datetime.strptime(row["timestamp"], "%d/%m/%Y %H:%M")

            user.add_review(review)
            repo.add_review(review)


def populate(data_path, repo):
    load_movies(data_path, repo)
    load_users(data_path, repo)
    load_reviews(data_path, repo)