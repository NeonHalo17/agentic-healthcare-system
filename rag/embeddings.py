from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Wrapper around a SentenceTransformer model.
    Responsible only for generating embeddings.
    """
    # Initialization function
    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2" # 
        )

    # Generate embeddings for just a piece of text
    def embed(self, text: str):
        
        return self.model.encode(
            text,
            convert_to_numpy=True
        )
    
    # Generate embeddings for documents, can be a list of documents
    def embed_documents(self, documents: list[str]):

        return self.model.encode(
            documents,
            convert_to_numpy=True
        )