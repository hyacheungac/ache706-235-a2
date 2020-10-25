from flask import Blueprint, render_template, request, redirect
import CS235Flix.repository.abstract_repository as repo
from os import environ

search_blueprint = Blueprint("search_bp", __name__)

@search_blueprint.route("/search", methods=['GET'])
def search():
    args = request.args
    if "q" not in args:
        return redirect("/")
    n = int(args["n"]) if "n" in args else 0
    q = args["q"].lower()
    filter = args["filter"] if "filter" in args else "all"
    DISPLAY_AT_ONCE = int(environ.get("DISPLAY_AT_ONCE"))

    # if user is trying to start from a negative page number, take the user back to the first page of the same search
    if n < 0:
        return redirect("/search"
                        + ("/" + filter if filter else "")
                        + "?q=%s" % q.replace(" ", "+"))

    movie_count = repo.repo_instance.get_media_count()
    movies = []
    current = 1

    while current <= movie_count:
        media = repo.repo_instance.get_media(current)

        title = q in media.title.lower()
        actor = any([q in actor.full_name.lower() for actor in media.actors])
        director = q in media.director.full_name.lower()
        genre = any([q in genre.genre_name.lower() for genre in media.genres])

        filters = {"all": [title, actor, director, genre],
                   "title": [title],
                   "actor": [actor],
                   "director": [director],
                   "genre": [genre],
                  }

        if any(filters.get(filter, filters["all"])):
            movies.append(media)
        current += 1

    results_count = len(movies)
    pages = results_count // DISPLAY_AT_ONCE
    start = DISPLAY_AT_ONCE * n
    end = min(start + DISPLAY_AT_ONCE, results_count)
    if start > results_count:
        return redirect("/search"
                        + ("/" + filter if filter else "")
                        + "?q=%s" % q.replace(" ", "+")
                        + "&n=%d" % pages)

    url_previous = n - 1
    url_next = n+1 if end < results_count else 0
    to_display = movies[start:end]

    return render_template(
        'search.html',
        query=q,
        num_results=results_count,
        page=n+1,
        pages=pages+1,
        movies=to_display,
        url_previous=url_previous,
        url_next=url_next,
        filter=filter,
    )
