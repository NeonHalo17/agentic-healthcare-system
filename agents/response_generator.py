import json

from config.llm_config import get_llm
from models.planner_models import Plan
from langchain_core.messages import SystemMessage, HumanMessage

# Using the query and retrieved information, return the output in natural language using llm
class ResponseGenerator:
    def __init__(self):
        self.llm = get_llm()

    def generate(self, query: str, plan: Plan, tool_results: dict) -> str:
        
        system = SystemMessage(
            content="""
            You are a healthcare assistant.

A planner has already decided which tools to execute.

Instructions:
- Answer ONLY using the information provided in Tool Results.
- Do not make assumptions or invent facts.
- If the requested information is unavailable, clearly state that.
- If multiple tool results are provided, combine them into one coherent answer.
- Do not mention the planner, tools, or internal workflow.
- Keep the response concise and professional.
            """
        )
        
        human = HumanMessage(
            content=f"""
            Below are the outputs returned by those tools.
            
            User Question:
{query}

Generated Plan:
{plan.model_dump_json(indent=2)}

Tool Results:
{json.dumps(tool_results, indent=2)}
            """
        )

        response = self.llm.invoke([system, human])
        return response.content