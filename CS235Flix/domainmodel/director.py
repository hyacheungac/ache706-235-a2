from CS235Flix.domainmodel.person import Person

class Director(Person):
    @property
    def director_full_name(self) -> str:
        return self.full_name