from faker import Faker
import random
import pandas as pd

fake = Faker()

def create_hospital_domain(number_of_hospitals):
    hospitals = []
    for i in range(number_of_hospitals):
        hospitals.append(
            {
            "id": i+1,
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            }
        )
    return hospitals

def create_doctor_domain(number_of_doctors, hospitals):
    doctors = []
    for i in range(number_of_doctors):
        doctors_hospital = random.choice(hospitals)
        doctors.append(
            {
            "id": i+1,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "work_number": fake.phone_number(),
            "address": fake.street_address(),
            "city": doctors_hospital["city"],
            "state": doctors_hospital["state"],
            "hospital_id": doctors_hospital["id"]
            }
        )
    return doctors

def run():
    hospitals = create_hospital_domain(5)
    doctors = create_doctor_domain(50, hospitals)
    df = pd.DataFrame(doctors)