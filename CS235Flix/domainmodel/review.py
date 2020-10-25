from datetime import datetime

from CS235Flix.domainmodel.movie import Movie

class Review:
    def __init__(self, movie, user, review_text, rating):
        self.__movie = movie if movie and type(movie) is Movie else None

        self.__review_text = (review_text if review_text and
                              type(review_text) is str else None)

        self.__rating = (rating if type(rating) is int and
                         1 <= rating <= 10 else None)

        self.__timestamp = datetime.today()
        self.__user = user


    @property
    def movie(self):
        return self.__movie

    @property
    def user(self):
        return self.__user

    @property
    def hash(self):
        return hash(self)

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp


    def __repr__(self):
        return f"<Review {repr(self.__movie)}, {self.__timestamp}>"

    def __eq__(self, other):
        return (self.movie == other.movie
                and self.review_text == other.review_text
                and self.rating == other.rating
                and self.timestamp == other.timestamp)

    def __hash__(self):
        return hash(self.__timestamp)

    def edit(self, text, rating):
        self.__review_text = text
        self.__rating = rating
        self.__timestamp = datetime.today()

