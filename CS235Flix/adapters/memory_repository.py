import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from CS235Flix.adapters.repository import AbstractRepository, RepositoryException
from CS235Flix.domainmodel import movie
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.review import Review
from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.watchlist import WatchList
from CS235Flix.data.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository(AbstractRepository):
    # movies ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._genres = list()
        self._users = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.rank] = movie

    def get_movie(self, rank: int) -> Movie:
        movie = None
        try:
            movie = self._movies_index[rank]
        except KeyError:
            pass  # Ignore exception and return None.
        return movie

    def get_movies_by_release_year(self, target_year: int) -> List[Movie]:
        target_movie = Movie(
            release_year=target_year,
            title=None,
        )
        matching_movies = list()
        try:
            index = self.movie_index(target_movie)
            for movie in self._movies[index:None]:
                if movie.release_year == target_year:
                    matching_movies.append(movie)
                else:
                    break
        except ValueError:
            # No movies for specified date. Simply return an empty list.
            pass
        return matching_movies

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None
        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self):
        movie = None
        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_rank(self, rank_list):
        # Strip out any ranks in rank_list that don't represent movie ranks in the repository.
        existing_ranks = [rank for rank in rank_list if rank in self._movies_index]

        # Fetch the movies.
        movies = [self._movies_index[rank] for rank in existing_ranks]
        return movies

    def get_movie_ranks_by_genre(self, genre: Genre):
        # Linear search, to find the first occurrence of a genre with the name genre.
        genre = next((genre for genre in self._genres if genre.genre_name == genre), None)

        # Retrieve the ranks of movies associated with the genre.
        if genre is not None:
            movie_ranks = [Movie.rank for genre in Movie.genres]
        else:
            # No genre with name genre_name, so return an empty list.
            movie_ranks = list()

        return movie_ranks

    def get_title_of_previous_movie(self, movie: Movie):
        previous_movie = None

        try:
            index = self.movie_index(movie)
            previous_movie = self._movies_index[index - 1]
        except ValueError:
            # No earlier movies, so return None.
            pass

        return previous_movie

    def get_title_of_next_movie(self, movie: Movie):
        next_movie = None

        try:
            index = self.movie_index(movie)
            next_movie = self._movies_index[index + 1]
        except ValueError:
            # No subsequent movies, so return None.
            pass

        return next_movie

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self._genres

    def add_review(self, review: Review):
        super().add_review(review)
        self._reviews.append(review)

    def get_reviews(self):
        return self._reviews

    # Helper method to return movie index.
    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        if index != len(self._movies) and self._movies[index].release_year == movie.release_year:
            return index
        raise ValueError


def load_movies_and_genres(data_path: str, repo: MemoryRepository):
    for movie in MovieFileCSVReader(data_path).get_dataset_of_movies():
        repo.add_movie(movie)
    repo._genres = MovieFileCSVReader(data_path).get_dataset_of_genres()


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row

def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(data_row[1],generate_password_hash(data_row[2]))
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def load_reviews(data_path: str, repo: MemoryRepository, users):
    for data_row in read_csv_file(os.path.join(data_path, '')):
        review = Review(
            review_text=data_row[3],
            user=users[data_row[1]],
            movie=repo.get_movie(int(data_row[2])),
            timestamp=datetime.fromisoformat(data_row[4])
        )
        repo.add_review(review)


def populate(data_path: str, repo: MemoryRepository):
    # Load movies and genres into the repository.
    load_movies_and_genres(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load reviews into the repository.
    load_reviews(data_path, repo, users)
