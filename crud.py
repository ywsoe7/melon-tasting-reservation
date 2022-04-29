"""CRUD operations."""

from model import db, User, Appointment, connect_to_db


def create_user(username):
    """Create a new user."""

    user = User(username=username)

    return user


def get_user_by_username(username):
    """Return a user by username."""

    return User.query.filter(User.username == username).first()


def create_appointment(date, start_time, end_time, user_id):
    """Create an appointment."""

    appointment = Appointment(date=date, start_time=start_time, end_time=end_time, user_id=user_id)

    return appointment
    

def get_appointment_by_user(user_id):
    """Return user's appointments"""

    return Appointment.query.filter_by(user_id=user_id).all()


if __name__ == "__main__":
    from server import app

    connect_to_db(app)