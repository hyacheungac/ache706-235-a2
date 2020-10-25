import pytest

try:
    from CS235Flix.domainmodel.actor import Actor
    from CS235Flix.domainmodel.director import Director
    from CS235Flix.domainmodel.genre import Genre
    from CS235Flix.domainmodel.movie import Movie
    from CS235Flix.domainmodel.review import Review
    from CS235Flix.domainmodel.user import User
    from CS235Flix.domainmodel.watchlist import WatchList
except ImportError:
    # allow importing from the CS235Flix directory
    import sys
    sys.path.append("CS235Flix")
