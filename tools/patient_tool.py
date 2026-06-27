from rag.rag_service import RAGService


class PatientTool:

    def __init__(self):
        self.rag_service = RAGService()

    def get_patient(self, patient_name: str):
        """
        Retrieve the patient's clinical record
        from the Patient RAG.
        """
        if not patient_name:
            return None

        return self.rag_service.search_patient_context(patient_name)

    def get_patient_by_name(self, name: str):
        return self.get_patient(name)

    def get_history(self, patient_name: str):
        return self.get_patient(patient_name)
