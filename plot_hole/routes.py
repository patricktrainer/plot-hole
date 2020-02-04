from flask import render_template, url_for, flash, redirect, request
from plot_hole import app, db, bcrypt
from plot_hole.forms import RegistrationForm, LoginForm, PlotForm
from plot_hole.models import User, Plot
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=("GET", "POST"))
def home():
    return render_template("home.html")


@app.route("/map", methods=("GET", "POST"))
def map():
    form = PlotForm()
    plots = Plot.query.all()
    if form.validate_on_submit():
        plot = Plot(lat=form.lat.data, long=form.long.data, author=current_user)
        db.session.add(plot)
        db.session.commit()
        flash("Plotted!", "is-primary")
        return redirect(url_for("map"))
    return render_template("map.html", plots=plots, form=form)


@app.route("/register", methods=("GET", "POST"))
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )

        user = User(
            username=form.email.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        flash(f"Account created for {form.email.data}!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=("GET", "POST"))
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            next_page = request.args.get("next")
            flash("You have been logged in!")
            return redirect(next_page) if next_page else redirect(url_for("map"))
        else:
            flash("Login Unsuccessful - Check Email or Password")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")


@app.route("/plots", methods=("GET", "POST"))
@login_required
def plots():
    form = PlotForm()
    if form.validate_on_submit():
        plot = Plot(lat=form.lat.data, long=form.long.data, author=current_user)
        db.session.add(plot)
        db.session.commit()
        flash("Posted!", "is-primary")
        return redirect(url_for("home"))
    return render_template("plot_form.html", plots=plots, form=form)
