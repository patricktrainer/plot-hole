from flask import render_template, url_for, flash, redirect, request
from plot_hole import app
from plot_hole.forms import RegistrationForm, LoginForm
from plot_hole.models import User

plots = [{
    '-90.7314': '89.6431',
    '-90.6754': '89.7134',
    '-90.1234': '89.9873',
    '-90.5432': '89.5342',
    '-90.1625': '89.0987',
    '-90.1875': '89.7498'
}]


@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/plot')
def plot():
    return render_template('plots.html', plots=plots)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}!')
        return redirect(url_for('map'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for user in User.query.all():
            if user == form.email.data:

                flash('You have been logged in!')
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
