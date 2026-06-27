from rag.document_loader import DocumentLoader
from rag.patient_summary_manager import PatientSummaryManager
from rag.rag_manager import RAGManager
from rag.rag_generator import RAGGenerator

# This is the entry point for the Healthcare Agent module, all calls to RAG services from the agent will go through here
class RAGService:
    # Initilization function
    def __init__(self):
        # Medical documents RAG
        self.medical_loader = DocumentLoader("data/medical_docs")
        # Load docuemnts
        medical_documents = self.medical_loader.load_documents()
        # Initialize RAGManager
        self.medical_rag = RAGManager()
        # Generate embeddings and index for the loaded documents
        self.medical_rag.build_index(medical_documents)

        # Patient Summary RAG
        self.patient_summary_manager = PatientSummaryManager("data/mock_ehr/patients.json")
        # Load patient data as patient summaries
        patient_documents = (self.patient_summary_manager.build_patient_summaries())
        # Initialize RAGManager
        self.patient_rag = RAGManager()
        # Generate embeddings and index for the loaded documents
        self.patient_rag.build_index(patient_documents)

        # Shared Generator
        self.generator = RAGGenerator()

    # Search for medical information
    def search_medical_information(self, query):
        """
        Retrieve relevant medical documents
        and generate a response.
        """
        # Perform RAG and return retrieved medical documents
        retrieved_documents = self.medical_rag.search(query)
        return self.generator.generate(query,retrieved_documents)

    # Search for patient context
    def search_patient_context(self, query):
        """
        Retrieve patient summaries.

        Returns the raw retrieved summaries for now.
        """
        return self.patient_rag.search(query)