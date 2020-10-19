import random
from CS235Flix.data.movie_file_csv_reader import MovieFileCSVReader
from CS235Flix.domainmodel import movie
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.director import Director


def pick_from_actor(actor : Actor):
    filename = "C:/Users/85251/Downloads/COMPSCI notes (AucklandUni)/COMPSCI 235/CS235FlixSkeleton/datafiles/Data1000Movies.csv"
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    actors = movie_file_reader.get_dataset_of_actors()
    valid_movie_list = [movie if actor in actors else None]
    seed = len(valid_movie_list)
    return valid_movie_list[random.randint(0, seed - 1)]

def pick_from_director(director: Director):
        filename = "C:/Users/85251/Downloads/COMPSCI notes (AucklandUni)/COMPSCI 235/CS235FlixSkeleton/datafiles/Data1000Movies.csv"
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        directors = movie_file_reader.get_dataset_of_directors()
        valid_movie_list = [movie if director in directors else None]
        seed = len(valid_movie_list)
        return valid_movie_list[random.randint(0, seed - 1)]

def pick_from_genre(genre: Genre):
        filename = "C:/Users/85251/Downloads/COMPSCI notes (AucklandUni)/COMPSCI 235/CS235FlixSkeleton/datafiles/Data1000Movies.csv"
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        genres = movie_file_reader.get_dataset_of_genres()
        valid_movie_list = [movie if genre in genres else None]
        seed = len(valid_movie_list)
        return valid_movie_list[random.randint(0, seed - 1)]
