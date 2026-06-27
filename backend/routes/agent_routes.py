from fastapi import APIRouter, Depends

from backend.schemas import QueryRequest
from backend.dependencies import get_agent

from agents.healthcare_agent import HealthcareAgent
# Route the request from the frontend to the agent
router = APIRouter(prefix="/agent",tags=["Healthcare Agent"])

# Only create one POST request for the query for now

# POST endpoint for user query, entry point of our application
@router.post("/query")
def query(request: QueryRequest,agent: HealthcareAgent = Depends(get_agent)):
    print("REQUEST:", request)
    result = agent.run(query=request.query, patient_id=request.patient_id, session_id=request.session_id)
    print("RESULT:", result)
    return result