import json
from pathlib import Path


class PatientTool:

    # Initialization function
    def __init__(self):
        # Set file path to the file patients.json, can be changed to wherever the patient data is coming from
        self.file_path = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "data"
            / "mock_ehr"
            / "patients.json"
        )
        
    # Load and parse the file as a json
    def _load_data(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    # Get patient records based on patient_id
    def get_patient(self, patient_id):
        # Call _load_data function and get the patient data as a json
        patients = self._load_data()
        # Iterate over each patient in the data
        for patient in patients:
            # If the patient_id is found, return that json entry
            if patient["patient_id"] == patient_id:
                return patient
        # If patient id is not found, return None
        return None

    # Get patient records based on patient name
    def get_patient_by_name(self, name):
        # Call _load_data functino and the patient data as a json
        patients = self._load_data()
        # Iterate over each patient in the data
        for patient in patients:
            # If there is a match, return that patient records
            if patient["name"].lower() == name.lower():
                return patient
        # If patient name is not found, return None
        return None

    # Return patient history in a standard format
    def get_history(self, patient_id):
        # Get patient records using the get_patient method
        patient = self.get_patient(patient_id)
        # If patient is not found, return None
        if not patient:
            return None

        # Define a standard format that the tool will return history in
        return {
            "diagnosis": patient["diagnosis"],
            "treatment": patient["treatment"],
            "notes": patient["notes"],
            "last_visit": patient["last_visit"]
        }

    # Update notes for a patient record
    def update_notes(self, patient_id, notes):
        # Load patients data
        patients = self._load_data()
        # Iterate over each patient in the database
        for patient in patients:
            # If match is hit, update the notes attribute with input notes
            if patient["patient_id"] == patient_id:
                patient["notes"] = notes
                # Write into the json file that is our synthetic data for now
                with open(self.file_path, "w") as f:
                    json.dump(
                        patients,
                        f,
                        indent=4
                    )
                # If change is made, return True
                return True
        # If no change made, that is, patient was not found, return False
        return False