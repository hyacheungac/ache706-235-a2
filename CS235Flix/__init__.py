"""Initialize Flask app."""

import os

from flask import Flask

try:
    from CS235Flix.domainmodel.person import Person
except ImportError:
    # allow importing from the src directory
    import sys
    sys.path.append("src")

import CS235Flix.repository.abstract_repository as repo
from CS235Flix.repository.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('CS235Flix', 'repository', 'datafiles')

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    # Build the application
    with app.app_context():
        # @app.errorhandler(404)
        # def page_not_found(e):
        #     return render_template('404.html'), 404

        from CS235Flix.blueprints import index, movie, search, authentication, review
        app.register_blueprint(index.index_blueprint)
        app.register_blueprint(movie.movie_blueprint)
        app.register_blueprint(search.search_blueprint)
        app.register_blueprint(review.review_blueprint)
        app.register_blueprint(authentication.authentication_blueprint)

    return app
