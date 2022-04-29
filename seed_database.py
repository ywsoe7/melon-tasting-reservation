"""Script to seed database."""

import os
from random import choice, randint
from datetime import datetime
import crud, model, server
from faker import Faker

os.system('dropdb reservations')
os.system('createdb reservations')

model.connect_to_db(server.app)
model.db.create_all()

fake = Faker()

# create users
user_db = []
for i in range(10):
    email = fake.email()
    new_user = crud.create_user(email)
    user_db.append(new_user)

# create appointments
appointments = []
for i in range(10):
    date = fake.date_between('-1y', 'today')
    print(date)
    start_time= fake.time()
    end_time= fake.time()
    user_id = i+1
    new_appointment = crud.create_appointment(date, start_time, end_time, user_id)
    appointments.append(new_appointment)