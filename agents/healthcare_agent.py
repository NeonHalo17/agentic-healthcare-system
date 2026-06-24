from agents.planner import Planner
from models.planner_models import Task

from tools.patient_tool import PatientTool
from tools.appointment_tool import AppointmentTool
from tools.disease_search_tool import DiseaseSearchTool

# Import Planner agent and all tools, we will call the tools here, this is the orchestrator agent

class HealthcareAgent:
    # Initialization function
    def __init__(self):
        # Initialize Agent and tools for the orchestrator
        self.planner = Planner()
        self.patient_tool = PatientTool()
        self.appointment_tool = (AppointmentTool())
        self.disease_tool = (DiseaseSearchTool())
        
    # Main method    
    def run(self, query, patient_id=None):
        # Get plan from planner agent
        plan = self.planner.create_plan(query)
        # Initialize results dictionary that will be returned
        results = {}
        # If retreive_patient_history is in planner tasks, call get_history tool
        
        if (Task.RETRIEVE_HISTORY in plan.tasks and patient_id): 
            results["history"] = (self.patient_tool.get_history(patient_id))
        # If book_appointment is in planner tasks, call get_available_slots tool
        if (Task.BOOK_APPOINTMENT in plan.tasks and plan.doctor_specialty):
            slots = self.appointment_tool.get_available_slots(plan.doctor_specialty)
            results["available_slots"] = slots
        # If search_medical_info is in planner tasks, call disease_tool tool
        if (Task.SEARCH_MEDICAL_INFO in plan.tasks):
            medical_info = self.disease_tool.search(query)
            results["medical_information"] = (medical_info)
        if (Task.UPDATE_RECORD in plan.tasks and patient_id):
            update_result = self.patient_tool.update_notes(patient_id, plan.update_note)
            results["updated_notes"] = update_result
        
        return results