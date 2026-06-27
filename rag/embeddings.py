from config.embedding_config import get_embedding_model

class EmbeddingModel:
    """
    Wrapper around a SentenceTransformer model.
    Responsible only for generating embeddings.
    """
    # Initialization function
    def __init__(self):
        self.model = get_embedding_model() # Initialize embedding model 

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