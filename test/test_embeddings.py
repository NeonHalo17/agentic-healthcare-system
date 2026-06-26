from rag.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()

text = "Chronic kidney disease is a progressive condition."

embedding = embedding_model.embed(text)

print(type(embedding))
print(embedding.shape)
print(embedding[:10])