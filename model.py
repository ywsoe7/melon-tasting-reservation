"""Models for reservation app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(25), nullable=False)

    appointment = db.relationship('Appointment', back_populates='user')

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>"


class Appointment(db.Model):
    """An appointment."""

    __tablename__ = 'appointments'

    appointment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable= False)

    user = db.relationship('Appointment', back_populates='appointment')

    def __repr__(self):
        return f"<Appointment appointment_id={self.appointment_id} date={self.date} time={self.start_time} to {self.end_time}>"


def connect_to_db(flask_app, db_uri="postgresql:///reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)