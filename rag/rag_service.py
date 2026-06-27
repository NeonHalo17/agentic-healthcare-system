from rag.document_loader import DocumentLoader
from rag.patient_record_loader import PatientRecordLoader
from rag.rag_manager import RAGManager
from rag.medline_service import MedlineService


class RAGService:

    def __init__(self):
        # Medical Knowledge RAG
        self.medical_loader = DocumentLoader("data/medical_docs")

        medical_documents = (self.medical_loader.load_documents())
        self.medical_rag = RAGManager()
        self.medical_rag.build_index(medical_documents)

        # Patient Record RAG
        self.patient_loader = PatientRecordLoader("data/mock_ehr/patient_records")
        patient_documents = (self.patient_loader.load_documents())
        self.patient_rag = RAGManager()
        self.patient_rag.build_index(patient_documents)

        # External Knowledge
        self.medline = MedlineService()

    def search_medical_information(self, query: str):
        return self.medical_rag.search(query)

    def search_patient_context(self, patient_name: str):
        return self.patient_rag.search(patient_name)

    def retrieve_context(self, query: str, patient_query: str | None = None, disease_name: str | None = None):

        patient_context = None

        if patient_query:
            patient_context = (self.search_patient_context(patient_query))

        medical_context = (self.search_medical_information(query))
        
        external_context = None

        if disease_name:
            external_context = (self.medline.search(disease_name))

        return {
            "patient_context": patient_context,
            "medical_documents": medical_context,
            "external_reference": external_context
        }
