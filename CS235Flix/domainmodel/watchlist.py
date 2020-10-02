from CS235Flix.domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watchlist = []

    def add_movie(self, movie):
        if movie and type(movie) == Movie and movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if movie and type(movie) == Movie and movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) == int and 0 <= index < self.size():
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) != 0:
            return self.__watchlist[0]

    def __iter__(self):
        self.__iter_idx = 0
        return self

    def __next__(self):
        if self.__iter_idx < self.size():
            self.__iter_idx += 1
            return self.__watchlist[self.__iter_idx - 1]
        else:
            raise StopIteration