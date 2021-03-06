from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from plot_hole import db, bcrypt
from plot_hole.users.forms import RegistrationForm, LoginForm
from plot_hole.models import User, Plot

users = Blueprint("users", __name__)


@users.route("/register", methods=("GET", "POST"))
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            username=form.email.data,
            email=form.email.data,
            password=hashed_password,
        )
        user.save()

        flash(f"Account created for {form.email.data}!")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=("GET", "POST"))
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
            user.password, form.password.data
        ):
            login_user(user, remember=False)
            next_page = request.args.get("next")
            flash("You have been logged in!")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("users.account"))
            )
        else:
            flash("Login Unsuccessful - Check Email or Password")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@users.route("/account")
@login_required
def account():
    count = Plot.objects(user=current_user.id).count()
    plots = Plot.objects(user=current_user.id)

    return render_template(
        "account.html",
        title="Account",
        count=count,
        plots=[plot for plot in plots],
    )
