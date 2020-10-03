import csv

from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csv_file:
            movie_file_reader = csv.DictReader(csv_file)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                description = row["Description"]
                runtime_minutes = row["Runtime (Minutes)"]
                director = Director(row["Director"])
                genres = set([Genre(genre) for genre in row["Genre"].split(',')])
                actors = set([Actor(name) for name in row["Actors"].split(',')])
                rating = row["Rating"]
                votes = int(row["Votes"])
                revenue = row["Revenue (Millions)"]
                metascore = row["Metascore"]

                movie = Movie(title, release_year)
                movie.description = description
                movie.runtime_minutes = runtime_minutes
                movie.director = director
                movie.genre = genres
                movie.actor = actors
                movie.rating = rating
                movie.votes = votes
                movie.revenue = revenue
                movie.metascore = metascore

                self.__dataset_of_directors.add(director)
                self.__dataset_of_genres |= genres
                self.__dataset_of_actors |= actors
                self.__dataset_of_movies.append(movie)

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    def get_dataset_of_movies(self):
        return self.__dataset_of_movies

    def get_dataset_of_actors(self):
        return self.__dataset_of_actors

    def get_dataset_of_directors(self):
        return self.__dataset_of_directors

    def get_dataset_of_genres(self):
        return self.__dataset_of_genres