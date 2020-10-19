import abc
from typing import List

from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.review import Review

repo_instance = None

class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.
        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds a Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, rank: int) -> Movie:
        """ Returns Movie with rank from the repository.
        If there is no Movie with the given rank, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_release_year(self, target_year: int) -> List[Movie]:
        """ Returns a list of Movies that were published on release_year.
        If there are no Movie on the given release_year, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Articles in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first Movie, ordered by rank, from the repository.
        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the last Movie, ordered by rank, from the repository.
        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, rank_list):
        """ Returns a list of Movies, whose rank match those in rank_list, from the repository.
        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ranks_by_genre(self, genre: Genre):
        """ Returns a list of ranks representing Movies that are in the same Genre.
        If there are no Movies that are in the same Genre, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_title_of_previous_movie(self, movie: Movie):
        """ Returns the title of a Movie that immediately precedes movie.
        If Movie is the first Movie in the repository, this method returns None because there are no Movies on a previous rank.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_title_of_next_movie(self, movie: Movie):
        """ Returns the title of a Movie that immediately succeeds movie.
        If Movie is the last Movie in the repository, this method returns None because there are no Movies on a later rank.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the Genres stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Comment to the repository.
        If the Comment doesn't have bidirectional links with a Movie and a User, this method raises a
        RepositoryException and doesn't update the repository.
        """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Comment not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Comment not correctly attached to an Movie')

    @abc.abstractmethod
    def get_reviews(self):
        """ Returns the Reviews stored in the repository. """
        raise NotImplementedError