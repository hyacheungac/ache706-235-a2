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
    def add_media(self, user):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media(self, media_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_title(self, title):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_count(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_actor(self, actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_genre(self, genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_director(self, director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_by_year(self, year):
        raise NotImplementedError

    @abc.abstractmethod
    def get_media_since_year(self, year):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews_by_media(self, media_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews_by_user(self, username):
        raise NotImplementedError
