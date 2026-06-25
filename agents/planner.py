import json
from config.llm_config import get_llm
from models.planner_models import Plan


class Planner:
    # Initialization function, get llm
    def __init__(self):
        self.llm = get_llm()
        self.structured_llm = self.llm.with_structured_output(Plan)

    def create_plan(self,query: str):
        # Define the system prompt
        prompt = f"""
You are a healthcare workflow planner.

Your job is to analyze a user's healthcare request and return a workflow plan.

Return ONLY valid JSON.

Available tasks:
- retrieve_patient_history
- book_appointment
- search_medical_information
- update_patient_record

Extract:

- doctor_specialty
- disease_name
- patient_name
- update_note

Doctor specialties that may appear:
- Nephrologist
- Cardiologist
- Pulmonologist
- Endocrinologist
- General Physician

Instructions:
1. Identify all required tasks.
2. Extract the doctor specialty if the user is requesting an appointment.
3. If no doctor specialty is mentioned, set doctor_specialty to null.
4. Return ONLY JSON.
5. Do not include explanations or markdown.

If the user wants to update a patient record,
extract the note content into update_note.

User Query:
{query}

Expected JSON Schema:

{{
    "tasks": [],
    "doctor_specialty": null,
    "disease_name": null,
    "patient_name": null,
    "update_note": null
}}

Example 1

User:
Book a nephrologist appointment for Rajesh Sharma.

Output:

{{
    "tasks": [
        "book_appointment"
    ],
    "doctor_specialty": "Nephrologist",
    "disease_name": null,
    "update_note": null
}}

Example 2

User:
Summarize latest treatment options for chronic kidney disease.

Output:

{{
    "tasks": [
        "search_medical_information"
    ],
    "doctor_specialty": null,
    "disease_name": "Chronic Kidney Disease",
    "update_note": null
}}

Example 3

User:
Update Rajesh Sharma's record with fatigue and nausea.

Output:

{{
    "tasks": [
        "update_patient_record"
    ],
    "doctor_specialty": null,
    "disease_name": null,
    "update_note": "fatigue and nausea"
}}
"""
        # Get response from the llm
        plan = self.structured_llm.invoke(prompt)

        return plan