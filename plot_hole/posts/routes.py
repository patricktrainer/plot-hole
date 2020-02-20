from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from plot_hole.models import Plot
from plot_hole.posts.forms import PlotForm

posts = Blueprint("posts", __name__)


@posts.route("/map", methods=("GET", "POST"))
def map():
    form = PlotForm()
    plots = Plot.query.all()
    markers = [[plot.lat, plot.long] for plot in plots]
    if form.validate_on_submit():
        plot = Plot(lat=form.lat.data, long=form.long.data, author=current_user)
        db.session.add(plot)
        db.session.commit()
        flash("Plotted!", "is-primary")
        return redirect(url_for("posts.map"))
    return render_template("map.html", markers=markers, form=form)


@posts.route("/plot/<int:id>")
def plot(id):
    # plot = Plot.query.get(id)
    return render_template("plot.html")
