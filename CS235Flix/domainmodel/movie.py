from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.media import Media

class Movie(Media):
    def __init__(self, title: str, release_year: int):
        super().__init__(title, release_year)
        self.__genres = []

    @property
    def genres(self) -> list:
        return self.__genres

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
