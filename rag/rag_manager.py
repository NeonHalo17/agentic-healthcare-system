import faiss
import numpy as np
from rag.embeddings import EmbeddingModel

# Define RAGManager class
class RAGManager:
    # Initialization function
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.documents = []
        self.index = None

    # Build index for all embeddings
    def build_index(self, documents):
        self.documents = documents
        # Get content from all the documents
        texts = [doc["content"]for doc in documents]
        # Generate embeddings for each of them
        embeddings = self.embedding_model.embed_documents(texts)
        # FAISS expects float32 format
        embeddings = np.array(embeddings, dtype=np.float32)
        # Fix the embedding dimension
        dimension = embeddings.shape[1] 
        # Create FAISS index
        self.index = faiss.IndexFlatL2(dimension)
        # Add generated embeddings to the FAISS index
        self.index.add(embeddings)

    # Search documents based on query and return top_k relevant documents
    def search(self, query, top_k=3):
        if self.index is None:
            raise RuntimeError("Index has not been built yet")
        
        # Embed the input query
        query_embedding = self.embedding_model.embed(query)
        query_embedding = np.array([query_embedding],dtype=np.float32)

        # Search and get results
        distance, indices = self.index.search(query_embedding, top_k)
        results = []
            
        # Return the relevant parts of the documents that are searched and relevant to the query
        for idx in indices[0]:
            if idx == -1:
                continue
            results.append(self.documents[idx])
            
        return results
                
    # Save FAISS index
    def save_index(self, path):
        if self.index is None:
            raise RuntimeError("Nothing to save.")
        # Write index to teh location passed
        faiss.write_index(self.index, path)

    # Load FAISS index
    def load_index(self, path):
        self.index = faiss.read_index(path)

    