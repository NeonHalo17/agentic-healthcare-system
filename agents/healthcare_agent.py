from agents.planner import Planner
from models.planner_models import Task

from tools.patient_tool import PatientTool
from tools.appointment_tool import AppointmentTool
from rag.rag_service import RAGService
from agents.response_generator import ResponseGenerator 

from memory.memory_manager import (MemoryManager)

# Import Planner agent and all tools, we will call the tools here, this is the orchestrator agent

class HealthcareAgent:
    # Initialization function
    def __init__(self):
        # Initialize Agent and tools for the orchestrator
        self.planner = Planner()
        self.patient_tool = PatientTool()
        self.appointment_tool = (AppointmentTool())
        self.rag_service = (RAGService())
        # Initialize Memory for the Agent for current conversation
        self.memory = MemoryManager()
        # Final response
        self.response_generator = ResponseGenerator() 
        
    # Main method    
    def run(self, query, patient_id=None, session_id="default",):
        
        # Get plan from planner agent
        plan = self.planner.create_plan(query)
        print(plan)
        # Save patient name to contextual memory(conversation history)
        if plan.patient_name:
            self.memory.save_patient_context(session_id, plan.patient_name)
        
        
        # Initialize results dictionary that will be returned
        results = {}
        
        # Get patient_name from planner response(If is is there)
        patient_name = (plan.patient_name)
        
        if not patient_name:
            patient_name = (self.memory.get_patient_context(session_id))
        
        # If retreive_patient_history is in planner tasks, call get_history tool
        if (Task.RETRIEVE_HISTORY in plan.tasks and patient_id): 
            results["history"] = (self.patient_tool.get_history(patient_id))
            
        # If book_appointment is in planner tasks, call get_available_slots tool
        if (Task.BOOK_APPOINTMENT in plan.tasks and plan.doctor_specialty):
            appointment = self.appointment_tool.auto_book_appointment(patient_id=patient_id, specialty=plan.doctor_specialty)
            results["appointment_confirmation"] = appointment
            
        # If search_medical_info is in planner tasks, call disease_tool tool
        if (Task.SEARCH_MEDICAL_INFO in plan.tasks):
            medical_info = self.rag_service.search_medical_information(query)
            results["medical_information"] = (medical_info)
        
        # If update_record is in planner tasks, call update_notes tool
        if (Task.UPDATE_RECORD in plan.tasks and patient_id):
            update_result = self.patient_tool.update_notes(patient_id, plan.update_note)
            results["updated_notes"] = update_result
        
        # Save all interactions in conversation history
        self.memory.save_interaction(session_id, query, results)
        
        # Form output answer using retreived information and query in natural language
        answer = self.response_generator.generate(query=query, tool_results=results)
        
        return {
            "answer": answer,
            "tool_results": results,
            }