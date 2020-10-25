from CS235Flix.domainmodel.actor import Actor


def test_init():
    actor1 = Actor("Taika Waititi")
    assert repr(actor1) == "<Actor Taika Waititi>"
    actor2 = Actor("")
    assert actor2.actor_full_name is None
    actor3 = Actor(42)
    assert actor3.actor_full_name is None

def test_equality():
    actor1 = Actor("Taika Waititi")
    actor2 = Actor("")
    actor3 = Actor("Taika Waititi")

    assert actor1 != actor2
    assert actor1 == actor3

def test_sort():
    actor1 = Actor("a")
    actor2 = Actor("aa")
    actor3 = Actor("b")

    assert actor1 < actor2
    assert actor1 < actor3
    assert actor2 < actor3

def test_hash():
    actor1 = Actor("a")
    actor2 = Actor("a")
    actor3 = Actor("b")

    actors = set([actor1, actor2, actor3])
    assert len(actors) == 2
    assert actor1 in actors
    assert actor2 in actors
    assert actor3 in actors

def test_empty_colleagues():
    actor1 = Actor("a")
    actor2 = Actor("b")
    actor3 = Actor("c")

    assert not actor1.check_if_this_actor_worked_with(actor2)
    assert not actor1.check_if_this_actor_worked_with(actor3)

def test_add_colleague():
    actor1 = Actor("a")
    actor2 = Actor("b")
    actor3 = Actor("c")

    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2)
    assert not actor1.check_if_this_actor_worked_with(actor3)

def test_add_multiple_colleagues():
    actor1 = Actor("a")
    actor2 = Actor("b")
    actor3 = Actor("c")

    actor1.add_actor_colleague(actor2)
    actor1.add_actor_colleague(actor3)
    assert actor1.check_if_this_actor_worked_with(actor2)
    assert actor1.check_if_this_actor_worked_with(actor3)

def test_add_repeated_colleagues():
    actor1 = Actor("a")
    actor2 = Actor("b")

    actor1.add_actor_colleague(actor2)
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2)

def test_add_non_actor_colleague():
    actor1 = Actor("a")

    actor1.add_actor_colleague("b")
    assert not actor1.check_if_this_actor_worked_with("b")
