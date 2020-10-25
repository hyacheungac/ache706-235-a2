from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director

class Media(object):
    def __init__(self, title, release_year):
        self.__title = title.strip() if title and type(title) is str else None
        self.__release_year = (release_year if release_year and
                               type(release_year) is int and
                               release_year >= 1900 else None)
        self.__id = None

        self.__description = ""
        self.__director = Director(None)
        self.__actors = set()
        self.__runtime_minutes = 0

    @property
    def media_id(self):
        return self.__id

    @media_id.setter
    def media_id(self, id_val):
        self.__id = id_val

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if title and type(title) is str:
            self.__title = title.strip()

    @property
    def release_year(self):
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if description and type(description) is str:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director):
        if director and type(director) is Director:
            self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def runtime_minutes(self) -> str:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int:
            if runtime_minutes < 1:
                raise ValueError("runtime_minutes must be a positive number")
            self.__runtime_minutes = runtime_minutes

    def __repr__(self):
        return f"<{type(self).__name__} {self.title}, {self.release_year}>"

    def __eq__(self, other):
        return (self.__title == other.__title and
                self.__release_year == other.__release_year)

    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        return self.__title < other.__title

    def __hash__(self):
        return hash(repr(self))


    def add_actor(self, actor):
        if type(actor) is Actor and actor not in self.__actors:
            self.__actors.add(actor)

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)
