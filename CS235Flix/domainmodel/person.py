class Person(object):
    def __init__(self, full_name: str):
        if full_name == "" or type(full_name) is not str:
            self.__full_name = None
        else:
            self.__full_name = full_name.strip()

    @property
    def full_name(self) -> str:
        return self.__full_name

    def __repr__(self):
        return f"<{type(self).__name__} {self.__full_name}>"

    def __eq__(self, other):
        return self.full_name == other.full_name

    def __lt__(self, other):
        return self.full_name < other.full_name

    def __hash__(self):
        return hash(self.full_name)
