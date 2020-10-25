from CS235Flix.domainmodel.genre import Genre


def test_init():
    genre1 = Genre("Horror")
    genre2 = Genre("")
    genre3 = Genre(12)

    assert repr(genre1) == "<Genre Horror>"
    assert repr(genre2) == "<Genre None>"
    assert genre2.genre_name is None
    assert genre3.genre_name is None

def test_equality():
    genre1 = Genre("Horror")
    genre2 = Genre("")
    genre3 = Genre("Horror")

    assert genre1 != genre2
    assert genre1 == genre3

def test_sort():
    genre1 = Genre("a")
    genre2 = Genre("aa")
    genre3 = Genre("b")

    assert genre1 < genre2
    assert genre1 < genre3
    assert genre2 < genre3

def test_hash():
    genre1 = Genre("a")
    genre2 = Genre("a")
    genre3 = Genre("b")

    genres = set([genre1, genre2, genre3])
    assert len(genres) == 2
    assert genre1 in genres
    assert genre2 in genres
    assert genre3 in genres
