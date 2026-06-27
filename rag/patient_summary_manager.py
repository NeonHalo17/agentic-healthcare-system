import json


class PatientSummaryManager:
    # Initialization function
    def __init__(self, patient_file):
        self.patient_file = patient_file

    # Load patient data
    def load_patients(self):
        with open(self.patient_file, "r") as file:
            return json.load(file)

    # Build patient summaries from patient data
    def build_patient_summaries(self):
        patients = self.load_patients()
        summaries = []
        
        for patient in patients:
            summary = f"""
Patient Name: {patient['name']}

Age: {patient['age']}

Gender: {patient['gender']}

Diagnosis: {(patient['diagnosis'])}

Current Treatment: {(patient['treatment'])}

Allergies: {", ".join(patient['allergies'])}

Last Visit: {patient['last_visit']}

Clinical Notes: {patient['notes']}
"""

            summaries.append(
                {
                    "patient_id": patient["patient_id"],
                    "source": patient["name"],
                    "content": summary.strip()
                }
            )

        return summaries