from rag.document_loader import DocumentLoader
from rag.rag_manager import RAGManager

# Initialize documentloader and load medical documents
loader = DocumentLoader(
    "data/medical_docs"
)

documents = loader.load_documents()

# Initialize RAGManager
rag = RAGManager()
# Generate embeddings and FAISS index for all documents
rag.build_index(documents)
# Run search method
results = rag.search("kidney disease treatment")

print()
# Print results
for result in results:

    print(result["source"])
    print(result["content"])
    print("-" * 50)