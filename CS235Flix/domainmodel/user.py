class User:
    def __init__(self, user, pwd):
        self.__user = None
        if user and type(user) == str: self.__user = user.strip().lower()
        if pwd and type(pwd) is str:
            self.__password = pwd
        else:
            self.__password = None
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__user}>"

    def __eq__(self, other):
        return self.__user == other.__user

    def __lt__(self, other):
        return self.__user < other.__user

    def __hash__(self):
        return hash(self.__user)

    @property
    def user_name(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    def remove_review(self, review):
        if review in self.__reviews:
            self.__reviews.remove(review)