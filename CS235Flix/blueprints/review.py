from flask import Blueprint, render_template, redirect, session, request, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

import CS235Flix.adapters.repository as repo
from CS235Flix.domainmodel.review import Review

class ReviewForm(FlaskForm):
    text = StringField(validators=[DataRequired()],
                       render_kw={"placeholder": "Write a review..."})
    rating = IntegerField("Rating (input an integer between 1 and 10)",
                          [DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Submit')


review_blueprint = Blueprint("review_bp", __name__)


@review_blueprint.route("/delete/<review_hash>", methods=['GET'])
def delete(review_hash):
    review_hash = int(review_hash)
    user = repo.repo_instance.get_user(session['username'])

    for review in user.reviews:
        if hash(review) == review_hash:
            user.remove_review(review)
            repo.repo_instance.remove_review(review)
            break

    return redirect(request.referrer)


@review_blueprint.route("/edit/<review_hash>", methods=['GET', "POST"])
def edit(review_hash):
    review_hash = int(review_hash)
    form = ReviewForm()
    review = None

    user = repo.repo_instance.get_user(session['username'])
    for review_candidate in user.reviews:
        if hash(review_candidate) == review_hash:
            review = review_candidate
            break

    if "edit" not in request.referrer:
        session["edit-referrer"] = request.referrer

    if review and form.validate_on_submit():
        review_text = form.text.data
        review_rating = int(form.rating.data)
        review.edit(review_text, review_rating)

        redirect_url = session["edit-referrer"]
        session["edit-referrer"] = None
        return redirect(redirect_url)

    return render_template(
        'edit.html',
        review=review,
        form=form,
        handler_url=url_for('review_bp.edit', review_hash=review_hash),
    )