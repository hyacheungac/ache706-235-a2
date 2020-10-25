from CS235Flix.domainmodel.person import Person


def test_init():
    director1 = Person("Taika Waititi")
    assert repr(director1) == "<Person Taika Waititi>"
    director2 = Person("")
    assert director2.full_name is None
    director3 = Person(42)
    assert director3.full_name is None

def test_equality():
    director1 = Person("Taika Waititi")
    director2 = Person("")
    director3 = Person("Taika Waititi")

    assert director1 != director2
    assert director1 == director3

def test_sort():
    director1 = Person("a")
    director2 = Person("aa")
    director3 = Person("b")

    assert director1 < director2
    assert director1 < director3
    assert director2 < director3

def test_hash():
    director1 = Person("a")
    director2 = Person("a")
    director3 = Person("b")

    directors = set([director1, director2, director3])
    assert len(directors) == 2
    assert director1 in directors
    assert director2 in directors
    assert director3 in directors
