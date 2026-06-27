from fastapi import FastAPI, Depends

from backend.schemas import QueryRequest
from backend.dependencies import get_agent
from backend.routes.agent_routes import router as agent_router
from agents.healthcare_agent import HealthcareAgent

# Create FastAPI application
app = FastAPI(
    title="Agentic Healthcare Assistant",
    version="1.0.0"
)

app.include_router(agent_router)
