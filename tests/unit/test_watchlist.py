from CS235Flix.domainmodel.watchlist import WatchList, Movie


def test_init():
    watchlist = WatchList()
    print(f"Size of watchlist: {watchlist.size()}")


def test_add_movie():
    watchlist = WatchList()

    # test adding a movie while empty
    watchlist.add_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test adding a movie while not empty
    watchlist.add_movie(Movie("Ice Age", 2002))
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test adding a movie thats already in the list
    watchlist.add_movie(Movie("Ice Age", 2002))
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test adding something thats not a movie
    watchlist.add_movie("not a movie")
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())


def test_remove_movie():
    watchlist = WatchList()
    movies = [Movie("Moana", 2016), Movie("Ice Age", 2002)]

    # test removing the only movie in the list
    watchlist.add_movie(movies[0])
    watchlist.remove_movie(movies[0])
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test removing the first movie in the list
    watchlist.add_movie(movies[0])
    watchlist.add_movie(movies[1])
    watchlist.remove_movie(movies[0])
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test removing the last movie in the list
    watchlist.add_movie(movies[0])
    watchlist.add_movie(movies[1])
    watchlist.remove_movie(movies[1])
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test removing multiple movies
    watchlist.add_movie(movies[0])
    watchlist.add_movie(movies[1])
    watchlist.remove_movie(movies[0])
    watchlist.remove_movie(movies[1])
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test removing a movie thats not in the list
    watchlist.add_movie(movies[0])
    watchlist.remove_movie(movies[1])
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())

    # test removing something thats not a movie
    watchlist.add_movie(movies[1])
    watchlist.remove_movie("not a movie")
    print(f"Size of watchlist: {watchlist.size()}")
    print(watchlist.first_movie_in_watchlist())


def test_select_movie_to_watch():
    watchlist = WatchList()
    movies = [Movie("Moana", 2016), Movie("Ice Age", 2002)]

    # test selecting something below lower bound in an empty list
    print(watchlist.select_movie_to_watch(-1))
    # test selecting what would be the first movie in an empty list
    print(watchlist.select_movie_to_watch(0))
    # test selecting something above upper bound in an empty list
    print(watchlist.select_movie_to_watch(1))

    watchlist.add_movie(movies[0])
    watchlist.add_movie(movies[1])

    # test selecting something below lower bound
    print(watchlist.select_movie_to_watch(-1))
    # test selecting the first movie
    print(watchlist.select_movie_to_watch(0))
    # test selecting a different movie
    print(watchlist.select_movie_to_watch(1))
    # test selecting something above upper bound
    print(watchlist.select_movie_to_watch(2))


def test_size():
    watchlist = WatchList()

    # test size of an empty watch list
    print(f"Size of watchlist: {watchlist.size()}")

    # test size increases when a movie is added
    watchlist.add_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")

    # test size decreases when a movie is removed
    watchlist.remove_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")


def test_first_movie():
    watchlist = WatchList()
    movies = [Movie("Moana", 2016), Movie("Ice Age", 2002)]

    # test getting the first movie of an empty watchlist
    print(watchlist.first_movie_in_watchlist())

    # test getting the first movie of a watchlist
    watchlist.add_movie(movies[0])
    print(watchlist.first_movie_in_watchlist())

    # test getting the first movie of a 2 movie watchlist
    watchlist.add_movie(movies[1])
    print(watchlist.first_movie_in_watchlist())

def test_iter():
    watchlist = WatchList()
    movies = [Movie("Moana", 2016), Movie("Ice Age", 2002)]

    # iterate through an empty watchlist
    print("testing iter 1")
    for movie in watchlist:
        print(movie)

    # iterate through a 1 movie watchlist
    print("testing iter 2")
    watchlist.add_movie(movies[0])
    for movie in watchlist:
        print(movie)

    # iterate through a 2 movie watchlist
    print("testing iter 3")
    watchlist.add_movie(movies[1])
    for movie in watchlist:
        print(movie)
