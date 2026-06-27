import re
import requests
import xml.etree.ElementTree as ET


# Call external MedlinePlus API to retrieve medical information
class MedlineService:

    BASE_URL = "https://wsearch.nlm.nih.gov/ws/query"

    def clean_html(self, text: str) -> str:
        """Remove HTML tags from MedlinePlus responses."""
        if not text:
            return ""

        return re.sub(r"<[^>]+>", "", text).strip()

    def search(self, disease_name: str):
        try:
            response = requests.get(
                self.BASE_URL,
                params={
                    "db": "healthTopics",
                    "term": disease_name
                },
                timeout=10
            )

            response.raise_for_status()
            root = ET.fromstring(response.text)

            # Get only the highest-ranked document
            document = root.find(".//document")

            if document is None:
                return None

            item = {}

            for content in document.findall("content"):
                name = content.attrib.get("name")
                if name:
                    item[name] = self.clean_html(content.text)

            return {
                "title": item.get("title"),
                "summary": item.get("FullSummary"),
                "source": "MedlinePlus",
                "url": item.get("url")
            }

        except Exception as e:
            return {
                "error": str(e),
                "source": "MedlinePlus"
            }