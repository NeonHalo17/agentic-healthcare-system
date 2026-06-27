from pydantic import BaseModel

# Everytime a query comes in from the frontend, need to validate it(in terms of structure) before sending it to our agentic workflow
class QueryRequest(BaseModel):

    session_id: str
    patient_id: str | None = None
    query: str