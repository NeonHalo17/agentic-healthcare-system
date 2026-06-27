from agents.planner import Planner
from agents.response_generator import ResponseGenerator

from models.planner_models import Task

from tools.patient_tool import PatientTool
from tools.appointment_tool import AppointmentTool

from rag.rag_service import RAGService

from memory.memory_manager import MemoryManager


class HealthcareAgent:

    def __init__(self):

        self.planner = Planner()
        self.patient_tool = PatientTool()
        self.appointment_tool = AppointmentTool()
        self.rag_service = RAGService()
        self.memory = MemoryManager()
        self.response_generator = ResponseGenerator()

    def run(self, query: str, session_id: str = "default"):
        # Planning
        plan = self.planner.create_plan(query)

        # Save patient context
        if plan.patient_name:
            self.memory.save_patient_context(session_id, plan.patient_name)

        patient_name = (plan.patient_name or self.memory.get_patient_context(session_id))

        # Tool execution
        results = {}

        # Retrieve patient record
        if (Task.RETRIEVE_HISTORY in plan.tasks and patient_name):
            results["patient_record"] = (
                self.patient_tool.get_history(
                    patient_name
                )
            )

        # Book appointment
        if (Task.BOOK_APPOINTMENT in plan.tasks and plan.doctor_specialty):
            appointment = (
                self.appointment_tool.auto_book_appointment(
                    patient_name=patient_name,
                    specialty=plan.doctor_specialty
                )
            )
            results["appointment_confirmation"] = (appointment)

        # Medical search
        if Task.SEARCH_MEDICAL_INFO in plan.tasks:
            results["medical_information"] = (
                self.rag_service.retrieve_context(
                    query=query,
                    patient_query=patient_name,
                    disease_name=plan.disease_name
                )
            )

        # Update patient record
        if (Task.UPDATE_RECORD in plan.tasks and patient_name):
            update_result = (
                self.patient_tool.update_notes(
                    patient_name,
                    plan.update_note
                )
            )

            results["updated_notes"] = update_result

        # Save memory
        self.memory.save_interaction(session_id, query, results)

        # Generate final response
        answer = (
            self.response_generator.generate(
                query=query,
                plan=plan,
                tool_results=results
            )
        )

        return {
            "answer": answer,
            "tool_results": results
        }
