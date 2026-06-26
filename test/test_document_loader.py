from rag.document_loader import DocumentLoader

# Testing document_loader
loader = DocumentLoader(
    "data/medical_docs"
)

documents = loader.load_documents()

print(f"{len(documents)} documents loaded\n")

for document in documents:

    print(document["source"])
    print(document["content"])
    print("-" * 50)