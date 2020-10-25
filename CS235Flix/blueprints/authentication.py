from flask import Blueprint, render_template, redirect, url_for, session, request

from functools import wraps
from flask_wtf import FlaskForm
from password_validator import PasswordValidator
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

from CS235Flix.domainmodel.user import User
import CS235Flix.adapters.repository as repo

# Configure Blueprint.
authentication_blueprint = Blueprint(
    'authentication_bp', __name__, url_prefix='/authentication')


@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    error = None

    if form.validate_on_submit():
        # Successful POST, username and password valid.
        password = generate_password_hash(form.password.data)
        user = User(form.username.data, password)
        unique_username = repo.repo_instance.add_user(user)

        if unique_username:
            session.clear()
            session['username'] = user.username
            return redirect(url_for('index_bp.index'))

        else:
            error = 'Your username is already taken - please supply another'

    # For a GET or a failed POST request, return the Registration Web page.
    return render_template(
        'credentials.html',
        title='Register',
        form=form,
        username_error_message=error,
        password_error_message=None,
        handler_url=url_for('authentication_bp.register'),
    )

@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username_error = None
    password_error = None

    if form.validate_on_submit():
        # Successful POST, username and password valid
        try:
            user = repo.repo_instance.get_user(form.username.data)
            if not user:
                username_error = "Username not recognised - please supply another"

            valid = check_password_hash(user.password, form.password.data)
            if user and not valid:
                password_error = "Invalid password - please try again"

            # Initialise session and redirect the user to the home page.
            if user and valid:
                session.clear()
                session['username'] = user.username
                return redirect(url_for('index_bp.index'))
        except:
            pass

    # For a GET or a failed POST, return the Login Web page.
    return render_template(
        'credentials.html',
        title='Login',
        username_error_message=username_error,
        password_error_message=password_error,
        form=form,
    )


@authentication_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home_bp.home'))


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'username' not in session:
            return redirect(url_for('authentication_bp.login'))
        return view(**kwargs)
    return wrapped_view


class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must at least 8 characters, and contain an upper case letter, a lower case letter and a digit'
        self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(8) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    username = StringField('Username', [
        DataRequired(message='Your username is required'),
        Length(min=3, message='Your username is too short')])
    password = PasswordField('Password', [
        DataRequired(message='Your password is required'),
        PasswordValid()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired()])
    submit = SubmitField('Login')
