from agents.planner import Planner

planner = Planner()

query = """
My father has chronic kidney disease.
Book a nephrologist appointment.
Also summarize latest treatment methods.
"""

plan = planner.create_plan(
    query
)

print(plan)