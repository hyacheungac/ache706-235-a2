from CS235Flix.domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watchlist = []

    def add_movie(self, movie):
        if movie and type(movie) is Movie and movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if movie and type(movie) is Movie and movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) is int and index >= 0 and index < self.size():
            return self.__watchlist[index]
        else:
            return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        return self.__watchlist[0] if self.__watchlist else None

    def __iter__(self):
        self.__iter_idx = 0
        return self

    def __next__(self):
        if self.__iter_idx < self.size():
            self.__iter_idx += 1
            return self.__watchlist[self.__iter_idx - 1]
        else:
            raise StopIteration
