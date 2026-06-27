from rag.rag_service import RAGService

# Initialize RAG service to call search methods
rag = RAGService()

print("=" * 50)
print("Medical Search")
print("=" * 50)

# call search_medical_information, uses medical_docs
response = rag.search_medical_information("What are the symptoms and treatment of chronic kidney disease?")
print(response)

print("\n")

print("=" * 50)
print("Patient Search")
print("=" * 50)

# call search_patient_context, uses patient data
patients = rag.search_patient_context("patient with chronic kidney disease")

for patient in patients:
    print(patient["source"])
    print(patient["content"])
    print("-" * 50)