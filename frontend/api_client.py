import requests

from config import BACKEND_URL

# The frontend will call the backend from here
def query_agent(session_id: str, query: str):

    response = requests.post(
        f"{BACKEND_URL}/agent/query",
        json={
            "session_id": session_id,
            "query": query
        }
    )

    response.raise_for_status()

    return response.json()