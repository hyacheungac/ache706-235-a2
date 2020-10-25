"""Initialize Flask app."""

import os

from flask import Flask

from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director
from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.movie import Movie
from CS235Flix.domainmodel.review import Review
from CS235Flix.domainmodel.user import User
from CS235Flix.domainmodel.watchlist import WatchList


import CS235Flix.adapters.repository as repo
from CS235Flix.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('C:/', 'Users', '85251', 'Downloads', 'COMPSCI notes (AucklandUni)', 'COMPSCI 235', 'A2', 'ache706-235-a2', 'CS235Flix', 'adapters', 'data')

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    # Build the application
    with app.app_context():
        from CS235Flix.blueprints import movie, authentication, review
        from CS235Flix.templates import index
        app.register_blueprint(index.index_blueprint)
        app.register_blueprint(movie.movie_blueprint)
        # app.register_blueprint(search.search_blueprint)
        app.register_blueprint(review.review_blueprint)
        app.register_blueprint(authentication.authentication_blueprint)

    return app