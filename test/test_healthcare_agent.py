from agents.healthcare_agent import (HealthcareAgent)

agent = HealthcareAgent()

queries = [

    "Book a nephrologist appointment for Rajesh Sharma",

    "Summarize latest treatment methods for chronic kidney disease",

    "Update Rajesh Sharma record with fatigue and nausea",

    "Show Rajesh Sharma's medical history"
]

for query in queries:

    plan = agent.run(query, "P001")

    print("\nQUERY:")
    print(query)

    print("\nPLAN:")
    print(plan)

