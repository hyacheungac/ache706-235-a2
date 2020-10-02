import datetime

from CS235Flix.domainmodel.movie import Movie

class Review:
    def __init__(self, movie, review_text, rating):
        if movie and type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None
        if review_text and type(review_text) is str:
            self.__review_text = review_text.strip()
        else:
            self.__review_text = None
        if rating and type(rating) is int and 0 < rating < 11:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.date.today()


    @property
    def movie(self):
        return self.__movie

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
        return (str(self.movie) + str(self.review_text) + str(self.rating) + str(self.timestamp)) == (str(other.movie) + str(other.review_text) + str(other.rating) + str(other.timestamp))