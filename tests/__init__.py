import pytest

try:
    from CS235Flix.domainmodel.person import Person
except ImportError:
    # allow importing from the src directory
    import sys
    sys.path.append("CS235Flix")
