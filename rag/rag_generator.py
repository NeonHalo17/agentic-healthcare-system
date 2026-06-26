from langchain_ollama import ChatOllama
from config.llm_config import get_llm

# Creating this class to generate a system prompt using the context retreived by the Vector Search
class RAGGenerator:
    def __init__(self):

        self.llm = get_llm()

    # Generate response using LLM
    def generate(self, query, retrieved_documents):
        """
        Generate an answer using retrieved context.
        """
        # Define context based on retrived_documents
        context = "\n\n".join(
            [
                f"Source: {doc['source']}\n\n{doc['content']}"
                for doc in retrieved_documents
            ]
        )
        # Define system prompt
        prompt = f"""
You are a helpful healthcare assistant.

Answer ONLY using the information provided below.

If the answer cannot be found in the provided context,
say:

"I could not find enough information."

Context:
{context}

Question:
{query} 

Answer:
"""
        # Get response
        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": [
                doc["source"]
                for doc in retrieved_documents
            ]
        }