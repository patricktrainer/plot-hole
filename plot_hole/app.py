from flask import Flask, render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a4f2d0f8ca8ffdf793fe0b9a0562f32e'

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
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            # flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
