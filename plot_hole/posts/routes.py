from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from plot_hole import db
from plot_hole.models import Plot
from plot_hole.posts.forms import PlotForm

posts = Blueprint("posts", __name__)


@posts.route("/map", methods=("GET", "POST"))
def map():
    form = PlotForm()

    if form.validate_on_submit():
        plot = Plot(plot=[form.lat.data, form.long.data], user=current_user.id)
        plot.save()
        flash("Plotted!", "is-primary")
        return redirect(url_for("posts.map"))
    return render_template("map.html", form=form)


@posts.route("/api/get_plots")
def get_plots():
    plot = Plot.objects()
    return render_template("plot.html", plot=plot)


@posts.route("/plot_pothole")
def plot_pothole():
    longitude = request.args.get("longitude", type=float)
    latitude = request.args.get("latitude", type=float)

    if current_user.is_authenticated:
        plot = Plot(plot=[longitude, latitude], user=current_user.id)
        plot.save()
        flash("Plotted!", "is-primary")
        return redirect(url_for("posts.map"))
    flash("You must be logged in to do that!", "is-warning")
    return redirect(url_for("posts.map"))
