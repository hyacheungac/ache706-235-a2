from flask import Blueprint, render_template, request, url_for, redirect
import CS235Flix.repository.abstract_repository as repo
from os import environ

index_blueprint = Blueprint("index_bp", __name__)

@index_blueprint.route('/', methods=['GET'])
def index():
    args = request.args
    n = int(args["n"]) if "n" in args else 0
    DISPLAY_AT_ONCE = int(environ.get("DISPLAY_AT_ONCE"))

    if n < 0:
        return redirect(url_for("index_bp.index"))

    movies = []
    movie_count = repo.repo_instance.get_media_count()
    start = movie_count - DISPLAY_AT_ONCE * n
    if start < 0:
        n = movie_count // DISPLAY_AT_ONCE
        return redirect(url_for("index_bp.index", n=n))

    print(movie_count)
    print(n)
    print(start)
    for i in range(start, max(start - DISPLAY_AT_ONCE,0), -1):
        movies.append(repo.repo_instance.get_media(i))

    url_previous = n - 1
    url_next = n+1 if start > DISPLAY_AT_ONCE else 0

    return render_template(
        'index.html',
        movies=movies,
        url_previous=url_previous,
        url_next=url_next,
    )
