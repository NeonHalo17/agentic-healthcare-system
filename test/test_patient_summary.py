from rag.patient_summary_manager import PatientSummaryManager
from rag.rag_manager import RAGManager

# Build Patient Summary instance
summary_manager = PatientSummaryManager(
    "data/mock_ehr/patients.json"
)

documents = summary_manager.build_patient_summaries()

# Create RAGManager instance
rag = RAGManager()
# Create index and embeddings for the documents in the path
rag.build_index(documents)
# Perform semantic search based on vector search
results = rag.search(
    "patient with chronic kidney disease"
)

for result in results:

    print(result["source"])
    print(result["content"])
    print("-" * 50)