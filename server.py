"""Server for Melon Tasting Reservation app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud, random

from datetime import datetime, date
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/login", methods=['POST'])
def process_login():
    """Process user login."""

    username = request.form.get("username")

    user = crud.get_user_by_username(username)

    if not user:
        flash("Please enter a valid username.")
        return redirect("/")
    else:
        session["user_id"] = user.id,
        session["username"] = username,
        flash(f"Welcome back, {user.fname}!")

        return redirect("/reservation")

@app.route("/appointment-list-<user_id>")
def get_appointment_list(user_id):

    appointment_list = crud.get_appointment_by_user(user_id)

    print(appointment_list)

    if not appointment_list:
        return jsonify({"msg": "There are no appointments scheduled."})
    else:
        
        for item in appointment_list:
            [appt_id, date, start_time, end_time, user_id] = appointment_list
        
        return jsonify(date = date,
                        start_time = start_time,
                        end_time = end_time)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)