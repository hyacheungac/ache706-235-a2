from CS235Flix.domainmodel.movie import Movie, Genre, Actor, Director


def test_equality():
    movie1 = Movie("Moana", 2000)
    movie2 = Movie("Moana", 2001)
    movie3 = Movie("Moana", 2000)
    movie4 = Movie("Moanb", 2000)

    assert movie1 != movie2
    assert movie1 == movie3
    assert movie1 != movie4

def test_sort():
    movie1 = Movie("Moana", 2000)
    movie2 = Movie("Moanb", 2000)
    movie3 = Movie("Moanb", 2001)

    assert movie1 < movie2
    assert movie1 < movie3
    assert movie2 < movie3

def test_hash():
    movie1 = Movie("Moana", 2000)
    movie2 = Movie("Moana", 2000)
    movie3 = Movie("Moana", 2001)

    movies = set([movie1, movie2, movie3])
    assert len(movies) == 2
    assert movie1 in movies
    assert movie2 in movies
    assert movie3 in movies

def test_title():
    movie1 = Movie("Moana", 2000)
    assert movie1.title == "Moana"
    movie1.title = "Moanb"
    assert movie1.title == "Moanb"
    movie1.title = "Moana "
    assert movie1.title == "Moana"
    movie1.title = "Moana  "
    assert movie1.title == "Moana"
    movie1.title = " Moana"
    assert movie1.title == "Moana"
    movie1.title = "  Moana"
    assert movie1.title == "Moana"
    movie1.title = " Moana "
    assert movie1.title == "Moana"
    movie1.title = "  Moana  "
    assert movie1.title == "Moana"

def test_description():
    movie1 = Movie("Moana", 2000)
    assert movie1.description == ""
    movie1.description = "test description"
    assert movie1.description == "test description"
    movie1.description = "test description "
    assert movie1.description == "test description"
    movie1.description = "test description  "
    assert movie1.description == "test description"
    movie1.description = " test description"
    assert movie1.description == "test description"
    movie1.description = "  test description"
    assert movie1.description == "test description"
    movie1.description = " test description "
    assert movie1.description == "test description"
    movie1.description = "  test description  "
    assert movie1.description == "test description"

def test_director():
    movie1 = Movie("Moana", 2000)
    assert movie1.director == Director(None)
    movie1.director = Director("Ron Clements")
    assert movie1.director == Director("Ron Clements")
    movie1.director = Director("Rob Clements")
    assert movie1.director == Director("Rob Clements")

def test_genres():
    movie1 = Movie("Moana", 2000)
    genres = [Genre("Comedy"), Genre("Horror")]
    assert movie1.genres == []
    movie1.add_genre(genres[0])
    assert movie1.genres == [Genre("Comedy")]
    movie1.add_genre(genres[1])
    assert movie1.genres == [Genre("Comedy"), Genre("Horror")]
    movie1.add_genre(genres[1])
    assert movie1.genres == [Genre("Comedy"), Genre("Horror")]
    movie1.remove_genre(genres[1])
    assert movie1.genres == [Genre("Comedy")]
    movie1.remove_genre(genres[1])
    assert movie1.genres == [Genre("Comedy")]
    movie1.remove_genre(genres[0])
    assert movie1.genres == []
    movie1.remove_genre(genres[0])
    assert movie1.genres == []

def test_runtime():
    movie1 = Movie("Moana", 2000)
    assert movie1.runtime_minutes == 0
    movie1.runtime_minutes = "3"
    assert movie1.runtime_minutes == 0
    movie1.runtime_minutes = None
    assert movie1.runtime_minutes == 0

    try:
        movie1.runtime_minutes = 0
    except ValueError:
        pass
    else:
        raise AssertionError
    assert movie1.runtime_minutes == 0

    try:
        movie1.runtime_minutes = -4
    except ValueError:
        pass
    else:
        raise AssertionError
    assert movie1.runtime_minutes == 0

    movie1.runtime_minutes = 12
    assert movie1.runtime_minutes == 12
