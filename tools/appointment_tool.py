import json
from pathlib import Path


class AppointmentTool:

    # Define initilization method, called when object is created
    def __init__(self):
        root = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "data"
            / "mock_ehr"
        )
        # load the data paths into two attributes of this class
        self.doctors_file = root / "doctors.json"
        self.appointments_file = root / "appointments.json"

    # Load the doctors data
    def _load_doctors(self):
        # Open the file and load and parse the data into a json
        with open(self.doctors_file) as f:
            return json.load(f)

    # Load the appointments data
    def _load_appointments(self):
        # Open the file and load and parse the data into a json
        with open(self.appointments_file) as f:
            return json.load(f)

    # Find doctor based on specialty
    def find_doctor(self, specialty):
        # Load doctors data
        doctors = self._load_doctors()
        # Return list of doctors with required speciality
        return [
            doctor
            for doctor in doctors
            if doctor["specialty"].lower()
            == specialty.lower()
        ]

    # Get all available slots of the required specialized doctors
    def get_available_slots(self, specialty):
        # Get the list of specialized doctors needed
        doctors = self.find_doctor(specialty)
        # Initialize empty list of slots
        slots = []
        # Iterate over doctors data
        for doctor in doctors:
            # Iterate over slots in that particular doctor records
            for slot in doctor["available_slots"]:
                # Track the data in the empty slots dictionary we defined earlier
                slots.append(
                    {
                        "doctor_id": doctor["doctor_id"],
                        "doctor_name": doctor["name"],
                        "specialty": doctor["specialty"],
                        "slot": slot
                    }
                )
        # Return the list of available slots along with doctor information
        return slots

    # Get list of patient appointments
    def get_patient_appointments(self, patient_id):
        # Load appointments data
        appointments = self._load_appointments()
        # Return list of appointments under the passed patient_id
        return [
            appt
            for appt in appointments
            if appt["patient_id"] == patient_id
        ]

    # Define method to book appointments
    def book_appointment(self, patient_id, doctor_id, slot):
        # Load doctors data
        doctors = self._load_doctors()
        doctor_found = None
        # Iterate over each doctor in database
        for doctor in doctors:
            # Find our doctor, match by doctor_id
            if doctor["doctor_id"] == doctor_id:
                doctor_found = doctor
                break
            
        # If doctor not found, return appropriate message.
        if not doctor_found:
            return {
                "status": "failed",
                "message": "Doctor not found. Check Doctor ID again."
            }
            
        # If slot not available under the passed doctor, return appropriate message
        if slot not in doctor_found["available_slots"]:
            return {
                "status": "failed",
                "message": "Slot unavailable"
            }
            
        # Remove booked slot from the doctor
        doctor_found["available_slots"].remove(
            slot
        )
        # Save updated doctors.json
        with open(self.doctors_file, "w") as f:
            json.dump(
                doctors,
                f,
                indent=4
            )
        # Load appointments data
        appointments = self._load_appointments()
        # Write up an appointment record as is expected from the appointment database
        appointment = {
            "appointment_id": f"A{len(appointments)+1:03d}",
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "appointment_date": slot,
            "status": "Scheduled"
        }
        # Add the record to the appointments data
        appointments.append(appointment)

        # Update the appointments.json file to reflect data updation
        with open(self.appointments_file,"w") as f:
            json.dump(
                appointments,
                f,
                indent=4
            )
        # Return appropriate message, with appointment details post success
        return {
            "status": "success",
            "appointment": appointment
        }