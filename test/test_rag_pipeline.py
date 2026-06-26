from rag.document_loader import DocumentLoader
from rag.rag_manager import RAGManager
from rag.rag_generator import RAGGenerator

# Load documents
loader = DocumentLoader(
    "data/medical_docs"
)

documents = loader.load_documents()

rag = RAGManager()
# Generate embeddings and index for the stored documents
rag.build_index(documents)

generator = RAGGenerator()

retrieved = rag.search(
    "What are the treatments for chronic kidney disease?"
)

answer = generator.generate(
    "What are the treatments for chronic kidney disease?",
    retrieved
)

print(answer)