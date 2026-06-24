from agents.healthcare_agent import (HealthcareAgent)

agent = HealthcareAgent()

# Test 1
query = """
My father has chronic kidney disease.
Book a nephrologist appointment.
Also summarize latest treatment methods.
"""
result = agent.run(query=query, patient_id="P001")
print(result)

# Test 2
result = agent.run(query="Show patient history",patient_id="P001")
print(result)

# Task 3
result = agent.run(
query="""
    Update patient record.
    Add fatigue and nausea.
    """,
    patient_id="P001"
)
print(result)

# Task 4
query = """
Retrieve patient history.
Book a nephrologist appointment.
Summarize CKD treatment methods.
"""
result = agent.run(query=query,patient_id="P001")
print(result)