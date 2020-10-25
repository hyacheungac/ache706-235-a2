from flask import Blueprint, render_template, url_for, session

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

import CS235Flix.repository.abstract_repository as repo
from CS235Flix.domainmodel.review import Review


class ReviewForm(FlaskForm):
    text = StringField(validators=[DataRequired()],
                       render_kw={"placeholder": "Write a review..."})
    rating = IntegerField("Rating (input an integer between 1 and 10)",
                          [DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Submit')


movie_blueprint = Blueprint("movie_bp", __name__)

@movie_blueprint.route("/movie/<int:media_id>", methods=['GET', 'POST'])
def movie(media_id):
    form = ReviewForm()
    media = repo.repo_instance.get_media(media_id)

    if form.validate_on_submit():
        user = repo.repo_instance.get_user(session['username'])
        if user:
            review_text = form.text.data
            review_rating = int(form.rating.data)

            review = Review(media, user, review_text, review_rating)
            user.add_review(review)
            repo.repo_instance.add_review(review)

    reviews = repo.repo_instance.get_reviews_by_media(media)

    return render_template(
        'movie.html',
        form=form,
        movie=media,
        reviews=reviews,
        handler_url=url_for('movie_bp.movie', media_id=media_id),
    )
