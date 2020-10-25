# from CS235Flix.domainmodel.movie import Movie
# from CS235Flix.domainmodel.review import Review
from CS235Flix.domainmodel.person import Person

class User(Person):
    def __init__(self, usr, pwd):
        usr = usr.strip().lower() if usr and type(usr) is str else None
        super().__init__(usr)

        self.__password = pwd if pwd and type(pwd) is str else None
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def username(self):
        return self.full_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes


    def watch_movie(self, movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    def remove_review(self, review):
        if review in self.__reviews:
            self.__reviews.remove(review)





