import json

# Load the patients data
with open("data/mock_ehr/patients.json") as f:
    patients = json.load(f)

# Load the doctors data
with open("data/mock_ehr/doctors.json") as f:
    doctors = json.load(f)

# Load the appointments data
with open("data/mock_ehr/appointments.json") as f:
    appointments = json.load(f)

# Print length to check if data has been loaded correctly or not
print(f"Patients: {len(patients)}")
print(f"Doctors: {len(doctors)}")
print(f"Appointments: {len(appointments)}")