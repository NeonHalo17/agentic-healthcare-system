from sentence_transformers import SentenceTransformer

# Loading embedding model only once instead of everytime a RAGManager object is instantiated
_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def get_embedding_model():
    return _model