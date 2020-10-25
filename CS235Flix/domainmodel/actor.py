from CS235Flix.domainmodel.person import Person

class Actor(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.__colleagues = set()

    @property
    def actor_full_name(self) -> str:
        return self.full_name

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            self.__colleagues.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleagues
