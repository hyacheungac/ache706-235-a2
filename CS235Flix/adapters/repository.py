import abc

repo_instance = None

class RepositoryException(Exception):
    pass

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, user):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_title(self, title):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_count(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_actor(self, actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_genre(self, genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_director(self, director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_year(self, year):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_since_year(self, year):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews_by_movie(self, movie_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews_by_user(self, username):
        raise NotImplementedError