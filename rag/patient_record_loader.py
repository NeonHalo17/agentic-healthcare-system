from pathlib import Path
from pypdf import PdfReader


class PatientRecordLoader:

    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)

    def load_documents(self):
        documents = []
        for pdf_file in self.folder_path.glob("*.pdf"):
            reader = PdfReader(pdf_file)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            documents.append(
                {
                    # Filename becomes the source
                    "source": pdf_file.stem,
                    "content": text.strip()
                }
            )

        return documents
