from pathlib import Path


class DocumentLoader:
    # Initializtion function
    def __init__(self, document_directory):
        self.document_directory = Path(document_directory)

    # Load all documents and return a dictionary with document content as values
    def load_documents(self):
        documents = []

        for idx, file_path in enumerate(self.document_directory.glob("*.txt")):
            # Open all documents with .txt extension and store them in a source content key value pair
            with open(file_path, "r", encoding="utf-8") as file:
                documents.append(
                    {
                        "id": idx,
                        "source": file_path.name,
                        "content": file.read()
                    }
                )

        return documents