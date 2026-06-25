from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

# Define the list of tasks the orchestrator can do, so that it may not hallucinate later on
class Task(str, Enum):
    RETRIEVE_HISTORY = "retrieve_patient_history"
    BOOK_APPOINTMENT = "book_appointment"
    SEARCH_MEDICAL_INFO = ("search_medical_information")
    UPDATE_RECORD = ("update_patient_record")

# Define a structure that the LLM has to give the output in
class Plan(BaseModel):
    tasks: List[Task]
    doctor_specialty: Optional[str] = None
    disease_name: Optional[str] = None
    patient_name: Optional[str] = None
    update_note: Optional[str] = None