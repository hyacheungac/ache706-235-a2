
from flask import Blueprint, render_template, request, url_for, redirect
import CS235Flix.adapters.repository as repo
from os import environ

index_blueprint = Blueprint("index_bp", __name__)

@index_blueprint.route('/', methods=['GET'])
def index():
    args = request.args
    n = int(args["n"]) if "n" in args else 0
    display_at_once = int(environ.get("DISPLAY_AT_ONCE"))

    if n < 0:
        return redirect(url_for("index_bp.index"))

    movies = []
    movie_count = repo.repo_instance.get_movie_count()
    start = movie_count - display_at_once * n
    if start < 0:
        n = movie_count // display_at_once
        return redirect(url_for("index_bp.index", n=n))

    print(movie_count)
    print(n)
    print(start)
    for i in range(start, max(start - display_at_once,0), -1):
        movies.append(repo.repo_instance.get_movie(i))

    url_previous = n - 1
    url_next = n+1 if start > display_at_once else 0

    return render_template(
        'index.html',
        movies=movies,
        url_previous=url_previous,
        url_next=url_next,
    )