from CS235Flix.domainmodel.director import Director


def test_init():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None

def test_equality():
    director1 = Director("Taika Waititi")
    director2 = Director("")
    director3 = Director("Taika Waititi")

    assert director1 != director2
    assert director1 == director3

def test_sort():
    director1 = Director("a")
    director2 = Director("aa")
    director3 = Director("b")

    assert director1 < director2
    assert director1 < director3
    assert director2 < director3

def test_hash():
    director1 = Director("a")
    director2 = Director("a")
    director3 = Director("b")

    directors = set([director1, director2, director3])
    assert len(directors) == 2
    assert director1 in directors
    assert director2 in directors
    assert director3 in directors
