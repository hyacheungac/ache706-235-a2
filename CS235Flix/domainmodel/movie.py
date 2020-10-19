from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director

class Movie(object):
    def __init__(self, title: str, release_year: int):
        if title and type(title) == str:
            self.__title = title.strip()
        else:
            self.__title = None
        if release_year and type(release_year) == int and release_year >= 1900:
            self.__release_year = release_year
        else:
            raise ValueError("The release year must be 1900 or later!")
        self.__description = ""
        self.__director = Director("")
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0
        self.__rating = 0.0
        self.__votes = 0
        self.__revenue = 0.0
        self.__metascore = 0
        self.__rank = 0

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank):
        if rank > 0:
            self.__rank = rank

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) == str:
            self.__title = title.strip()
    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if type(description) == str:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director):
        if type(director) == Director:
            self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) == int:
            if runtime_minutes >= 1:
                self.__runtime_minutes = runtime_minutes
            else:
                raise ValueError("runtime_minutes must be a positive number!")

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == float:
            if 0 < rating < 10:
                self.__rating = rating
            else:
                raise ValueError("rating must be within the range 0 to 10!")

    @property
    def votes(self) -> int:
        return self.__votes

    @votes.setter
    def votes(self, votes):
        if type(votes) == int:
            if votes > 0:
                self.__votes = votes
            else:
                raise ValueError("Number of votes must be positive!")

    @property
    def revenue(self) -> float:
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        if type(revenue) == float:
            if revenue > 0:
                self.__revenue = revenue
            else:
                raise ValueError("revenue must be positive!")

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, metascore):
        if type(metascore) == int or metascore == "N/A":
            if metascore == "N/A" or metascore > 0:
                self.__metascore = metascore
            else:
                raise ValueError("metascore must be either between 0 and 100, or N/A!")

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        string1 = self.__title + "_" + str(self.__release_year)
        string2 = other.__title + "_" +str(other.__release_year)
        return string1 == string2

    def __lt__(self, other):
        string1 = self.__title + "_" + str(self.__release_year)
        string2 = other.__title + "_" + str(other.__release_year)
        return string1 < string2

    def __hash__(self):
        string = self.__title + "_" + str(self.__release_year)
        return hash(string)


    def add_actor(self, actor):
        if type(actor) == Actor and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) == Genre and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)